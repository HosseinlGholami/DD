import { create } from 'zustand';

interface AppState {
    currentState: 'ProductScan' | 'StartScan' | 'Scan';
    barcode: string;
}

const useStore = create<AppState>((set) => ({
    currentState: 'ProductScan',
    barcode: '',
}));

export default useStore;