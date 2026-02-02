import { useState } from "react";
import { uploadFinancialReport } from "./api";

function App() {
  const [file, setFile] = useState(null);
  const [industry, setIndustry] = useState("Retail");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    setLoading(true);
    setData(null);

    try {
      const res = await uploadFinancialReport(file, industry);
      console.log("Backend response:", res.data);
      setData(res.data);
    } catch (err) {
      console.error(err);
      alert("Frontend → Backend error. Check console.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>SME Financial Health Dashboard</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <select value={industry} onChange={(e) => setIndustry(e.target.value)}>
        <option value="Retail">Retail</option>
        <option value="Manufacturing">Manufacturing</option>
        <option value="Services">Services</option>
      </select>

      <br /><br />

      <button onClick={handleAnalyze}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      <hr />

      <h2>Raw API Response (DEBUG VIEW)</h2>

      <pre
        style={{
          background: "#f4f4f4",
          padding: 15,
          maxHeight: 400,
          overflow: "auto"
        }}
      >
        {data ? JSON.stringify(data, null, 2) : "No data yet"}
      </pre>

      {data && (
        <>
          <hr />
          <h2>Summary</h2>
          <p><b>Total Revenue:</b> {data.business_summary.total_revenue}</p>
          <p><b>Total Expense:</b> {data.business_summary.total_expense}</p>
          <p><b>Profit:</b> {data.business_summary.profit}</p>
          <p><b>Health Score:</b> {data.business_summary.financial_health_score}</p>
          <p><b>Risk Level:</b> {data.risk_overview.risk_level}</p>
          <p><b>Investor Note:</b> {data.investor_note}</p>
        </>
      )}
    </div>
  );
}

export default App;
