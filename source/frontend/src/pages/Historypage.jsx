import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function HistoryPage() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch("http://127.0.0.1:8000/history", {
          headers: { "Authorization": `Bearer ${token}` }
        });

        const data = await response.json();

        // If backend sent an error object instead of an array
        if (!response.ok) {
          throw new Error(data.detail || "Failed to fetch history");
        }

        setHistory(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, []);

  if (loading) return <div className="p-20 text-center text-white">Loading your cinema history...</div>;
  
  if (error) return (
    <div className="p-20 text-center text-red-500">
      <p>⚠️ Error: {error}</p>
      <Link to="/" className="text-blue-400 underline mt-4 block">Go back to Dashboard</Link>
    </div>
  );

  return (
    <div className="bg-black min-h-screen p-6 text-white">
      <div className="max-w-5xl mx-auto">
        <div className="flex justify-between items-center mb-10">
          <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-red-400">
            Search History
          </h1>
          <Link to="/" className="text-sm bg-gray-800 px-4 py-2 rounded-lg hover:bg-gray-700">
            + New Search
          </Link>
        </div>

        {history.length === 0 ? (
          <div className="text-center py-20 bg-gray-900 rounded-2xl border border-dashed border-gray-700">
            <p className="text-gray-500 text-xl">You haven't identified any movies yet!</p>
          </div>
        ) : (
          <div className="grid gap-6">
            {history.map((item,index) => (
              <div key={item._id || index} className="bg-gray-900 rounded-xl overflow-hidden flex flex-col md:flex-row border border-gray-800 hover:border-red-500 transition-all group">
                {/* Poster Section */}
                <div className="md:w-40 w-full h-56 md:h-auto overflow-hidden">
                  <img 
                    src={item.poster || "https://via.placeholder.com/300x450?text=No+Poster"} 
                    alt="movie" 
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform"
                  />
                </div>
                {/* Inside your map function */}
<h3 className="text-xl font-bold">
  {item.movie_name || item.movie || "Unknown Movie"}
</h3>
                {/* Info Section */}
                <div className="p-6 flex-grow">
                  <div className="flex justify-between items-start mb-2">
                    <h2 className="text-2xl font-bold">{item.movie || item.title}</h2>
                    <span className="text-green-500 font-bold bg-green-500/10 px-2 py-1 rounded text-sm">
                      {Math.round((item.confidence || 0) * 100)}% Match
                    </span>
                  </div>
                  
                  <p className="text-red-500 text-sm mb-3">
                    {item.genres?.length > 0 ? item.genres.join(" / ") : "Movie Identification"}
                  </p>

                  <p className="text-gray-400 text-sm line-clamp-3 mb-4">
                    {item.overview || "No overview available for this result."}
                  </p>

                  <div className="flex items-center justify-between text-xs text-gray-500 mt-auto border-t border-gray-800 pt-4">
                    <p>Analyzed on: {item.created_at || "N/A"}</p>
                    <button 
                      onClick={() => window.open(`https://www.youtube.com/results?search_query=${item.movie}+trailer`, '_blank')}
                      className="text-white hover:text-red-500 transition"
                    >
                      Watch Trailer →
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default HistoryPage;