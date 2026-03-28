import { Link } from "react-router-dom";

function Signup(){

return(

<div className="flex justify-center items-center h-screen">

<div className="bg-gray-900 p-8 rounded-xl w-80">

<h2 className="text-2xl mb-4 text-center">Signup</h2>

<input
type="text"
placeholder="Name"
className="w-full p-2 mb-3 bg-gray-800 rounded"
/>

<input
type="email"
placeholder="Email"
className="w-full p-2 mb-3 bg-gray-800 rounded"
/>

<input
type="password"
placeholder="Password"
className="w-full p-2 mb-3 bg-gray-800 rounded"
/>

<button className="w-full bg-red-600 py-2 rounded hover:bg-red-700">
Create Account
</button>

<Link to="/" className="block text-center mt-4 text-gray-400">
← Back
</Link>

</div>

</div>

)

}

export default Signup