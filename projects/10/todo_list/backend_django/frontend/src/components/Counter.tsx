import * as bases from "./ui/base";
import {
  Todos1,
  load,
  success,
  fail,
  reset,
  error,
} from "./CounterRedux";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import {useState} from "react";

export default function Page() {
//         getter(let)  setter(func)
    const [counter, setCounter] = useState(666) //
  function increase() {
        setCounter(counter + 1)
  }
    function decrease() {
        setCounter(counter - 1)
  }


  return (
    <div>
      <div>
        <h2>{counter}</h2>
      <button onClick={increase}>increase</button>
      <button onClick={decrease}>decrease</button>
      </div>
    </div>
  );
}
