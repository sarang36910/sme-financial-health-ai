import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export const uploadFinancialReport = async (file, industry) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(
    `${API_BASE}/financial-report/?industry=${industry}`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    }
  );
};
