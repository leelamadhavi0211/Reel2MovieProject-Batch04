import { Link, useNavigate } from "react-router-dom";

function Navbar() {

  const navigate = useNavigate();

  const token = localStorage.getItem("token");
  const name = localStorage.getItem("name");
  const email = localStorage.getItem("email");

  const handleLogout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (

    <div className="flex justify-between items-center p-4 bg-black">

      {/* Logo */}
      <h1 className="text-xl font-bold text-red-600">
        Reel2Movie
      </h1>

      {/* Right Side */}
      <div className="flex items-center gap-4">

        {!token ? (
          <>
            <Link to="/login" className="hover:text-red-500">
              Login
            </Link>

            <Link to="/signup" className="hover:text-red-500">
              Signup
            </Link>

          
          </>
        ) : (
          <>
            {/* User Info */}
            <div className="text-right">

              <p className="text-sm text-white font-semibold">
                Welcome, {name}
              </p>

              <p className="text-xs text-gray-400">
                {email}
              </p>

            </div>

            {/* Profile Circle */}
            <div className="bg-red-600 w-8 h-8 rounded-full flex items-center justify-center font-bold">
              {name?.charAt(0).toUpperCase()}
            </div>
            <Link to="/history"  className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg transition" >
              📜 View My History
             </Link>
            {/* Logout */}
            <button
              onClick={handleLogout}
              className="bg-red-600 px-4 py-1 rounded hover:bg-red-700"
            >
              Logout
            </button>
          </>
        )}

      </div>

    </div>

  );

}

export default Navbar;