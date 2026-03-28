/*import { useState } from "react";
import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import ResultCard from "../components/ResultCard";
import Loader from "../components/Loader";

function Dashboard(){

const [result,setResult] = useState(null);
const [loading,setLoading] = useState(false);
const [uploadsLeft] = useState(1);

return(

<div>

<Navbar/>

<div className="max-w-4xl mx-auto p-6">

<UploadBox
setResult={setResult}
setLoading={setLoading}
uploadsLeft={uploadsLeft}
/>

{loading && <Loader/>}

{result && <ResultCard data={result}/>}

</div>
</div>

)

}

export default Dashboard */
import { useState } from "react";
import Navbar from "../components/Navbar";
import UploadCard from "../components/UploadBox";
import Loader from "../components/Loader";
import ResultCard from "../components/ResultCard";

function Dashboard() {

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  return (

    <div className="min-h-screen bg-black text-white">

      {/* Navbar */}
      <Navbar />

      {/* HERO SECTION */}

      <section
        className="h-[420px] flex items-center justify-center text-center bg-cover bg-center"
        style={{
          backgroundImage:
            "url('https://images.unsplash.com/photo-1489599849927-2ee91cede3ba')"
        }}
      >

        <div className="bg-black/70 p-10 rounded-xl">

          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            Reel2Movie
          </h1>

          <p className="text-gray-300 max-w-xl">
            Identify the movie behind any reel, short video, screenshot,
            or audio clip using AI-powered media analysis.
          </p>

        </div>

      </section>

      {/* WHAT OUR WEBSITE DOES */}

      <section className="max-w-5xl mx-auto p-10 text-center">

        <h2 className="text-3xl font-bold mb-6">
          What Our Website Does
        </h2>

        <p className="text-gray-400 leading-relaxed">
          Reel2Movie analyzes short media clips such as Instagram reels,
          YouTube shorts, screenshots, or audio clips and identifies
          which movie they belong to. Our AI examines visual frames,
          scene composition, and sound patterns to detect the original film.
        </p>

      </section>

      {/* HOW IT WORKS */}

      <section className="max-w-6xl mx-auto p-10">

        <h2 className="text-3xl font-bold text-center mb-10">
          How It Works
        </h2>

        <div className="grid md:grid-cols-3 gap-8">

          <div className="bg-gray-900 p-6 rounded-xl shadow">

            <h3 className="text-xl font-bold mb-2">
              1. Upload Media
            </h3>

            <p className="text-gray-400">
              Upload a short video, screenshot, audio clip,
              or paste a reel URL.
            </p>

          </div>

          <div className="bg-gray-900 p-6 rounded-xl shadow">

            <h3 className="text-xl font-bold mb-2">
              2. AI Analysis
            </h3>

            <p className="text-gray-400">
              Our AI extracts frames, analyzes audio patterns,
              and studies scene similarities.
            </p>

          </div>

          <div className="bg-gray-900 p-6 rounded-xl shadow">

            <h3 className="text-xl font-bold mb-2">
              3. Movie Detection
            </h3>

            <p className="text-gray-400">
              The system compares the media with a large movie
              database and identifies the film.
            </p>

          </div>

        </div>

      </section>

      {/* UPLOAD SECTION */}

      <section className="max-w-4xl mx-auto p-10">

        <h2 className="text-3xl font-bold text-center mb-6">
          Analyze Your Reel
        </h2>

        <UploadCard
          setLoading={setLoading}
          setResult={setResult}
        />

      </section>

      {/* LOADING */}

      {loading && <Loader />}

      {/* RESULT */}

      {result && (

        <section className="max-w-4xl mx-auto p-10">

          <ResultCard data={result} />

        </section>

      )}

      {/* FOOTER */}

      <footer className="text-center p-6 border-t border-gray-800 mt-10">

        <p className="text-gray-500">
          Reel2Movie © 2026 — AI powered movie identification
        </p>

      </footer>

    </div>

  );

}

export default Dashboard;