import React from "react";
import logo from "./logo.svg";
import { Counter } from "./features/counter/Counter";
import "./App.css";
import axios from "axios";

// axios.defaults.baseURL = "http://192.168.0.101:8000";

// js - javascript
// ts - typescript
// jsx - react
// tsx - typescript + react

function App1() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Counter />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <span>
          <span>Learn </span>
          <a
            className="App-link"
            href="https://reactjs.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            React
          </a>
          <span>, </span>
          <a
            className="App-link"
            href="https://redux.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Redux
          </a>
          <span>, </span>
          <a
            className="App-link"
            href="https://redux-toolkit.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Redux Toolkit
          </a>
          ,<span> and </span>
          <a
            className="App-link"
            href="https://react-redux.js.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            React Redux
          </a>
        </span>
      </header>
    </div>
  );
}

// CRUD

function App() {
  // логика

  const string1 = "";
  const string2 = "";
  let string3 = "Python";

  const dict1 = { name: "Bogdan", age: 25, adult: undefined };

  const arr1 = [1, 2, 3, 4, 5];

  const arr2 = [
    { title: "Title 1", description: "Description 1", time_to_read: 1 },
    { title: "Title 2", description: "Description 2", time_to_read: 2 },
    { title: "Title 3", description: "Description 3", time_to_read: 3 },
    { title: "Title 4", description: "Description 4", time_to_read: 4 },
  ];

  console.log(arr1);
  console.log("Шолпан");

  // @ts-ignore

  function HelloWorld(message: String) {
    console.log(message);
  }

  const HelloWorld2 = (message: String) => {
    console.log(message);
  };

  let var2 = 20;

  HelloWorld(`Bogdan ${var2}`);
  HelloWorld2(`Bogdan ${var2}`);

  // alert("Опасность!")
  // prompt("введите", "12")

  // setTimeout(()=>)

  // логика

  // дизайн
  return (
    <div>
      <h1 className="">Hello world!</h1>
      <div className="text-danger top-border">danger</div>
      <main>
        <section className="py-5 text-center container">
          <div className="row py-lg-5">
            <div className="col-lg-6 col-md-8 mx-auto">
              <h1 className="fw-light">Album example</h1>
              <p className="lead text-muted">
                Something short and leading about the collection below—its
                contents, the creator, etc. Make it short and sweet, but not too
                short so folks don’t simply skip over it entirely.
              </p>
              <p>
                <a href="#" className="btn btn-primary my-2">
                  Main call to action
                </a>
                <a href="#" className="btn btn-secondary my-2">
                  Secondary action
                </a>
              </p>
            </div>
          </div>
        </section>

        <div className="album py-5 bg-light">
          <div className="container">
            <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
              {arr2.map((item, index) => (
                <div className="col">
                  <div className="card shadow-sm">
                    <svg
                      className="bd-placeholder-img card-img-top"
                      width="100%"
                      height="225"
                      xmlns="http://www.w3.org/2000/svg"
                      role="img"
                      aria-label="Placeholder: Thumbnail"
                      preserveAspectRatio="xMidYMid slice"
                      focusable="false"
                    >
                      <title>Placeholder</title>
                      <rect width="100%" height="100%" fill="#55595c"></rect>
                      <text x="50%" y="50%" fill="#eceeef" dy=".3em">
                        {item.title}
                      </text>
                    </svg>

                    <div className="card-body">
                      <p className="card-text">{item.description}</p>
                      <div className="d-flex justify-content-between align-items-center">
                        <div className="btn-group">
                          <button
                            type="button"
                            className="btn btn-sm btn-outline-secondary"
                          >
                            View
                          </button>
                          <button
                            type="button"
                            className="btn btn-sm btn-outline-secondary"
                          >
                            Edit
                          </button>
                        </div>
                        <small className="text-muted">
                          {item.time_to_read} mins
                        </small>
                        #{index + 1}
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
  // дизайн
}

function ReadOne() {
  function GetData() {
    let id = 1;
    axios
      .get(`https://jsonplaceholder.typicode.com/todos/`)
      .then((response) => console.log(response.data))
      .catch((error) => console.log(error));
  }

  return (
    <div>
      ReadOne
      <button onClick={GetData} className="btn btn-lg btn-primary">
        get data
      </button>
    </div>
  );
}

function ReadAll() {
  return <div>ReadOne</div>;
}

function Create() {
  return <div>ReadOne</div>;
}

function Update() {
  return <div>ReadOne</div>;
}

function Delete() {
  return <div>ReadOne</div>;
}

export default ReadOne;
