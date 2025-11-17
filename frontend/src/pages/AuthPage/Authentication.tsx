import { Outlet } from "react-router-dom";

const Authentication : React.FC = () => {
    return(
        <div>
            <h2>Welcome to Authentication</h2>
            <Outlet />
        </div>
    )
}

export default Authentication;

