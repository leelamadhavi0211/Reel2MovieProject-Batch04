import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../services/api";


function Login() {

  const navigate = useNavigate();

  const [form, setForm] = useState({
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleLogin = async () => {

    try {

      const res = await API.post("/login", form);

      // store JWT token
      localStorage.setItem("token", res.data.token);

      localStorage.setItem("name", res.data.name);
      localStorage.setItem("email", res.data.email);

      alert("Login successful");

      navigate("/");

    } catch (err) {

      alert(err.response?.data?.detail || "Login failed");

    }

  };

  return (

    <div className="flex justify-center items-center h-screen">

      <div className="bg-gray-900 p-8 rounded-xl w-80">

        <h2 className="text-2xl mb-4 text-center">Login</h2>

        <input
          name="email"
          placeholder="Email"
          onChange={handleChange}
          className="w-full p-2 mb-3 bg-gray-800 rounded"
        />

        <input
          name="password"
          type="password"
          placeholder="Password"
          onChange={handleChange}
          className="w-full p-2 mb-3 bg-gray-800 rounded"
        />

        <button
          onClick={handleLogin}
          className="w-full bg-red-600 py-2 rounded hover:bg-red-700"
        >
          Login
        </button>

        <Link to="/" className="block text-center mt-4 text-gray-400">
          ← Back
        </Link>

      </div>

    </div>

  );

}

export default Login;