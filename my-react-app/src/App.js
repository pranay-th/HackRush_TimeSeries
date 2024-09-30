import React from 'react';
import PatientRecords from './components/PatientRecords';
import DrugConsumption from './components/DrugConsumption';
import TimeSeriesPlot from './components/TimeSeriesPlot';

function App() {
  return (
    <div className="App">
      <header>
        <h1>Flask and React Data Visualization</h1>
      </header>
      <div className="container">
        <PatientRecords />
        <DrugConsumption />
        <TimeSeriesPlot />
      </div>
    </div>
  );
}

export default App;
