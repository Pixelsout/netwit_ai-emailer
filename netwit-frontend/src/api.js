import axios from "axios";

export const uploadCSV = (formData) =>
  axios.post("http://localhost:8000/upload/", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

export const getPreview = (email) =>
  axios.get(`http://localhost:8000/preview/${email}`);

export const getAnalytics = () =>
  axios.get("http://localhost:8000/analytics/");
