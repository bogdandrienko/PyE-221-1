import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import axios from "axios";

function App() {
  let val1 = 12;
  let [val2, setVal2] = useState(12);
  function Inrease() {
    val1 += 1;
    console.log(val1);
  }
  function Inrease2() {
    setVal2(val2 + 1);
  }

  useEffect(() => {
    console.log(val2);
  }, [val2]);

  function Decrease2() {
    setVal2(val2 - 1);
    console.log(val2);
  }

  let data1 = [1, 2, 3];
  let [data2, setData2] = useState([]);

  async function GetData() {
    let response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos"
    );
    console.log(response);
    // @ts-ignore
    setData2(response.data);
  }

  return (
    <div className="App">
      <div>
        {val1}
        <button onClick={Inrease}>increase</button>
      </div>

      <div>
        {val2}
        <button onClick={Inrease2}>increase2</button>
      </div>

      <header className="App-header">
        <div onClick={GetData} className={""}>
          GetData
        </div>
        <div>
          {
            // @ts-ignore
            data2.map((item, index: number) => (
              <div key={index}>
                {
                  // @ts-ignore
                  index
                }{" "}
                {
                  // @ts-ignore
                  item.title
                }
              </div>
            ))
          }
        </div>

        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
