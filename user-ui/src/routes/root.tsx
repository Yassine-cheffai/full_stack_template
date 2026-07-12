import {Link, Outlet} from "react-router";

const Root = () => (
    <div>
        <nav>
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
        </nav>
        <Outlet/>
    </div>
);

export default Root;