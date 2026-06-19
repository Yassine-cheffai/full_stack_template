import {StrictMode} from 'react'
import {createRoot} from 'react-dom/client'
import {createTheme, ThemeProvider} from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import './index.css'
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import {RouterProvider} from "react-router";
import router from "./routes/routes.ts"

const darkTheme = createTheme({
    palette: {
        mode: 'dark',
        primary: {
            main: '#759e4a',
        },
    },
});

createRoot(document.getElementById('root')!).render(
    <StrictMode>
        <ThemeProvider theme={darkTheme}>
            <CssBaseline/>
            <RouterProvider router={router}/>
        </ThemeProvider>
    </StrictMode>,
)