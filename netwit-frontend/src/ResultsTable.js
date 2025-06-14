import React from "react";

function ResultsTable({ results, onPreview }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Email</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {results.map((r, i) => (
          <tr key={i}>
            <td>{r.email}</td>
            <td>{r.status}</td>
            <td>
              <button onClick={() => onPreview(r.email)}>Preview</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ResultsTable;
