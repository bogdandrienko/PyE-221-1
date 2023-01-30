import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

export const loadWeb = "loadWeb";
export const successWeb = "successWeb";
export const failWeb = "failWeb";
export const errorWeb = "errorWeb";
export const resetWeb = "resetWeb";

export function WebReducer(state = {}, action: { type: string; payload: any }) {
  //@ts-ignore
  switch (action.type) {
    case loadWeb:
      return { load: true, data: undefined, error: undefined };
    case successWeb:
      return { load: false, data: action.payload, error: undefined };
    case failWeb:
      return { load: false, data: undefined, error: action.payload };
    case errorWeb:
      return { load: false, data: undefined, error: action.payload };
    case resetWeb:
      return { load: undefined, data: undefined, error: undefined };
    default:
      return state;
  }
}

export default function Page() {
  const dispatch = useDispatch();

  async function getData() {
    try {
      dispatch({ type: "loadWeb" });
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/todos"
      );
      if (
        response.data ||
        // @ts-ignore
        (response.status === 200 && response.status === 201)
      ) {
        dispatch({ type: successWeb, payload: response.data });
        // console.log(response.data)
      } else {
        dispatch({ type: errorWeb, payload: response.statusText });
        console.log(response.status, response.statusText);
      }
    } catch (error: any) {
      dispatch({ type: failWeb, payload: error.toString() });
      console.log("error: ", error);
    }
  }

  return (
    <div>
      <button onClick={getData}>getData</button>
    </div>
  );
}
