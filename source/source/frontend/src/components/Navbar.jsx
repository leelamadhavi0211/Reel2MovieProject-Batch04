import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="flex justify-between items-center p-5 bg-black/60 backdrop-blur">

      <h1 className="text-2xl font-bold text-red-600">
        Reel2Movie
      </h1>

      <div className="space-x-4">

        <Link
          to="/login"
          className="px-4 py-2 border border-red-600 rounded hover:bg-red-600 transition"
        >
          Login
        </Link>

        <Link
          to="/signup"
          className="px-4 py-2 bg-red-600 rounded hover:bg-red-700 transition"
        >
          Signup
        </Link>

      </div>

    </nav>
  );
}

export default Navbar;