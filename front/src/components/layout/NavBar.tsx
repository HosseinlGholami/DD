import classNames from 'classnames';

import React, { PropsWithChildren } from 'react';
import { ReactSVG } from 'react-svg';
// import { Icon } from '@/components/UIKit';


export const Navbar = ({ children }: PropsWithChildren) => {
    return (
        <div className='tw-bg-background-surface-0 tw-px-5 tw-py-3 md:tw-px-8 tw-text-content-dark md:tw-border-b tw-border-border-1 tw-w-full tw-flex tw-gap-4 tw-items-center'>
            {children}
        </div>
    );
};

export const NavbarStartActions = ({ children }: PropsWithChildren) => {
    return <div className='tw-flex tw-items-center tw-justify-start tw-gap-2'>{children}</div>;
};

export const NavbarEndActions = ({ children }: PropsWithChildren) => {
    return <div className='tw-flex tw-items-center tw-justify-end tw-gap-2'>{children}</div>;
};

export const NavbarTitle = ({ children }: PropsWithChildren) => {
    return (
        <div className='tw-flex-1 tw-text-mobile-heading-h5-regular xl:tw-text-desktop-heading-h5-regular'>
            {children}
        </div>
    );
};
type NavbarBackButtonProps = {
    onClick?: () => void;
};

export const NavbarBackButton = ({ onClick }: NavbarBackButtonProps) => {
    return (
        <div>
            <ReactSVG src="@assets/icons/nav_arrow_right.svg" />
        </div>
    );
};

export type BreadCrumbItem = {
    label: string;
    href: string;
    isDisabled?: boolean;
};

type NavbarBreadCrumbsProps = {
    items: BreadCrumbItem[];

    onClick?: (item: BreadCrumbItem) => void;
};

export const NavbarBreadCrumbs = ({ items, onClick }: NavbarBreadCrumbsProps) => {
    return (
        <div className='tw-flex tw-items-center tw-gap-1 tw-line-clamp-1'>
            {items.map((item, index) => {
                return (
                    <React.Fragment key={index}>
                        <div
                            className={classNames(
                                 'tw-text-mobile-body-subtitle-strong xl:tw-text-desktop-body-subtitle-strong tw-text-content-dark',
                                {
                                    'tw-text-content-lowemphasis': index !== items.length - 1,
                                    'tw-text-content-highemphasis': index === items.length - 1,
                                    'tw-opacity-50 !tw-cursor-default': item.isDisabled,
                                    'tw-cursor-pointer': !item.isDisabled,
                                },
                            )}
                             onClick={(e) => {
                                if (onClick) {
                                    e.preventDefault();
                                    onClick(item);
                                }

                                if (item.isDisabled || index === items.length - 1) {
                                    e.preventDefault();
                                }
                            }}
                        >
                            {item.label}
                        </div>

                        {index !== items.length - 1 && (
                            <div
                                className={classNames(
                                     'tw-text-mobile-body-subtitle-regular xl:tw-text-desktop-body-subtitle-regular tw-cursor-pointer tw-text-content-dark',
                                    {
                                        'tw-text-content-lowemphasis': index !== items.length - 1,
                                        'tw-text-content-highemphasis': index !== items.length - 1,
                                    },
                                )}
                            >
                                /
                            </div>
                        )}
                    </React.Fragment>
                );
            })}
        </div>
    );
};
