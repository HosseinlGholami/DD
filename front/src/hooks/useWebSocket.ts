// src/hooks/useWebSocket.ts
import { useEffect, useState } from 'react';
import { io, Socket } from 'socket.io-client';
import useStore from '../store/store';

interface DataPoint {
    x: number;
    y: number;
    z: number;
}
interface Dimension {
    w: number;
    h: number;
    l: number;
    weight: number;
}

type DataVal = DataPoint | Dimension;

interface SocketData {
    cmd: string;
    data?: DataVal[]
};

interface PlotData {
    x: number[];
    y: number[];
    z: number[];
};

const useWebSocket = (url: string) => {
    // const [socketData, setSocketData] = useState<SocketData>({ cmd: '', data: [] });
    const [plotData, setPlotData] = useState<PlotData>({ x: [], y: [], z: [] });

    useEffect(() => {
        const socket: Socket = io(url);

        socket.on('connect', () => {
            console.log('Connected to WebSocket');
        });

        socket.on('meta', (newData: Partial<SocketData>) => {
            // console.log('Received new data:', newData);

            if (newData.cmd === "start_scan") {
                console.log('Scan started');
                // useStore.setState({command: "start_scan"})
                setPlotData({ x: [], y: [], z: [] });
            } else if (newData.cmd === "end_scan") {
                console.log('Scan ended');
                if (newData.data && 'w' in newData.data[0]) {
                    useStore.setState({
                        result: {
                            w: newData.data[0].w,
                            l: newData.data[0].l,
                            h: newData.data[0].h,
                            weight: newData.data[0].weight,
                        },
                        command: "end_scan"
                    })
                }
                // setSocketData({ cmd: 'end_scan' });
            } else if (newData.cmd === "plot") {
                // console.log('Plot data:', newData.data);
                // setSocketData({ cmd: 'plot', data: newData.data })
                if (newData.data && 'x' in newData.data[0]) {
                    setPlotData((prevPlotData) => ({
                        x: [...prevPlotData.x, ...newData.data!.map(point => (point as DataPoint).x)],
                        y: [...prevPlotData.y, ...newData.data!.map(point => (point as DataPoint).y)],
                        z: [...prevPlotData.z, ...newData.data!.map(point => (point as DataPoint).z)],
                    }));
                }
            } else if (newData.cmd === "img_ready") {
                useStore.setState({ command: "img_ready" });
            } else {
                // console.log(newData)
            }
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