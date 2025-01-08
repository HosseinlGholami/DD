// src/pages/HomePage.tsx
import React from 'react';
import ProductScanState from '../components/states/ProductScanState';
import StartScanState from '../components/states/StartScanState';
import ScanState from '../components/states/ScanState';
import useStore from '../store/store';

const MainPage: React.FC = () => {

    const { currentState } = useStore();
    let StateComponent;

    switch (currentState) {
        case 'ProductScan':
            StateComponent = ProductScanState;
            break;
        case 'StartScan':
            StateComponent = StartScanState;
            break;
        case 'Scan':
            StateComponent = ScanState;
            break;
        default:
            StateComponent = null;
    }

    return (
        <div>
            {StateComponent && <StateComponent />}
        </div>
    );
};

export default MainPage;