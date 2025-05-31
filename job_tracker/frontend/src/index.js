import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Jobs from "./pages/Jobs/Jobs";
import {CssBaseline, GlobalStyles} from '@mui/material';


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <CssBaseline enableColorScheme />
    <GlobalStyles styles={{ body: { backgroundColor: '#ab7922' } }} />
    <Jobs />
  </React.StrictMode>
);

