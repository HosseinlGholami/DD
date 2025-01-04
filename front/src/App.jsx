import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import {MainLayout} from "./components/Layout";
import {ThemeProvider} from "./theme";

function App() {

  const generateRoutes = () => {
    // Create an array of route objects based on user access permissions
    const routes = [
      // Map additional routes based on user access permissions
      ...(true
        ? [{ path: "/", element: <HomePage /> }]
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
        onNavBackClick={() => {
            console.log('hello');
        }}
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

          {/* <NotifWebSocketComponent /> */}
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
