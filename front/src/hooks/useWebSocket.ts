// src/hooks/useWebSocket.ts
import { useEffect, useState } from 'react';
import { io, Socket } from 'socket.io-client';

interface SocketData {
    cmd: string;
    data?: {
        x?: number;
        y?: number;
        z?: number;
        url?: string;
        w?: number;
    }
};

interface PlotData {
    x: number[];
    y: number[];
    z: number[];
};

const useWebSocket = (url: string) => {
    const [socketData, setSocketData] = useState<SocketData>({ cmd: '', data: {} });
    const [plotData, setPlotData] = useState<PlotData>({ x: [], y: [], z: [] });

    useEffect(() => {
        const socket: Socket = io(url);

        socket.on('connect', () => {
            console.log('Connected to WebSocket');
        });

        socket.on('meta', (newData: Partial<SocketData>) => {
            console.log('Received new data:', newData);

            if (newData.cmd === "start_scan") {
                console.log('Scan started');
                setSocketData({ cmd: 'start_scan' });
            } else if (newData.cmd === "end_scan") {
                console.log('Scan ended');
                setSocketData({ cmd: 'end_scan' });
            } else if (newData.cmd === "plot") {
                console.log('Plot data:', newData.data);
                setSocketData({ cmd: 'plot', data: newData.data });
                setPlotData((prevPlotData) => ({
                    x: newData.data && newData.data.x !== undefined ? [...prevPlotData.x, newData.data.x] : prevPlotData.x,
                    y: newData.data && newData.data.y !== undefined ? [...prevPlotData.y, newData.data.y] : prevPlotData.y,
                    z: newData.data && newData.data.z !== undefined ? [...prevPlotData.z, newData.data.z] : prevPlotData.z,
                }));
            } else {
                console.log("I GOT KOSSHER!")
                console.log(newData)
            }


            // setPlotData((prevPlotData) => ({
            //     x: newData.x !== undefined ? [...prevPlotData.x, ...newData.x] : prevPlotData.x,
            //     y: newData.y !== undefined ? [...prevPlotData.y, ...newData.y] : prevPlotData.y,
            //     z: newData.z !== undefined ? [...prevPlotData.z, ...newData.z] : prevPlotData.z,
            // }));
        });

        return () => {
            socket.off('meta');
            socket.off('connect');
            socket.disconnect();
        };
    }, [url]);

    return { plotData, setPlotData };
};

export default useWebSocket;