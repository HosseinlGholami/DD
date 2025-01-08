import neopixel
import board
import time


NUM_PIXLE = 310
PIXLE_PIN = board.D10
pixels = neopixel.NeoPixel( PIXLE_PIN,NUM_PIXLE , brightness = 1, auto_write = False)


def fill_color(cl):
    pixels.fill(cl)
    pixels.show()


def do_flush():
    fill_color((255,255,255))

def end_flush():
    fill_color((0,0,0))



if __name__ == "__main__":
    while True:
        
        fill_color((255,255,255))
        time.sleep(1)
        print("255,0,0")

        fill_color((0,255,0))
        time.sleep(1)
        print("0,0,0")

        fill_color((0,0,255))
        time.sleep(1)
        print("0,0,255")


# for i in range(NUM_PIXLE):
#     pixels[i] = (0, 100, 0)

# pixels.show()

# time.sleep(5)

# pixels.fill((0,0,0))



