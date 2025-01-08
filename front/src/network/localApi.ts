import axios from 'axios';
import { LOCAL_API_URL } from './apiUrl';

const startScan = async (barcode: string) => {
    try {
        const response = await axios.post(LOCAL_API_URL + '/start', { "barcode": barcode });
        if (response.status === 200) {
            console.log('Scan started');
            return true;
        } else {
            console.error('Failed to start scan');
            return false;
        }
    } catch (error) {
        console.error('Error calling start API:', error);
        return false;
    }
}


const stopScan = async () => {
    try {
        const response = await axios.post(LOCAL_API_URL + '/stop');
        if (response.status === 200) {
            console.log('Scan stopped');
            return true;
        } else {
            console.error('Failed to stop scan');
            return false;
        }
    } catch (error) {
        console.error('Error calling stop API:', error);
        return false;
    }
}

export { startScan, stopScan };