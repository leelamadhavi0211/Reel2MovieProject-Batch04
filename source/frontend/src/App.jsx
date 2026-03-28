import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import HistoryPage from "./pages/Historypage"; // 1. Import your new page

function App() {
  // Check if user is logged in
  const isAuth = localStorage.getItem("token");

  return (
    <BrowserRouter>
      <Routes>
        {/* Main Page */}
        <Route path="/" element={<Dashboard />} />

        {/* History Page - Only allow if isAuth exists, else send to login */}
        <Route 
          path="/history" 
          element={isAuth ? <HistoryPage /> : <Navigate to="/login" />} 
        />

        {/* Auth Pages - If already logged in, redirect to home */}
        <Route
          path="/login"
          element={isAuth ? <Navigate to="/" /> : <Login />}
        />

        <Route
          path="/signup"
          element={isAuth ? <Navigate to="/" /> : <Signup />}
        />

        {/* Catch ALL unknown routes and redirect to home */}
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;