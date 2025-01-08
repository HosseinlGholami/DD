import React from "react";
import QRCodeCard from "../ui/QRCodeCard";
import Icon from "../ui/Icon";
import { ReactComponent as PlayIcon } from "../../assets/icons/play.svg";
import { ReactComponent as StopIcon } from "../../assets/icons/stop.svg";
import { ReactComponent as NightIcon } from "../../assets/icons/night.svg";
import { ReactComponent as ScanToStartIcon } from "../../assets/icons/scan_to_start.svg";
// import InputBox from "../ui/Inputbox";
import useStore from "../../store/store";
import { startScan } from "../../network/localApi";
import { useScanner } from "../../hooks/useScanner";

const MainPage: React.FC = () => {
  //   const [command, setCommand] = React.useState<string>("");

  // const handleInputChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
  //     const value = e.target.value;
  //     setCommand(value);
  //     if (value === "HOK") {
  //         const barcode = useStore.getState().barcode;
  //         if (await startScan(barcode)) {
  //             useStore.setState({ currentState: 'Scan' });

  //         }
  //         else {
  //             // TODO: show toast
  //             console.error('Failed to start scan');
  //             useStore.setState({ currentState: 'Scan' });
  //         }

  //     } else if (value === "NOK") {
  //         useStore.setState({ currentState: 'ProductScan' });
  //     }
  // };

  useScanner(async (barcode: string) => {
    if (barcode === "HOK") {
      const barcode = useStore.getState().barcode;
      if (await startScan(barcode)) {
        useStore.setState({ currentState: "Scan" });
      } else {
        // TODO: show toast
        console.error("Failed to start scan");
        useStore.setState({ currentState: "Scan" });
      }
    } else if (barcode === "NOK") {
      useStore.setState({ currentState: "ProductScan" });
    }
  });

  return (
    <div className="tw-p-4 tw-grid tw-grid-rows-[auto,1fr]">
      <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
        <QRCodeCard qrValue="HOK" text="شروع اسکن" icon={PlayIcon} />
        <QRCodeCard qrValue="NOK" text="پاک کردن" icon={StopIcon} />
        <div className="tw-col-span-2" />

        <QRCodeCard qrValue="DARK" text="حالت شب" icon={NightIcon} />
      </div>

      <div className="tw-mt-8 tw-flex tw-flex-col tw-items-center">
        <Icon SvgIcon={ScanToStartIcon} height={200} width={200} />
        <div className="tw-text-center tw-text-gray-500 tw-mt-4">
          برای شروع QR Code را اسکن کنید
        </div>
      </div>
    </div>
  );
};

export default MainPage;
