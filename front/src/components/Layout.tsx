import { PropsWithChildren } from 'react';

import { DashboardHeader } from './Header';
import {
    BreadCrumbItem,
    Navbar,
    NavbarBackButton,
    NavbarBreadCrumbs,
    NavbarEndActions,
    NavbarStartActions,
    NavbarTitle,
} from './NavBar';
import classNames from 'classnames';

export type MainLayoutProps = {
    className?: string;
    renderHeader?: React.ReactNode;
    renderNavbar?: React.ReactNode;

    renderNavbarStartActions?: React.ReactNode;
    renderNavbarEndActions?: React.ReactNode;
    renderNavbarTitle?: React.ReactNode;

    navTitle?: string;
    navBackButton?: boolean;
    onNavBackClick?: () => void;

    breadCrumbItems?: BreadCrumbItem[];
};

const MainLayout = ({
    children,
    breadCrumbItems,
    navBackButton,
    navTitle,
    renderHeader,
    renderNavbar,
    renderNavbarEndActions,
    renderNavbarStartActions,
    renderNavbarTitle,
    onNavBackClick,
    className,
}: PropsWithChildren<MainLayoutProps>) => {
    return (
        <div className='tw-h-screen tw-bg-background-surface-1 tw-flex tw-flex-col tw-max-w-screen-4xl'>
            {renderHeader || (
                <div className='md:tw-block tw-hidden'>
                    <DashboardHeader />
                </div>
            )}

            {renderNavbar || (
                <Navbar>
                    <NavbarStartActions>
                        {navBackButton && <NavbarBackButton onClick={onNavBackClick} />}
                        {renderNavbarStartActions}
                    </NavbarStartActions>
                    <NavbarTitle>{renderNavbarTitle || navTitle}</NavbarTitle>
                    <NavbarEndActions>
                        {renderNavbarEndActions}
                        <div className='tw-hidden md:tw-block'>
                            {breadCrumbItems && <NavbarBreadCrumbs items={breadCrumbItems} />}
                        </div>
                    </NavbarEndActions>
                </Navbar>
            )}

            <div className={classNames('tw-flex-1', className)}>
                <div className='tw-h-full'>{children}</div>
            </div>
        </div>
    );
};

export { MainLayout };
