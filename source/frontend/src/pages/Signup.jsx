import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../services/api";

function Signup() {

  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSignup = async () => {

    try {

      const res = await API.post("/signup", form);

      alert(res.data.message);

      navigate("/login");

    } catch (err) {

      alert(err.response?.data?.detail || "Signup failed");

    }

  };

  return (

    <div className="flex justify-center items-center h-screen">

      <div className="bg-gray-900 p-8 rounded-xl w-80">

        <h2 className="text-2xl mb-4 text-center">Signup</h2>

        <input
          name="name"
          placeholder="Name"
          onChange={handleChange}
          className="w-full p-2 mb-3 bg-gray-800 rounded"
        />

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
          onClick={handleSignup}
          className="w-full bg-red-600 py-2 rounded hover:bg-red-700"
        >
          Create Account
        </button>

        <Link to="/" className="block text-center mt-4 text-gray-400">
          ← Back
        </Link>

      </div>

    </div>

  );

}

export default Signup;