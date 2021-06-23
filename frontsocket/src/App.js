import logo from './logo.svg';
import './App.css';
import React from 'react';
import { w3cwebsocket as W3CWebSocket }  from 'websocket';
import GaugeChart from 'react-gauge-chart';


var socket = new W3CWebSocket('ws://localhost:8000/ws/some_url/')


function App() {

  const [page, setPage] = React.useState({Temperatura: 0.0, Humedad: 0.0});


 


    socket.onopen = () => {
      console.log('WebSocket Client Connected');
    };
    socket.onmessage = function(event){
      var data = JSON.parse(event.data);
      
      setPage(data)
      
      
    };
  

    
    
  return (
    <div className="App">
      <div className="Gauge1">
        <h1>Humedad</h1>
      <GaugeChart
        id="gauge-chart"
        textColor="#333"
        nrOfLevels={3}
        arcsLength={[0.33, 0.33, 0.33]}
        colors={["#5BE12C", "#F5CD19", "#EA4228"]}
        percent={page.Humedad/100}
        arcPadding={0.02}
        text
      />
      </div>

      <div className="Gauge1">
      <h1>Temperatura</h1>
      <GaugeChart
        id="gauge-chart"
        textColor="#333"
        nrOfLevels={3}
        arcsLength={[0.33, 0.33, 0.33]}
        colors={["#5BE12C", "#F5CD19", "#EA4228"]}
        percent={page.Temperatura/100}
        arcPadding={0.02}
        text
      />
      </div>
  
    </div>
  );
}

export default App;
