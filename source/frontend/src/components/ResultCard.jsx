function ResultCard({ data }) {
  return (
    <div className="bg-gray-900 p-6 rounded-xl shadow-lg mt-10 grid md:grid-cols-2 gap-6 text-white">
      {/* Poster */}
      <div className="flex justify-center">
        <img
          src={data?.poster || "https://via.placeholder.com/500x750?text=No+Poster"}
          alt="poster"
          className="rounded shadow-2xl max-h-[500px] object-cover"
        />
      </div>

      <div>
        {/* Movie Info */}
        <h2 className="text-3xl font-bold mb-2">
          {data?.title || data?.movie || "Unknown Movie"}
        </h2>
        
        <p className="text-gray-400 mb-1">
          {/* Note: changed .genre to .genres.join() since it is a list */}
          Genre: {data?.genres?.length > 0 ? data.genres.join(", ") : "N/A"}
        </p>
        
        <p className="text-gray-400 mb-4 italic">
          Released: {data?.release_date || "Unknown"}
        </p>

        {/* Overview / Description */}
        <div className="mb-6">
          <h3 className="font-bold text-red-500 mb-1">Overview</h3>
          <p className="text-sm text-gray-300 leading-relaxed">
            {data?.overview || "No description available for this movie."}
          </p>
        </div>

        {/* Confidence Bar */}
        <div className="mt-4">
          <div className="flex justify-between mb-1">
            <p>AI Confidence</p>
            <p>{Math.round((data?.confidence || 0) * 100)}%</p>
          </div>
          <div className="w-full bg-gray-700 h-3 rounded">
            <div
              className="bg-red-600 h-3 rounded transition-all duration-500"
              style={{ width: `${(data?.confidence || 0) * 100}%` }}
            ></div>
          </div>
        </div>

        {/* Video Analysis */}
        <div className="grid grid-cols-2 gap-4 mt-8">
          <div>
            <h3 className="font-bold border-b border-gray-700 mb-2 pb-1 text-sm">Video Details</h3>
            <ul className="text-xs text-gray-400 space-y-1">
              <li>Resolution: {data?.video?.resolution || "N/A"}</li>
              <li>Duration: {data?.video?.duration || "N/A"}</li>
              <li>Frames: {data?.video?.frames || "N/A"}</li>
            </ul>
          </div>

          <div>
            <h3 className="font-bold border-b border-gray-700 mb-2 pb-1 text-sm">Audio Details</h3>
            <ul className="text-xs text-gray-400 space-y-1">
              <li>Language: {data?.audio?.language || "N/A"}</li>
              <li>Rating: {data?.vote_average || "N/A"}/10</li>
              <li>Clarity: {data?.audio?.clarity || "N/A"}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ResultCard;