import { useEffect, useState } from "react";
import axios from "axios";
export function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const resp = await axios.get("http://localhost:5000/events");
      setData(resp.data);
    };

    fetchData();

    const interval = setInterval(() => {
      fetchData();
    }, 15000);

    return () => clearInterval(interval);
  }, []);
  if (!data.length) {
    return <div>Loading...</div>;
  }
  return (
    <div className="max-w-2xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-semibold mb-6 text-center text-gray-800">
        GitHub Webhook Activity
      </h1>
      <div className="space-y-4">
        {data.map((d) => (
          <RenderActions key={d._id["$oid"]} d={d} />
        ))}
      </div>
    </div>
  );
}
function RenderActions({ d }) {
  const { event, author, timestamp, to_branch, from_branch, branch } = d;

  const date = new Date(timestamp).toLocaleString("en-US", {
    dateStyle: "medium",
    timeStyle: "short",
    timeZone: "UTC",
  });

  let message = "";
  let color = "";

  if (event === "MERGE") {
    message = `${author} merged branch ${from_branch} to ${to_branch} on ${date}`;
    color = "bg-green-100 border-green-300 text-green-700";
  } else if (event === "PUSH") {
    message = `${author} pushed to ${branch} on ${date}`;
    color = "bg-blue-100 border-blue-300 text-blue-700";
  } else if (event === "PULL_REQUEST") {
    message = `${author} submitted a pull request from ${from_branch} to ${to_branch} on ${date}`;
    color = "bg-yellow-100 border-yellow-300 text-yellow-800";
  } else {
    message = `Unknown event by ${author} on ${date}`;
    color = "bg-gray-100 border-gray-300 text-gray-700";
  }

  return (
    <div className={`p-4 border rounded-lg shadow-sm ${color}`}>
      {message}
    </div>
  );
}
