import * as bases from "../components/ui/base";
import {
  Todos1,
  load,
  success,
  fail,
  reset,
  error,
} from "../components/Counter";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

export default function Page() {
  const dispatch = useDispatch();

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

  return (
    <bases.Base1 title={"Hello"}>
      <h1>Home page</h1>
      <Todos1 />
      <button onClick={() => get()}>get</button>
    </bases.Base1>
  );
}
