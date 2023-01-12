import React, {useState} from 'react';
import logo from './logo.svg';
import { Counter } from './features/counter/Counter';
import './App.css';
import axios from "axios"

axios.defaults.baseURL = "http://127.0.0.1:8000/api";

function App() {
    // const [userId, setUserId] = useState()

    async function getOneUser(id: number){
        const config = {
          url: `/users/${id}`,
          method: `GET`,
          timeout: 5000,
          headers: {
            Authorization: ``,
          },
          data: {},
        };
        const response = await axios(config);
        // @ts-ignore
        console.log(response)
    }

    async function getAllUser(){
        const timeStart = Date();

        const config = {
          url: `users/`,
          method: `GET`,
          timeout: 5000,
          headers: {
            Authorization: ``,
          },
          data: {},
        };
        const response = await axios(config);
        // @ts-ignore
        console.log(response)
        const timeEnd = Date();

        // @ts-ignore
        console.log(timeEnd, timeStart)
    }

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={()=> getOneUser(1)}>get One User</button>
        <button onClick={getAllUser} >get All Users</button>

      </header>
    </div>
  );
}

export default App;
