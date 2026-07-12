import {Outlet} from "react-router";
import NavigationBar from "../components/root/NavigationBar.tsx";


const Root = () => (
    <div>
        <NavigationBar/>
        <Outlet/>
    </div>
);

export default Root;