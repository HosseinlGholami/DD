// src/pages/HomePage.tsx
import React from "react";
import DimensionPlot from "../DimensionPlot";
import useWebSocket from "../../hooks/useWebSocket";
import QRCodeCard from "../ui/QRCodeCard";
import { ReactComponent as NightIcon } from "../../assets/icons/night.svg";
import { ReactComponent as RetryIcon } from "../../assets/icons/retry.svg";
import { ReactComponent as PauseIcon } from "../../assets/icons/pause.svg";
import { ReactComponent as FinishIcon } from "../../assets/icons/finish.svg";
// import Icon from "../ui/Icon";
import InfoCard from "../ui/InfoCard";
// import InputBox from "../ui/Inputbox";
import Skeleton from "../ui/Skeleton";
import useStore from "../../store/store";
import { startScan, stopScan } from "../../network/localApi";
import { useScanner } from "../../hooks/useScanner";
import WS_URL from "../../network/wsUrl";
import { LOCAL_API_URL } from "../../network/apiUrl";

interface PlotData {
  x: number[];
  y: number[];
  z: number[];
}

const ScanState: React.FC = () => {
  const { plotData, setPlotData } = useWebSocket(LOCAL_API_URL); // Update to your WebSocket URL
  //   const [command, setCommand] = React.useState<string>("");
  const [loading, setLoading] = React.useState<boolean>(true);

  useScanner(async (barcode: string) => {
    if (barcode === "FINISH") {
      useStore.setState({ currentState: "ProductScan" });
    } else if (barcode === "PAUSE") {
      if (await stopScan()) {
        console.log("Scan paused");
        setLoading(false);
        // TODO: show toast
        // TODO: set values to null
      } else {
        console.log("Failed to pause scan");
        setLoading(false);
      }
    } else if (barcode === "RETRY") {
      const barcode = useStore.getState().barcode;
      if (await startScan(barcode)) {
        console.log("Scan restarted");
        setLoading(true);
        // TODO: show toast
      } else {
        console.error("Failed to restart scan");
        setLoading(true);
      }
    }
  });

  return (
    <div className="tw-p-4 tw-grid tw-grid-rows-[auto,1fr] tw-gap-8">
      {!loading && (
        <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
          <QRCodeCard qrValue="FINISH" text="پایان اسکن" icon={FinishIcon} />
          <QRCodeCard qrValue="RETRY" text="اسکن مجدد" icon={RetryIcon} />
          <div className="tw-col-span-2" />
          <QRCodeCard qrValue="DARK" text="حالت شب" icon={NightIcon} />
        </div>
      )}
      {loading && (
        <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
          <QRCodeCard
            qrValue="PAUSE"
            text="توقف اسکن"
            icon={PauseIcon}
            color="#DE3730"
          />

          <div className="tw-col-span-3" />

          <QRCodeCard qrValue="DARK" text="حالت شب" icon={NightIcon} />
        </div>
      )}
      <div className="tw-grid tw-grid-cols-5 tw-gap-2 tw-grid-rows-1">
        {loading ? (
          <div className="tw-col-span-1">
            <InfoCard title="مشخصات کالا" className="tw-col-span-1">
              <div className="tw-grid tw-grid-rows-5 tw-gap-2">
                <Skeleton className="tw-h-8" />
                <Skeleton className="tw-h-8" />
                <Skeleton className="tw-h-8" />
                <Skeleton className="tw-h-8" />
                <Skeleton className="tw-h-8" />
              </div>
            </InfoCard>
          </div>
        ) : (
          <InfoCard title="مشخصات کالا" className="tw-col-span-1">
            <div className="tw-grid tw-grid-rows-5 tw-gap-2">
              <div>طول: ***</div>
              <div>عرض: ***</div>
              <div>ارتفاع: ***</div>
              <div>وزن: ***</div>
              <div>سایر کالا: ***</div>
            </div>
          </InfoCard>
        )}
        <InfoCard title="نمودار نقطه‌ای" className="tw-col-span-2">
          <div className="tw-h-48 tw-bg-gray-100 tw-rounded-md tw-flex tw-items-center tw-justify-center">
            <DimensionPlot plotData={plotData as PlotData} />
          </div>
        </InfoCard>

        <InfoCard title="تصویر" className="tw-col-span-2">
          {loading ? (
            <Skeleton className="tw-h-48 tw-bg-gray-100 tw-rounded-md tw-flex tw-items-center tw-justify-center" />
          ) : (
            <div className="tw-h-48 tw-bg-gray-100 tw-rounded-md tw-flex tw-items-center tw-justify-center">
              Image Place Holder
            </div>
          )}
        </InfoCard>
      </div>
    </div>
  );
};

export default ScanState;
