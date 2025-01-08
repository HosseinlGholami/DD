import classNames from 'classnames';

const Skeleton = ({ className }: { className?: string }) => {
    return (
        <div
            role='status'
            className={classNames(
                'tw-animate-pulse tw-overflow-hidden tw-min-w-6 tw-min-h-[24px] tw-rounded-md',
                className,
            )}
        >
            <div className={'tw-bg-background-surface-1 tw-w-full tw-min-h-[24px] tw-h-full'} />
        </div>
    );
};

export default Skeleton;
