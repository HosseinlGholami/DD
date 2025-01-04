// src/index.js
import React from "react";
import { createRoot } from "react-dom/client";
import "./tailwind.css";
import App from "./App";

const root = document.getElementById("root");
const reactRoot = createRoot(root);
reactRoot.render(<App />);
