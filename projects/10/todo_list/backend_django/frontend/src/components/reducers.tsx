import * as constants from "./constants";

export function constructorReducer(
  constant = {
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
  }
) {
  return function (state = {}, action: { type: string; payload: any }) {
    //@ts-ignore
    switch (action.type) {
      case constant.load:
        return { load: true }; // data: undefined
      case constant.success:
        return { load: false, data: action.payload }; // fail: undefined
      case constant.fail:
        return { load: false, fail: action.payload }; // error: undefined
      case constant.error:
        return { load: false, error: action.payload }; // fail: undefined
      case constant.reset:
        return {};
      default:
        return state;
    }
  };
}

export function reducerTodoList(
  state = {},
  action: { type: string; payload: any }
) {
  //@ts-ignore
  switch (action.type) {
    case constants.loadTodoList:
      return { load: true }; // data: undefined
    case constants.successTodoList:
      return { load: false, data: action.payload }; // fail: undefined
    case constants.failTodoList:
      return { load: false, fail: action.payload }; // error: undefined
    case constants.errorTodoList:
      return { load: false, error: action.payload }; // fail: undefined
    case constants.resetTodoList:
      return {};
    default:
      return state;
  }
}

export function reducerTodoDetail(
  state = {},
  action: { type: string; payload: any }
) {
  //@ts-ignore
  switch (action.type) {
    case constants.detailTodo.load:
      return { load: true }; // data: undefined
    case constants.detailTodo.success:
      return { load: false, data: action.payload }; // fail: undefined
    case constants.detailTodo.fail:
      return { load: false, fail: action.payload }; // error: undefined
    case constants.detailTodo.error:
      return { load: false, error: action.payload }; // fail: undefined
    case constants.detailTodo.reset:
      return {};
    default:
      return state;
  }
}
