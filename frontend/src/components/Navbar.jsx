import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Navbar() {
  const { user, logoutUser } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logoutUser();
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">✍️ BlogSpace</Link>
      </div>

      <div className="navbar-links">
        <Link to="/">Home</Link>

        {user ? (
          <>
            <Link to="/create">Write</Link>
            <Link to="/profile">Profile</Link>
            <button onClick={handleLogout} className="btn-logout">
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/signup" className="btn-signup">
              Sign Up
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}