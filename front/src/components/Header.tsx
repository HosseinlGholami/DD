import classNames from 'classnames';

import { ReactSVG } from 'react-svg';

import { ReactComponent as RoboticsLogo } from '../assets/icons/robotics_logo.svg';
import Icon from './Icon';

export const DashboardHeader = () => {

    return (
        <div className='tw-bg-background-surface-0 tw-px-5 tw-py-4 md:tw-py-2 md:tw-px-4tw-flex tw-gap-2 tw-items-center tw-border-border-1 tw-border-b'>
                        <Icon SvgIcon={RoboticsLogo} width={250} height={70} />
                            {/* <ReactSVG src='@assets/icons/robotics_logo.svg' /> */}

        </div>
    );
};
