import { create } from 'zustand';

interface AppState {
    currentState: 'ProductScan' | 'StartScan' | 'Scan';
    barcode: string;
    command: string;
    result: {
        w: number;
        h: number;
        l: number;
        weight: number;
    }
}

const useStore = create<AppState>((set) => ({
    currentState: 'ProductScan',
    barcode: '',
    command: '',
    result: {
        l: -1,
        h: -1,
        w: -1,
        weight: -1
    }
}));

export default useStore;