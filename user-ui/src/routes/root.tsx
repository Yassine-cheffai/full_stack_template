import {Outlet} from "react-router";
import NavigationBar from "@/components/root/NavigationBar";


const Root = () => (
    <div>
        <NavigationBar/>
        <Outlet/>
    </div>
);

export default Root;