import React, { useState, useEffect } from 'react';

const PatientRecords = () => {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    fetch('/api/patient_records')
      .then((response) => response.json())
      .then((data) => setRecords(data))
      .catch((error) => console.error('Error fetching patient records:', error));
  }, []);

  return (
    <div className="data-section">
      <h2>Patient Records</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Time</th>
            <th>Disease</th>
            <th>Region</th>
          </tr>
        </thead>
        <tbody>
          {records.map((record, index) => (
            <tr key={index}>
              <td>{new Date(record.date).toLocaleDateString()}</td>
              <td>{new Date(record.time).toLocaleTimeString()}</td>
              <td>{record.disease}</td>
              <td>{record.region}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PatientRecords;
