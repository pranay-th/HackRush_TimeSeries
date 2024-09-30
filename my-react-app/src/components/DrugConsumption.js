import React, { useState, useEffect } from 'react';

const DrugConsumption = () => {
  const [consumption, setConsumption] = useState([]);

  useEffect(() => {
    fetch('/api/drug_consumption')
      .then((response) => response.json())
      .then((data) => setConsumption(data))
      .catch((error) => console.error('Error fetching drug consumption data:', error));
  }, []);

  return (
    <div className="data-section">
      <h2>Drug Consumption</h2>
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
          {consumption.map((item, index) => (
            <tr key={index}>
              <td>{new Date(item.date).toLocaleDateString()}</td>
              <td>{new Date(item.time).toLocaleTimeString()}</td>
              <td>{item.disease}</td>
              <td>{item.region}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DrugConsumption;
