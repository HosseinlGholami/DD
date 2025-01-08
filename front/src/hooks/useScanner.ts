import { useCallback, useEffect, } from "react";

type ListenerType = (event: KeyboardEvent) => void;

// this hook will get an input ref and add a keydown listener to it in order to capture the barcode
export const useScanner = (callback: (barcode: string) => void) => {
    const addListener = useCallback(() => {
        let scannedBarcode = "";
        let barcodeFirstCharacter = "";
        let lastKeyPressTime = 0;
        const typingDelay = 50;

        // gun scan
        const handleKeyDown = (event: KeyboardEvent) => {
            const currentTime = new Date().getTime();
            const timeSinceLastKeyPress = currentTime - lastKeyPressTime;

            if (timeSinceLastKeyPress < typingDelay) {
                if (event.key === "Enter") {
                    callback(barcodeFirstCharacter + scannedBarcode)
                    scannedBarcode = "";
                    barcodeFirstCharacter = "";
                    return;
                }

                if (event.key !== "Shift" && event.key !== "Unidentified")
                    scannedBarcode += event.key;
            } else {
                barcodeFirstCharacter = event.key !== "Shift" ? event.key : "";
                scannedBarcode = "";
            }

            lastKeyPressTime = currentTime;
        };

        window.addEventListener("keydown", handleKeyDown);

        return {
            handleKeyDown,
        };
    }, [callback]);

    const removeListener = useCallback(
        (listener: ListenerType) => {

            window.removeEventListener("keydown", listener);
        },
        []
    );

    useEffect(() => {
        const listeners = addListener();

        return () => {
            if (listeners?.handleKeyDown) removeListener(listeners?.handleKeyDown);
        };
    }, [addListener, removeListener]);
};

// const handleScan = useCallback((barcode: string) => {
//     console.log(barcode);
// })

// useScanner(handleScan);