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

const endProc = async () => {
    try {
        const response = await axios.post(LOCAL_API_URL + '/end-proc');
        if (response.status === 200 && response.data.result === "OK") {
            console.log('Process finished!');
            return true;
        } else {
            console.error('Failed to End Process.');
            return false;
        }
    } catch (error) {
        console.error('Error calling end API:', error);
        return false;
    }
}

const zerotare = async () => {
    try {
        const response = await axios.post(LOCAL_API_URL + '/zerotare');
        if (response.status === 200) {
            console.log('Zerotare Successful!');
            return true;
        } else {
            console.error('Zerotare Failed.');
            return false;
        }
    } catch (error) {
        console.error('Error calling zerotare API:', error);
        return false;
    }
}

export { startScan, stopScan, endProc, zerotare };