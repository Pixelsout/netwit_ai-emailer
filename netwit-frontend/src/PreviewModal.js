import React from "react";

function PreviewModal({ content, onClose }) {
  if (!content) return null;
  return (
    <div style={{ background: "#fff", border: "1px solid #ccc", padding: "20px" }}>
      <button onClick={onClose}>Close</button>
      <div dangerouslySetInnerHTML={{ __html: content }} />
    </div>
  );
}

export default PreviewModal;
