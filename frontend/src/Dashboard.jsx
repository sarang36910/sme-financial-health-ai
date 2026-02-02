import {
  BarChart, Bar, XAxis, YAxis, Tooltip,
  PieChart, Pie, Cell
} from "recharts";

const COLORS = ["#4CAF50", "#F44336"];

export default function Dashboard({ data }) {
  if (!data || !data.business_summary) {
    return <p>No data available</p>;
  }

  const barData = [
    {
      name: "Revenue",
      value: data.business_summary.total_revenue
    },
    {
      name: "Expense",
      value: data.business_summary.total_expense
    }
  ];

  const pieData = [
    {
      name: "Profit",
      value: data.business_summary.profit
    },
    {
      name: "Expense",
      value: data.business_summary.total_expense
    }
  ];

  return (
    <div style={{ marginTop: 20 }}>
      <h2>📊 Financial Dashboard</h2>

      <h3>
        Health Score: {data.business_summary.financial_health_score}
      </h3>

      <p>
        <b>Risk Level:</b> {data.risk_overview.risk_level}
      </p>

      <BarChart width={400} height={250} data={barData}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="value" fill="#2196F3" />
      </BarChart>

      <PieChart width={400} height={250}>
        <Pie data={pieData} dataKey="value" outerRadius={80}>
          {pieData.map((_, index) => (
            <Cell key={index} fill={COLORS[index]} />
          ))}
        </Pie>
        <Tooltip />
      </PieChart>

      <p style={{ marginTop: 10 }}>
        <b>Investor Note:</b> {data.investor_note}
      </p>
    </div>
  );
}
