import React, { useState } from "react";
import { uploadCSV } from "./api";

function Upload({ onUploadComplete }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);
    const res = await uploadCSV(formData);
    setLoading(false);
    onUploadComplete(res.data.results);
  };

  return (
    <div>
      <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={!file || loading}>
        {loading ? "Uploading..." : "Upload CSV"}
      </button>
    </div>
  );
}

export default Upload;
