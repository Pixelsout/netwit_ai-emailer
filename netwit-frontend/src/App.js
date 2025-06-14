import React, { useState } from "react";
import Upload from "./Upload";
import ResultsTable from "./ResultsTable";
import PreviewModal from "./PreviewModal";
import Dashboard from "./Dashboard";
import { getPreview } from "./api";
import "./App.css";

function App() {
  const [results, setResults] = useState([]);
  const [previewContent, setPreviewContent] = useState(null);

  const handlePreview = async (email) => {
    const res = await getPreview(email);
    setPreviewContent(res.data);
  };

  return (
    <div className="App" style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>📬 NetWit AI Email Dashboard</h1>
      <Upload onUploadComplete={setResults} />
      <hr />
      <Dashboard />
      <hr />
      <ResultsTable results={results} onPreview={handlePreview} />
      <PreviewModal content={previewContent} onClose={() => setPreviewContent(null)} />
    </div>
  );
}

export default App;
