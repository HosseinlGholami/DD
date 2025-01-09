import React from 'react';
import QRCode from 'react-qr-code';
import Icon from './Icon';

type QRCodeCardProps = {
    qrValue: string; // Value to encode in the QR code
    text: string; // Text to display
    icon: React.FunctionComponent<React.SVGProps<SVGSVGElement>>;
    color?: string; // Optional color for text, icon, and QR code
};

const QRCodeCard = ({ qrValue, text, icon, color = '#000' }: QRCodeCardProps) => {
    return (
        <div
            className="tw-w-48 tw-h-16 tw-bg-background-surface-0 tw-rounded-tl-lg tw-rounded-br-none tw-rounded-tr-none tw-rounded-bl-none tw-flex tw-items-center tw-justify-between tw-p-4"
        >
            <div className="tw-flex tw-items-center tw-gap-2">
                <QRCode 
                    value={qrValue} 
                    size={64} 
                    fgColor={color} // Sets the color of the QR code
                    className="tw-rounded-md" 
                />
                <Icon SvgIcon={icon} width={20} height={20} /> {/* Sets the color of the icon */}
                <span 
                    className="tw-font-semibold tw-text-mobile-body-md xl:tw-text-desktop-body-md"
                    style={{ color: color }} // Sets the color of the text
                >
                    {text}
                </span>
            </div>
        </div>
    );
};

export default QRCodeCard;