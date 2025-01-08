import React from "react";
import QRCodeCard from "../ui/QRCodeCard";
import { ReactComponent as NightIcon } from "../../assets/icons/night.svg";
import { ReactComponent as ProductScanIcon } from "../../assets/icons/scan_product.svg";
import Icon from "../ui/Icon";
// import InputBox from "../ui/Inputbox";
import useStore from "../../store/store";
import { useScanner } from "../../hooks/useScanner";

const ProductScanState: React.FC = () => {
  //   const [serial, setSerial] = React.useState<string>("");

  //   const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  //     const value = e.target.value;
  //     setSerial(value);
  //     if (value.length === 5) {
  //       useStore.setState({ barcode: value, currentState: "StartScan" });
  //     }
  //   };

  // const handleScan = useCallback((barcode: string) => {
  //     console.log(barcode);
  // }, []);

  useScanner((barcode: string) => {
    if (barcode.length >= 5) {
      useStore.setState({ barcode: barcode, currentState: "StartScan" });
    }
  });

  return (
    <div className="tw-p-4 tw-grid tw-grid-rows-[auto,1fr] tw-justify-items-center">
      <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
        <div className="tw-col-span-5" />
        {/* <QRCodeCard qrValue="DARK" text="حالت شب" icon={NightIcon} /> */}
      </div>

      <div className="tw-mt-8 tw-flex tw-flex-col tw-items-center">
        <Icon SvgIcon={ProductScanIcon} height={200} width={200} />
        <div className="tw-text-center tw-text-gray-500 tw-mt-4">
          برای شروع سریال کالا را اسکن کنید
        </div>
      </div>
    </div>
  );
};

export default ProductScanState;
