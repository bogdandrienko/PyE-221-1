import * as constants from "./constants";
import axios from "axios";
import { Dispatch } from "react";

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
    dispatch({ type: constants.detailTodo.load });
    const response = await axios.get(
      `https://jsonplaceholder.typicode.com/todos/${id}`
    );
    if (
      response.data ||
      // @ts-ignore
      (response.status === 200 && response.status === 201)
    ) {
      dispatch({ type: constants.detailTodo.success, payload: response.data });
      console.log(response.data);
    } else {
      dispatch({
        type: constants.detailTodo.error,
        payload: response.statusText,
      });
      console.log(response.status, response.statusText);
    }
  } catch (error: any) {
    dispatch({ type: constants.detailTodo.fail, payload: error.toString() });
    console.log("error: ", error);
  }
}

// @ts-ignore
export async function postRegisterUser(dispatch, url, data) {
  try {
    dispatch({ type: constants.constantRegisterUser.load });
    const response = await axios.post(url, data);
    if (
      response.data ||
      // @ts-ignore
      (response.status === 200 && response.status === 201)
    ) {
      dispatch({
        type: constants.constantRegisterUser.success,
        payload: response.data,
      });
      console.log(response.data);
    } else {
      dispatch({
        type: constants.constantRegisterUser.error,
        payload: response.statusText,
      });
      console.log(response.status, response.statusText);
    }
  } catch (error: any) {
    dispatch({
      type: constants.constantRegisterUser.fail,
      payload: error.toString(),
    });
    console.log("error: ", error);
  }
}

export function getDetailTodo(id: number) {
  return constructorAction({
    // url: `https://jsonplaceholder.typicode.com/todos/${id}`,
    url: `http://127.0.0.1:8000/api/todos/${id}/`,
    constant: constants.detailTodo,
  });
}

export function getAllTodos() {
  return constructorAction({
    // url: `https://jsonplaceholder.typicode.com/todos/`,
    url: `http://127.0.0.1:8000/api/todos/`,
    constant: constants.listTodos,
  });
}

export function constructorAction(
  props = {
    // @ts-ignore
    url,
    constant: {
      // @ts-ignore
      load: string,
      // @ts-ignore
      success: string,
      // @ts-ignore
      fail: string,
      // @ts-ignore
      error: string,
      // @ts-ignore
      reset: string,
    },
  }
) {
  return async function (dispatch: any) {
    try {
      // TODO load
      dispatch({ type: props.constant.load });
      const response = await axios.get(props.url); // todo откуда берём данные
      if (response.status === 200 || response.status === 201) {
        // TODO success
        dispatch({
          type: props.constant.success, // todo куда ложим успешные данные
          payload: response.data,
        });
      } else {
        // TODO error
        dispatch({
          type: props.constant.error,
          payload: response.statusText,
        });
      }
    } catch (error) {
      console.log("error: ", error);
      // TODO fail
      dispatch({
        type: props.constant.fail,
        // @ts-ignore
        payload: error.toString(),
      });
    }
  };
}
