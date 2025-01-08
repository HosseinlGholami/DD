import React from 'react';

interface IconProps {
  SvgIcon: React.FunctionComponent<React.SVGProps<SVGSVGElement>>;
  color?: string;
  width?: number | string;
  height?: number | string;
}

const Icon: React.FC<IconProps> = ({
  SvgIcon,
  color = 'currentColor',
  width = 24,
  height = 24
}) => (
  <SvgIcon
    width={width}
    height={height}
    fill={color}
    aria-hidden="true"
  />
);

export default Icon;