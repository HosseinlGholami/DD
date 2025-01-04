
import numpy as np
import serial
import struct


class Lidar:
    START_HEADER_BYTE = '54'
    PACKET_LENGTH_BYTE = '2c'

    HEADER = 0
    LENGTH = 1
    SPEED = 2
    START_ANGLE = 3
    DATA_START = 4
    DATA_END = 28
    END_ANGLE = 28
    TIME_STAMP = 29

    angle_offset_degree = -3.4  # Lidar not being aligned
    packed_struct = '<bbHHhBhBhBhBhBhBhBhBhBhBhBhBHHx'

    crc_table = [
        0x00, 0x4d, 0x9a, 0xd7, 0x79, 0x34, 0xe3,
        0xae, 0xf2, 0xbf, 0x68, 0x25, 0x8b, 0xc6, 0x11, 0x5c, 0xa9, 0xe4, 0x33,
        0x7e, 0xd0, 0x9d, 0x4a, 0x07, 0x5b, 0x16, 0xc1, 0x8c, 0x22, 0x6f, 0xb8,
        0xf5, 0x1f, 0x52, 0x85, 0xc8, 0x66, 0x2b, 0xfc, 0xb1, 0xed, 0xa0, 0x77,
        0x3a, 0x94, 0xd9, 0x0e, 0x43, 0xb6, 0xfb, 0x2c, 0x61, 0xcf, 0x82, 0x55,
        0x18, 0x44, 0x09, 0xde, 0x93, 0x3d, 0x70, 0xa7, 0xea, 0x3e, 0x73, 0xa4,
        0xe9, 0x47, 0x0a, 0xdd, 0x90, 0xcc, 0x81, 0x56, 0x1b, 0xb5, 0xf8, 0x2f,
        0x62, 0x97, 0xda, 0x0d, 0x40, 0xee, 0xa3, 0x74, 0x39, 0x65, 0x28, 0xff,
        0xb2, 0x1c, 0x51, 0x86, 0xcb, 0x21, 0x6c, 0xbb, 0xf6, 0x58, 0x15, 0xc2,
        0x8f, 0xd3, 0x9e, 0x49, 0x04, 0xaa, 0xe7, 0x30, 0x7d, 0x88, 0xc5, 0x12,
        0x5f, 0xf1, 0xbc, 0x6b, 0x26, 0x7a, 0x37, 0xe0, 0xad, 0x03, 0x4e, 0x99,
        0xd4, 0x7c, 0x31, 0xe6, 0xab, 0x05, 0x48, 0x9f, 0xd2, 0x8e, 0xc3, 0x14,
        0x59, 0xf7, 0xba, 0x6d, 0x20, 0xd5, 0x98, 0x4f, 0x02, 0xac, 0xe1, 0x36,
        0x7b, 0x27, 0x6a, 0xbd, 0xf0, 0x5e, 0x13, 0xc4, 0x89, 0x63, 0x2e, 0xf9,
        0xb4, 0x1a, 0x57, 0x80, 0xcd, 0x91, 0xdc, 0x0b, 0x46, 0xe8, 0xa5, 0x72,
        0x3f, 0xca, 0x87, 0x50, 0x1d, 0xb3, 0xfe, 0x29, 0x64, 0x38, 0x75, 0xa2,
        0xef, 0x41, 0x0c, 0xdb, 0x96, 0x42, 0x0f, 0xd8, 0x95, 0x3b, 0x76, 0xa1,
        0xec, 0xb0, 0xfd, 0x2a, 0x67, 0xc9, 0x84, 0x53, 0x1e, 0xeb, 0xa6, 0x71,
        0x3c, 0x92, 0xdf, 0x08, 0x45, 0x19, 0x54, 0x83, 0xce, 0x60, 0x2d, 0xfa,
        0xb7, 0x5d, 0x10, 0xc7, 0x8a, 0x24, 0x69, 0xbe, 0xf3, 0xaf, 0xe2, 0x35,
        0x78, 0xd6, 0x9b, 0x4c, 0x01, 0xf4, 0xb9, 0x6e, 0x23, 0x8d, 0xc0, 0x17,
        0x5a, 0x06, 0x4b, 0x9c, 0xd1, 0x7f, 0x32, 0xe5, 0xa8
    ]

    def __init__(self, port,callback, min_confidence_level=200):
        self.port = port
        self.serial = serial.Serial(port, baudrate=115200, timeout=1)
        self.min_confidence_level = min_confidence_level
        self.callback = callback

    def calculate_crc(self, input_packet):
        crc = 0
        for i in range(46):
            byte_value = input_packet[2 * i: 2 * i + 2]
            crc = Lidar.crc_table[(crc ^ int(byte_value, 16)) & 0xff]
        return crc

    def decode_byte_packets(self, input_byte_packet):
        return struct.unpack(Lidar.packed_struct, input_byte_packet)

    def align_packets(self):
        while True:
            try:
                input_byte = self.serial.read().hex()
            except:
                print(f"[debug:]:input_byte is empty")
                input_byte = None
            if input_byte == Lidar.START_HEADER_BYTE:
                try:
                    packet_length_byte = self.serial.read().hex()
                except:
                    packet_length_byte = None
                    print(f"[debug:]:packet_length_byte is empty")

                if packet_length_byte == Lidar.PACKET_LENGTH_BYTE:
                    try:
                        self.serial.read(45)  # read the rest of the packet
                    except:
                        print(f"[debug:]:self.serial.read(45) is empty")
                    break

    def reset_input_buffer(self):
        self.serial.reset_input_buffer()
        self.serial.close()
        self.serial.open()

    def is_packet_valid(self, data_packet):
        data_packet_hex = data_packet.hex()
        crc_byte = data_packet[46]
        calculated_crc = self.calculate_crc(data_packet_hex[:-2])
        return crc_byte == calculated_crc

    def degree_to_radians(self, degree):
        return degree / 180 * np.pi

    def get_lidar_packets(self):
        total_angles = np.array([])
        total_distances = np.array([])
        total_confidences = np.array([])
        
        while True:
            try:
                data_packet = self.serial.read(47)
            except:
                print(f"[debug:]: data_packet is empty")
                data_packet= None
            if data_packet:
                if not self.is_packet_valid(data_packet):
                    self.align_packets()
                    continue

                decoded_packet = self.decode_byte_packets(data_packet)
                
                # Determine angles
                if decoded_packet[Lidar.END_ANGLE] < decoded_packet[Lidar.START_ANGLE]:
                    angles = np.linspace(decoded_packet[Lidar.START_ANGLE] / 100, 
                                        decoded_packet[Lidar.END_ANGLE] / 100 + 360, 12)
                else:
                    angles = np.linspace(decoded_packet[Lidar.START_ANGLE] / 100, 
                                        decoded_packet[Lidar.END_ANGLE] / 100, 12)

                # Apply angle offset and convert to radians
                angles = self.degree_to_radians(angles + Lidar.angle_offset_degree)
                distances = decoded_packet[Lidar.DATA_START:Lidar.DATA_END:2]
                confidences = decoded_packet[Lidar.DATA_START + 1:Lidar.DATA_END + 1:2]
                timestamp = decoded_packet[Lidar.TIME_STAMP]

                # Append data
                total_angles = np.concatenate((total_angles, angles), axis=0)
                total_distances = np.concatenate((total_distances, distances), axis=0)
                total_confidences = np.concatenate((total_confidences, confidences), axis=0)

                # Filter by confidence level
                mask = total_confidences > self.min_confidence_level
                filtered_angles = total_angles[mask]
                filtered_distances = total_distances[mask]
                filtered_confidences = total_confidences[mask]
                
                # Pass data to callback, if provided
                if self.callback:
                    self.callback(filtered_distances, filtered_angles, filtered_confidences, timestamp)


def degree_to_radians(degree):
    return degree / 180 * np.pi

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y
