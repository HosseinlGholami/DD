import classnames from 'classnames';

// import styles from './loading.module.scss';

interface Props {
    isFullScreen?: boolean;
    color?: 'white' | 'low-emphasis';
    className?: string;
}

function Loading({ className, isFullScreen, color = 'low-emphasis' }: Props) {
    const componentClassName = classnames(
        'd-flex ai-center jc-center',
        {
            'w-100 h-100': isFullScreen,
        },
        className,
        color,
    );
    const itemClassName = classnames(
        'rounded-circle',
        'tw-bg-content-lowemphasis',
    );

    return (
        <div className={componentClassName}>
            <div className={itemClassName} />
            <div className={itemClassName} />
            <div className={itemClassName} />
        </div>
    );
}

export { Loading };
