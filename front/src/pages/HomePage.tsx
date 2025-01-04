// src/pages/HomePage.tsx
import React from 'react';
import DimensionPlot from '../components/DimensionPlot';
import useWebSocket from '../hooks/useWebSocket';
import 'bootstrap/dist/css/bootstrap.min.css'; // Ensure Bootstrap CSS is imported
import QRCodeCard from '../components/QRCodeCard';
import { ReactComponent as PlayIcon } from '../assets/icons/play.svg';
import { ReactComponent as StopIcon } from '../assets/icons/stop.svg';
import { ReactComponent as NightIcon } from '../assets/icons/night.svg';
import { ReactComponent as ProductScanIcon } from '../assets/icons/scan_product.svg';
import { ReactComponent as ScanToStartIcon } from '../assets/icons/scan_to_start.svg';
import { ReactComponent as RetryIcon } from '../assets/icons/retry.svg';
import { ReactComponent as PauseIcon } from '../assets/icons/pause.svg';
import { ReactComponent as FinishIcon } from '../assets/icons/finish.svg';
import Icon from '../components/Icon';
import InfoCard from '../components/InfoCard';
// import logo from "../statics/dk.png";

interface PlotData {
    x: number[];
    y: number[];
    z: number[];
}

const HomePage: React.FC = () => {
    const { plotData, setPlotData } = useWebSocket('http://localhost:5003');  // Update to your WebSocket URL

    const handleStart = async () => {
        try {
            const response = await fetch('http://localhost:5003/start');  // Adjust this to your Flask app's URL
            if (response.ok) {
                setPlotData({ x: [], y: [], z: [] });  // Clear plot data
                console.log('Plot data cleared');
            } else {
                console.error('Failed to clear plot data');
            }
        } catch (error) {
            console.error('Error calling /start API:', error);
        }
    };

    return (
        // <div className="tw-p-4 tw-grid tw-grid-rows-[auto,1fr] tw-justify-items-center">
        //     <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
        //         <QRCodeCard 
        //             qrValue="HOK" 
        //             text="شروع اسکن" 
        //             icon={PlayIcon} 
        //         />
        //         <QRCodeCard 
        //             qrValue="NOK" 
        //             text="پاک کردن" 
        //             icon={StopIcon} 
        //         />
        //         <div className='tw-col-span-2' />

        //         <QRCodeCard 
        //             qrValue="DARK" 
        //             text="حالت شب" 
        //             icon={NightIcon} 
        //         />
        //     </div>

        //     <div className="tw-mt-8 tw-flex tw-flex-col tw-items-center">
        //         <Icon SvgIcon={ScanToStartIcon} height={200} width={200} />
        //         <div className="tw-text-center tw-text-gray-500 tw-mt-4">
        //             برای شروع QR Code را اسکن کنید
        //         </div>
        //     </div>
        // </div>




        // <div className="tw-p-4 tw-grid tw-grid-rows-[auto,1fr] tw-justify-items-center">
        //     <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
        //         <div className='tw-col-span-4'/>
        //         <QRCodeCard
        //             qrValue="DARK"
        //             text="حالت شب"
        //             icon={NightIcon}
        //         />
        //     </div>

        //     <div className="tw-mt-8 tw-flex tw-flex-col tw-items-center">
        //         <Icon SvgIcon={ProductScanIcon} height={200} width={200} />
        //         <div className="tw-text-center tw-text-gray-500 tw-mt-4">
        //             برای شروع سریال کالا را اسکن کنید
        //         </div>
        //     </div>
        // </div>




        // <div className="tw-p-4 tw-grid tw-grid-rows-[auto,1fr] tw-gap-8">
        //     <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
        //         <QRCodeCard
        //             qrValue="PAUSE"
        //             text="توقف اسکن"
        //             icon={PauseIcon}
        //             color="#DE3730"
        //         />
        //         <QRCodeCard
        //             qrValue="RETRY"
        //             text="اسکن مجدد"
        //             icon={RetryIcon}
        //         />
        //         <div className='tw-col-span-2' />

        //         <QRCodeCard
        //             qrValue="DARK"
        //             text="حالت شب"
        //             icon={NightIcon}
        //         />
        //     </div>

        //     <div className="tw-grid tw-grid-cols-2 tw-gap-2 tw-grid-rows-2">
        //         <InfoCard title="مشخصات کالا" className="tw-col-span-1">
        //             <div className="tw-grid tw-grid-rows-5 tw-gap-2">
        //                 <div>طول: ***</div>
        //                 <div>عرض: ***</div>
        //                 <div>ارتفاع: ***</div>
        //                 <div>وزن: ***</div>
        //                 <div>سایر کالا: ***</div>
        //             </div>
        //         </InfoCard>
        //         <InfoCard title="نمودار نقطه‌ای" className="tw-col-span-1">
        //             <div className="tw-h-48 tw-bg-gray-100 tw-rounded-md tw-flex tw-items-center tw-justify-center">
        //                 3D Scatter Plot Here
        //             </div>
        //         </InfoCard>

        //         <InfoCard title="تصویر" className="tw-col-span-2">
        //             <div className="tw-h-48 tw-bg-gray-100 tw-rounded-md tw-flex tw-items-center tw-justify-center">
        //                 Image Placeholder
        //             </div>
        //         </InfoCard>
        //     </div>
        // </div>

        <div className="tw-p-4 tw-grid tw-grid-rows-[auto,1fr] tw-gap-8">
            <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
                <QRCodeCard
                    qrValue="FINISH"
                    text="پایان اسکن"
                    icon={FinishIcon}
                />
                <div className='tw-col-span-4' />
            </div>

            <div className="tw-grid tw-grid-cols-2 tw-gap-2 tw-grid-rows-2">
                <InfoCard title="مشخصات کالا" className="tw-col-span-1">
                    <div className="tw-grid tw-grid-rows-5 tw-gap-2">
                        <div>طول: ***</div>
                        <div>عرض: ***</div>
                        <div>ارتفاع: ***</div>
                        <div>وزن: ***</div>
                        <div>سایر کالا: ***</div>
                    </div>
                </InfoCard>
                <InfoCard title="نمودار نقطه‌ای" className="tw-col-span-1">
                    <div className="tw-h-48 tw-bg-gray-100 tw-rounded-md tw-flex tw-items-center tw-justify-center">
                        3D Scatter Plot Here
                    </div>
                </InfoCard>

                <InfoCard title="تصویر" className="tw-col-span-2">
                    <div className="tw-h-48 tw-bg-gray-100 tw-rounded-md tw-flex tw-items-center tw-justify-center">
                        Image Placeholder
                    </div>
                </InfoCard>
            </div>
        </div>
    );
};

export default HomePage;