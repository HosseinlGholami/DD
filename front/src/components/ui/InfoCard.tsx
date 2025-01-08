
import classNames from 'classnames';

import { ReactNode } from 'react';
 export type InfoCardProps = {
    title: string;
    className?: string;
    children?: ReactNode
};

const Title = ({ title }: { title: string }) => {
    return (
        <div className='tw-flex tw-flex-col tw-gap-2'>
            <div
                className={classNames(
                    'tw-text-content-dark tw-font-semibold tw-text-mobile-heading-h5-regular xl:tw-text-desktop-heading-h5-regular',
                )}
            >
                {title}
            </div>
            <div className='tw-bg-content-primary tw-w-[70px] tw-h-[2px] tw-rounded-sm'></div>
        </div>
    );
};


const InfoCard = ({  title, className, children }: InfoCardProps) => {
    return (
        <div
            className={classNames(
                'tw-p-4 tw-pt-3 tw-bg-background-surface-0 tw-rounded-xl tw-flex tw-flex-col tw-gap-3',
                className,
            )}
        >
            <Title title={title} />

            {children}
        </div>
    );
};

export default InfoCard;
