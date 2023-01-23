import * as bases from "../components/ui/base";
import {
  Todos1,
  load,
  success,
  fail,
  reset,
  error,
} from "../components/CounterRedux";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import HttpPage from "../components/Counter";
import WebReducer from "../components/WebReducer";
import {useEffect} from "react";


export default function Page() {
  const dispatch = useDispatch();
// @ts-ignore
  const webStore = useSelector((state) => state.webStore);

  async function getData(){

      const response = await axios.get("https://jsonplaceholder.typicode.com/todos")
      console.log(response.data)

      const load = false
      const success = undefined
      const data = undefined
      const error = undefined

      const web = {
          load : false,
          success : undefined,
          data : undefined,
          error : undefined,
          reset : undefined
      }


      // LOAD (loader) 1
      // SUCCESS (.map) 1 + 1
      // ERROR (text) 1

  }

  // <button onClick={() => }>load</button>
  // <button onClick={() => }>
  //   success
  // </button>
  // <button onClick={() => }>fail</button>
  // <button onClick={() => dispatch({ type: error })}>error</button>
  // <button onClick={() => dispatch({ type: reset })}>reset</button>

  async function get() {
    dispatch({ type: load });
    try {
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/1todos"
      );
      dispatch({ type: success, payload: response.data });
    } catch (error) {
      dispatch({ type: fail });
    }
  }

  useEffect(()=> {
      console.log(webStore)
  }, [webStore])
  return (
    <bases.Base1 title={"Hello"}>
      <h1>Home page</h1>
        <div>{webStore.load === true ? "загрузка идёт" : "загрузка остановилась"}</div>
      
      <Todos1 />
      <button onClick={() => getData()}>get</button>

      <br/>
      <br/>
      <br/>
      <WebReducer/>
    </bases.Base1>
  );
}
