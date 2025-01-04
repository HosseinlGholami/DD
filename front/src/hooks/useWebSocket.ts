// src/hooks/useWebSocket.ts
import { useEffect, useState } from 'react';
import { io, Socket } from 'socket.io-client';

interface PlotData {
    x: number[];
    y: number[];
    z: number[];
}

const useWebSocket = (url: string) => {
    const [plotData, setPlotData] = useState<PlotData>({ x: [], y: [], z: [] });

    useEffect(() => {
        const socket: Socket = io(url);

        socket.on('connect', () => {
            console.log('Connected to WebSocket');
        });

        socket.on('meta', (newData: Partial<PlotData>) => {
            console.log('Received new data:', newData);

            setPlotData((prevPlotData) => ({
                x: newData.x !== undefined ? [...prevPlotData.x, ...newData.x] : prevPlotData.x,
                y: newData.y !== undefined ? [...prevPlotData.y, ...newData.y] : prevPlotData.y,
                z: newData.z !== undefined ? [...prevPlotData.z, ...newData.z] : prevPlotData.z,
            }));
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