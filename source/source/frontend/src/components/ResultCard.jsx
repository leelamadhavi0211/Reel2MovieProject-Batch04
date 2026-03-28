function ResultCard({data}) {

return(

<div className="bg-gray-900 p-6 rounded-xl shadow-lg mt-10 grid md:grid-cols-2 gap-6">

<img
src={data.poster}
alt="poster"
className="rounded"
/>

<div>

<h2 className="text-2xl font-bold">{data.movie}</h2>

<p className="text-gray-400">Genre: {data.genre}</p>

<div className="mt-4">

<p>Confidence</p>

<div className="w-full bg-gray-700 h-3 rounded">

<div
className="bg-red-600 h-3 rounded"
style={{width:`${data.confidence*100}%`}}
></div>

</div>

</div>

<h3 className="mt-6 font-bold">Video Analysis</h3>

<ul className="text-gray-400">
<li>Resolution: {data.video.resolution}</li>
<li>Duration: {data.video.duration}</li>
<li>Frames: {data.video.frames}</li>
</ul>

<h3 className="mt-4 font-bold">Audio Analysis</h3>

<ul className="text-gray-400">
<li>Language: {data.audio.language}</li>
<li>Music: {data.audio.music}</li>
<li>Clarity: {data.audio.clarity}</li>
</ul>

</div>

</div>

)

}

export default ResultCard;