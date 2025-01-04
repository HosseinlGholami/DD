import { PropsWithChildren, createContext, useCallback, useContext, useState } from 'react';

type Theme = 'dark' | 'light';

const getCurrentTheme = () => {
    const theme = localStorage.getItem('theme');

    if (theme) {
        if (theme === 'light') {
            document.documentElement.classList.remove('tw-dark');
        } else {
            document.documentElement.classList.add('tw-dark');
        }

        return theme as Theme;
    }
    localStorage.setItem('theme', 'light');
    document.documentElement.classList.remove('tw-dark');
    return 'light';
};

type ThemeContextType = {
    theme: Theme;
    changeTheme: (theme: Theme) => void;
    toggleTheme: () => void;
} | null;

const ThemeContext = createContext<ThemeContextType>(null);

export const useTheme = () => {
    const themeContext = useContext(ThemeContext);

    if (!themeContext) {
        throw new Error('useTheme should be used within ThemeProvider');
    }

    return themeContext;
};

export const ThemeProvider = ({ children }: PropsWithChildren) => {
    const [theme, setTheme] = useState<Theme>(getCurrentTheme);

    const changeTheme = useCallback((mode: Theme) => {
        if (mode === 'light') {
            document.documentElement.classList.remove('tw-dark');
            setTheme('light');
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.classList.add('tw-dark');
            setTheme('dark');
            localStorage.setItem('theme', 'dark');
        }
    }, []);

    const toggleTheme = useCallback(() => {
        const theme = document.documentElement.classList;

        if (theme.contains('tw-dark')) {
            changeTheme('light');
        } else {
            changeTheme('dark');
        }
    }, [changeTheme]);

    return (
        <ThemeContext.Provider
            value={{
                theme,
                toggleTheme,
                changeTheme,
            }}
        >
            {children}
        </ThemeContext.Provider>
    );
};
