import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MainPage from "./pages/MainPage";
import { MainLayout } from "./components/layout/Layout";
import { ThemeProvider } from "./theme";

function App() {

  const generateRoutes = () => {
    // Create an array of route objects based on user access permissions
    const routes = [
      // Map additional routes based on user access permissions
      ...(true
        ? [{ path: "/", element: <MainPage /> }]
        : []),
    ];

    return routes.map((route, index) => (
      <Route key={index} path={route.path} element={route.element} />
    ));
  };


  return (
    <Router>
      <ThemeProvider>
        <div dir='rtl'>
          <MainLayout
            navTitle='دستگاه اندازه‌گیری'
            navBackButton
            onNavBackClick={() => {}}
            breadCrumbItems={[
              {
                label: 'خانه',
                href: '/',
              },
              {
                label: 'اندازه‌گیری',
                href: '/',
              },
            ]}
          >
            <div>
              <Routes>{generateRoutes()}</Routes>
            </div>
          </MainLayout>
        </div>
      </ThemeProvider>
    </Router>
  );
}

export default App;
