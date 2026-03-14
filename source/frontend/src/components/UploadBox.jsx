import { useState } from "react";
import axios from "axios";

function UploadCard({ setResult, setLoading }) {

  const [mode, setMode] = useState("file");
  const [file, setFile] = useState(null);
  const [url, setUrl] = useState("");

  const handleUpload = async () => {

    if (mode === "file" && !file) {
      alert("Please select a file");
      return;
    }

    if (mode === "url" && url === "") {
      alert("Please paste a URL");
      return;
    }

    setLoading(true);

    try {

      let response;

      if (mode === "file") {

        const formData = new FormData();
        formData.append("media", file);

        response = await axios.post(
          "http://localhost:5000/upload-file",
          formData
        );

      } else {

        response = await axios.post(
          "http://localhost:5000/upload-url",
          { url }
        );

      }

      setResult(response.data);

    } catch (error) {

      console.log(error);

      // temporary mock response (until backend exists)

      setTimeout(() => {

        setResult({
          movie: "Inception",
          genre: "Sci-Fi",
          confidence: 0.91,
          poster:
            "https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg",
          video: {
            resolution: "1080p",
            duration: "8s",
            frames: "240"
          },
          audio: {
            language: "English",
            music: "Detected",
            clarity: "High"
          }
        });

        setLoading(false);

      }, 1500);

      return;
    }

    setLoading(false);

  };

  return (

    <div className="bg-gray-900 p-8 rounded-xl shadow-lg max-w-xl mx-auto mt-10">

      <h2 className="text-xl font-bold text-center mb-6">
        Upload Media
      </h2>

      {/* Mode Toggle */}

      <div className="flex justify-center gap-4 mb-6">

        <button
          onClick={() => setMode("file")}
          className={`px-4 py-2 rounded ${
            mode === "file" ? "bg-red-600" : "bg-gray-700"
          }`}
        >
          Upload File
        </button>

        <button
          onClick={() => setMode("url")}
          className={`px-4 py-2 rounded ${
            mode === "url" ? "bg-red-600" : "bg-gray-700"
          }`}
        >
          Paste URL
        </button>

      </div>

      {/* File Upload */}

      {mode === "file" && (

        <input
          type="file"
          accept="video/*,audio/*,image/*"
          onChange={(e) => setFile(e.target.files[0])}
          className="w-full mb-4"
        />

      )}

      {/* URL Upload */}

      {mode === "url" && (

        <input
          type="text"
          placeholder="Paste Instagram / YouTube short URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          className="w-full p-2 mb-4 rounded bg-gray-800 border border-gray-700"
        />

      )}

      <button
        onClick={handleUpload}
        className="w-full bg-red-600 py-2 rounded hover:bg-red-700 transition"
      >
        Analyze Media
      </button>

    </div>

  );

}

export default UploadCard;