import {createBrowserRouter} from "react-router";
import Root from "./root.tsx"
import Home from "./home.tsx"
import About from "./about.tsx"

const router = createBrowserRouter([
    {
        path: "/",
        Component: Root,
        children: [
            {index: true, Component: Home},
            {path: "about", Component: About},
        ],
    },
]);

export default router;