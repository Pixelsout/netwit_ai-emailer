import React, { useEffect, useState } from "react";
import { Doughnut } from "react-chartjs-2";
import { getAnalytics } from "./api";

// ✅ Register Chart.js modules
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function Dashboard() {
  const [data, setData] = useState({ sent: 0, failed: 0, opened: 0, clicked: 0 });

  useEffect(() => {
    getAnalytics().then((res) => setData(res.data));
  }, []);

  const chartData = {
    labels: ["Sent", "Failed", "Opened", "Clicked"],
    datasets: [
      {
        label: "Email Stats",
        data: [data.sent, data.failed, data.opened, data.clicked],
        backgroundColor: ["#4caf50", "#f44336", "#2196f3", "#ff9800"],
        borderWidth: 1,
      },
    ],
  };

  return (
    <div style={{ maxWidth: "400px", margin: "0 auto", textAlign: "center" }}>
      <h3>📊 Email Analytics</h3>
      <Doughnut data={chartData} />
    </div>
  );
}

export default Dashboard;
