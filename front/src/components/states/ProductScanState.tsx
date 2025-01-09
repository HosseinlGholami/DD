import React from "react";
import QRCodeCard from "../ui/QRCodeCard";
import { ReactComponent as NoneIcon } from "../../assets/icons/none.svg";
import { ReactComponent as ProductScanIcon } from "../../assets/icons/scan_product.svg";
import Icon from "../ui/Icon";
// import InputBox from "../ui/Inputbox";
import useStore from "../../store/store";
import { useScanner } from "../../hooks/useScanner";
import { zerotare } from "../../network/localApi";

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

  useScanner( async (barcode: string) => {
    if (barcode.length >= 5) {
      useStore.setState({ barcode: barcode, currentState: "StartScan" });
    } else if (barcode === "ZERO") {
      if (await zerotare()) {
        console.log("Zero.")
      } else {
        console.log("NZero")
      }
    }
  });

  return (
    <div className="tw-p-4 tw-grid tw-grid-rows-[auto,1fr] tw-justify-items-center">
      <div className="tw-grid tw-grid-cols-5 tw-gap-4 tw-justify-items-start">
        <div className="tw-col-span-4" />
        <QRCodeCard qrValue="ZERO" text="صفر کردن ترازو" icon={NoneIcon} color="#DE3730" />
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
