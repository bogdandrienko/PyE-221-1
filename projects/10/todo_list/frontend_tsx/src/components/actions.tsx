import * as constants from "./constants";
import axios from "axios";

// @ts-ignore
export async function getTodoList(dispatch) {
  try {
    dispatch({ type: constants.loadTodoList });
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/todos"
    );
    if (
      response.data ||
      // @ts-ignore
      (response.status === 200 && response.status === 201)
    ) {
      dispatch({ type: constants.successTodoList, payload: response.data });
      console.log(response.data);
    } else {
      dispatch({
        type: constants.errorTodoList,
        payload: response.statusText,
      });
      console.log(response.status, response.statusText);
    }
  } catch (error: any) {
    dispatch({ type: constants.failTodoList, payload: error.toString() });
    console.log("error: ", error);
  }
}

// @ts-ignore
export async function getTodoDetail(dispatch, id) {
  try {
    dispatch({ type: constants.loadTodoDetail });
    const response = await axios.get(
      `https://jsonplaceholder.typicode.com/todos/${id}`
    );
    if (
      response.data ||
      // @ts-ignore
      (response.status === 200 && response.status === 201)
    ) {
      dispatch({ type: constants.successTodoDetail, payload: response.data });
      console.log(response.data);
    } else {
      dispatch({
        type: constants.errorTodoDetail,
        payload: response.statusText,
      });
      console.log(response.status, response.statusText);
    }
  } catch (error: any) {
    dispatch({ type: constants.failTodoDetail, payload: error.toString() });
    console.log("error: ", error);
  }
}
