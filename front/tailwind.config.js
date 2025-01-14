/** @type {import("tailwindcss").Config} */
export default {
  darkMode: 'class',
  content: ['./src/**/*.{html,ts,tsx,jsx}'],
  theme: {
      // colors generated by script
      colors: {
          background: {
              surface: {
                  0: 'rgb(var(--color-fc-background-surface-0) / <alpha-value>)',
                  1: 'rgb(var(--color-fc-background-surface-1) / <alpha-value>)',
                  2: 'rgb(var(--color-fc-background-surface-2) / <alpha-value>)',
              },
              primary: 'rgb(var(--color-fc-background-primary) / <alpha-value>)',
              secondary: 'rgb(var(--color-fc-background-secondary) / <alpha-value>)',
              caution: 'rgb(var(--color-fc-background-caution) / <alpha-value>)',
              success: 'rgb(var(--color-fc-background-success) / <alpha-value>)',
              neutral: 'rgb(var(--color-fc-background-neutral) / <alpha-value>)',
              error: 'rgb(var(--color-fc-background-error) / <alpha-value>)',
              scrim: 'rgb(var(--color-fc-background-scrim))',
              snackbar: 'rgb(var(--color-fc-background-snackbar) / <alpha-value>)',
              shadow: 'rgb(var(--color-fc-background-shadow))',
              type: {
                  consignment: 'rgb(var(--color-fc-background-type-consignment) / <alpha-value>)',
                  promotion: 'rgb(var(--color-fc-background-type-promotion) / <alpha-value>)',
                  crossdoc: 'rgb(var(--color-fc-background-type-crossdoc) / <alpha-value>)',
                  single: 'rgb(var(--color-fc-background-type-single) / <alpha-value>)',
                  reject: 'rgb(var(--color-fc-background-type-reject) / <alpha-value>)',
                  critical: 'rgb(var(--color-fc-background-type-critical) / <alpha-value>)',
                  retail: 'rgb(var(--color-fc-background-type-retail) / <alpha-value>)',
                  skipinventory:
                      'rgb(var(--color-fc-background-type-skipinventory) / <alpha-value>)',
                  backtoshelf: 'rgb(var(--color-fc-background-type-backtoshelf) / <alpha-value>)',
              },
          },
          content: {
              light: 'rgb(var(--color-fc-content-light) / <alpha-value>)',
              disabled: 'rgb(var(--color-fc-content-disabled) / <alpha-value>)',
              lowemphasis: 'rgb(var(--color-fc-content-lowemphasis) / <alpha-value>)',
              highemphasis: 'rgb(var(--color-fc-content-highemphasis) / <alpha-value>)',
              dark: 'rgb(var(--color-fc-content-dark) / <alpha-value>)',
              primary: 'rgb(var(--color-fc-content-primary) / <alpha-value>)',
              secondary: 'rgb(var(--color-fc-content-secondary) / <alpha-value>)',
              caution: 'rgb(var(--color-fc-content-caution) / <alpha-value>)',
              success: 'rgb(var(--color-fc-content-success) / <alpha-value>)',
              neutral: 'rgb(var(--color-fc-content-neutral) / <alpha-value>)',
              error: 'rgb(var(--color-fc-content-error) / <alpha-value>)',
              type: {
                  consignment: 'rgb(var(--color-fc-content-type-consignment) / <alpha-value>)',
                  promotion: 'rgb(var(--color-fc-content-type-promotion) / <alpha-value>)',
                  crossdoc: 'rgb(var(--color-fc-content-type-crossdoc) / <alpha-value>)',
                  single: 'rgb(var(--color-fc-content-type-single) / <alpha-value>)',
                  reject: 'rgb(var(--color-fc-content-type-reject) / <alpha-value>)',
                  critical: 'rgb(var(--color-fc-content-type-critical) / <alpha-value>)',
                  retail: 'rgb(var(--color-fc-content-type-retail) / <alpha-value>)',
                  skipinventory:
                      'rgb(var(--color-fc-content-type-skipinventory) / <alpha-value>)',
                  backtoshelf: 'rgb(var(--color-fc-content-type-backtoshelf) / <alpha-value>)',
              },
          },
          border: {
              0: 'rgb(var(--color-fc-border-0) / <alpha-value>)',
              1: 'rgb(var(--color-fc-border-1) / <alpha-value>)',
              2: 'rgb(var(--color-fc-border-2) / <alpha-value>)',
          },
          button: {
              primary: 'rgb(var(--color-fc-button-primary) / <alpha-value>)',
              secondary: 'rgb(var(--color-fc-button-secondary) / <alpha-value>)',
              outline: 'rgb(var(--color-fc-button-outline) / <alpha-value>)',
              error: 'rgb(var(--color-fc-button-error) / <alpha-value>)',
              disabled: 'rgb(var(--color-fc-button-disabled))',
              content: {
                  primary: 'rgb(var(--color-fc-button-content-primary) / <alpha-value>)',
                  secondary: 'rgb(var(--color-fc-button-content-secondary) / <alpha-value>)',
                  outline: 'rgb(var(--color-fc-button-content-outline) / <alpha-value>)',
                  error: 'rgb(var(--color-fc-button-content-error) / <alpha-value>)',
                  disabled: 'rgb(var(--color-fc-button-content-disabled) / <alpha-value>)',
              },
              hover: {
                  primary: 'rgb(var(--color-fc-button-hover-primary) / <alpha-value>)',
                  secondary: 'rgb(var(--color-fc-button-hover-secondary) / <alpha-value>)',
                  outline: 'rgb(var(--color-fc-button-hover-outline))',
                  error: 'rgb(var(--color-fc-button-hover-error))',
              },
              click: {
                  primary: 'rgb(var(--color-fc-button-click-primary) / <alpha-value>)',
                  secondary: 'rgb(var(--color-fc-button-click-secondary) / <alpha-value>)',
                  outline: 'rgb(var(--color-fc-button-click-outline))',
                  error: 'rgb(var(--color-fc-button-click-error))',
              },
          },
          map: {
              midsize: 'rgb(var(--color-fc-map-midsize))',
              highsecurity: 'rgb(var(--color-fc-map-highsecurity))',
              clothing: 'rgb(var(--color-fc-map-clothing))',
              bunchfood: 'rgb(var(--color-fc-map-bunchfood))',
              cleaner: 'rgb(var(--color-fc-map-cleaner))',
              misc: 'rgb(var(--color-fc-map-misc))',
              stationary: 'rgb(var(--color-fc-map-stationary))',
              shoe: 'rgb(var(--color-fc-map-shoe))',
              dryfood: 'rgb(var(--color-fc-map-dryfood))',
              bag: 'rgb(var(--color-fc-map-bag))',
              beauty: 'rgb(var(--color-fc-map-beauty))',
              book: 'rgb(var(--color-fc-map-book))',
              fragile: 'rgb(var(--color-fc-map-fragile))',
              singleconfig: 'rgb(var(--color-fc-map-singleconfig))',
          },
      }, // colors generated by script
      // typography generated by script
      fontSize: {
          'mobile-heading-h1-regular': [
              '28px',
              {
                  fontWeight: 500,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h1-regular-compact': [
              '28px',
              {
                  fontWeight: 500,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h1-black': [
              '28px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h1-extrabold': [
              '28px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h2-regular': [
              '22px',
              {
                  fontWeight: 600,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h2-regular-compact': [
              '22px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h2-black': [
              '22px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h2-extrabold': [
              '22px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h3-regular': [
              '18px',
              {
                  fontWeight: 600,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h3-regular-compact': [
              '18px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h3-black': [
              '18px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h3-extrabold': [
              '18px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h4-regular': [
              '16px',
              {
                  fontWeight: 600,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h4-regular-compact': [
              '16px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h4-black': [
              '16px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h4-extrabold': [
              '16px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h5-regular': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h5-regular-compact': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h5-black': [
              '14px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-heading-h5-extrabold': [
              '14px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-subtitle-regular': [
              '13px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-subtitle-regular-compact': [
              '13px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-subtitle-strong': [
              '13px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-subtitle-strong-compact': [
              '13px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-subtitle-black': [
              '13px',
              {
                  fontWeight: 950,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-subtitle-extrabold': [
              '13px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body1-regular': [
              '12px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body1-regular-compact': [
              '12px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body1-strong': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body1-strong-compact': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body1-black': [
              '12px',
              {
                  fontWeight: 950,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body1-extrabold': [
              '12px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body2-regular': [
              '11px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body2-regular-compact': [
              '11px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body2-strong': [
              '11px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body2-strong-compact': [
              '11px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body2-black': [
              '11px',
              {
                  fontWeight: 950,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-body2-extrabold': [
              '11px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-Caption-regular': [
              '10px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-Caption-regular-compact': [
              '10px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-Caption-strong': [
              '10px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-Caption-strong-compact': [
              '10px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-Caption-black': [
              '10px',
              {
                  fontWeight: 950,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-Caption-extrabold': [
              '10px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-body-unit': [
              '8px',
              {
                  fontWeight: 800,
                  lineHeight: '170%',
                  letterSpacing: -0.1,
              },
          ],
          'mobile-button-large-regular': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-button-large-regular-compact': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-button-large-extrabold': [
              '14px',
              {
                  fontWeight: 800,
                  lineHeight: '170%',
                  letterSpacing: 0,
              },
          ],
          'mobile-button-medium-regular': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-button-medium-regular-compact': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '170%',
                  letterSpacing: 0,
              },
          ],
          'mobile-button-medium-extrabold': [
              '12px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-link-large-regular': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-link-large-light': [
              '14px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-link-large-regular-compact': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-link-large-light-compact': [
              '14px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-link-medium-regular': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-link-medium-light': [
              '12px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'mobile-link-medium-regular-compact': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'mobile-link-medium-light-compact': [
              '12px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h1-regular': [
              '33px',
              {
                  fontWeight: 500,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h1-regular-compact': [
              '33px',
              {
                  fontWeight: 500,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h1-black': [
              '33px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h1-extrabold': [
              '33px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h2-regular': [
              '26px',
              {
                  fontWeight: 500,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h2-regular-compact': [
              '26px',
              {
                  fontWeight: 500,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h2-black': [
              '26px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h2-extrabold': [
              '26px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h3-regular': [
              '21px',
              {
                  fontWeight: 500,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h3-regular-compact': [
              '21px',
              {
                  fontWeight: 500,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h3-black': [
              '21px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h3-extrabold': [
              '21px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h4-regular': [
              '19px',
              {
                  fontWeight: 600,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h4-regular-compact': [
              '19px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h4-black': [
              '19px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h4-extrabold': [
              '19px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h5-regular': [
              '16px',
              {
                  fontWeight: 600,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h5-regular-compact': [
              '16px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h5-black': [
              '16px',
              {
                  fontWeight: 950,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-heading-h5-extrabold': [
              '16px',
              {
                  fontWeight: 800,
                  lineHeight: '210%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-subtitle-regular': [
              '15px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-subtitle-regular-compact': [
              '15px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-subtitle-strong': [
              '15px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-subtitle-strong-compact': [
              '15px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-subtitle-black': [
              '15px',
              {
                  fontWeight: 950,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-subtitle-extrabold': [
              '15px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body1-regular': [
              '14px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body1-regular-compact': [
              '14px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body1-strong': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body1-strong-compact': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body1-black': [
              '14px',
              {
                  fontWeight: 950,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body1-extrabold': [
              '14px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body2-regular': [
              '12px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body2-regular-compact': [
              '12px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body2-strong': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body2-strong-compact': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body2-black': [
              '12px',
              {
                  fontWeight: 950,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-body2-extrabold': [
              '12px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-Caption-regular': [
              '11px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-Caption-regular-compact': [
              '11px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-Caption-strong': [
              '11px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-Caption-strong-compact': [
              '11px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-Caption-black': [
              '11px',
              {
                  fontWeight: 950,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-Caption-extrabold': [
              '11px',
              {
                  fontWeight: 800,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-body-unit': [
              '8px',
              {
                  fontWeight: 800,
                  lineHeight: '170%',
                  letterSpacing: -0.1,
              },
          ],
          'desktop-button-large-regular': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-button-large-regular-compact': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-button-large-extrabold': [
              '14px',
              {
                  fontWeight: 800,
                  lineHeight: '170%',
                  letterSpacing: 0,
              },
          ],
          'desktop-button-medium-regular': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-button-medium-regular-compact': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-button-medium-extrabold': [
              '12px',
              {
                  fontWeight: 800,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-link-large-regular': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-link-large-light': [
              '14px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-link-large-regular-compact': [
              '14px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-link-large-light-compact': [
              '14px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-link-medium-regular': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-link-medium-light': [
              '12px',
              {
                  fontWeight: 400,
                  lineHeight: '215%',
                  letterSpacing: 0,
              },
          ],
          'desktop-link-medium-regular-compact': [
              '12px',
              {
                  fontWeight: 600,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
          'desktop-link-medium-light-compact': [
              '12px',
              {
                  fontWeight: 400,
                  lineHeight: '125%',
                  letterSpacing: 0,
              },
          ],
      }, // typography generated by script
      extend: {
          borderRadius: {
              0: '0',
              sm: '0.2rem', // 2px,
              md: '0.4rem', // 4px,
              lg: '0.6rem', // 6px,
              xl: '0.8rem', // 8px,
              '2xl': '1rem', // 10px,
              '3xl': '1.2rem', // 12px,
              full: '9999px',
          },
          borderWidth: {
              DEFAULT: '1px',
              0: '0',
              2: '2px',
              3: '3px',
              4: '4px',
              6: '6px',
              8: '8px',
          },
          keyframes: {
              blink: {
                  '50%': { background: 'transparent' },
              },
              slideInLeft: {
                  '0%': {
                      transform: 'translateX(-100%)',
                      opacity: 0,
                  },
                  '100%': {
                      transform: 'translateX(0)',
                      opacity: 1,
                  },
              },
          },
          animation: {
              blink: 'blink 1s ease-in-out infinite',
              'blink-1/2': 'blink 1s ease-in-out 500ms infinite',
              'blink-1/4': 'blink 1s ease-in-out 250ms infinite',
              'slide-in-left': 'slideInLeft 0.5s ease-out',
          },
      },
      spacing: {
          0: '0',
          1: '0.4rem',
          2: '0.8rem',
          3: '1.2rem',
          4: '1.6rem',
          5: '2rem',
          6: '2.4rem',
          7: '2.8rem',
          8: '3.2rem',
          9: '3.6rem',
          10: '4rem',
          11: '4.4rem',
          12: '4.8rem',
          14: '5.6rem',
          16: '6.4rem',
          20: '8rem',
          24: '9.6rem',
          28: '11.2rem',
          32: '12.8rem',
          36: '14.4rem',
          40: '16rem',
          44: '17.6rem',
          48: '19.2rem',
          52: '20.8rem',
          56: '22.4rem',
          60: '24rem',
          64: '25.6rem',
          72: '28.8rem',
          80: '32rem',
          96: '38.4rem',
      },
  },
  plugins: [],
  prefix: 'tw-',
};
