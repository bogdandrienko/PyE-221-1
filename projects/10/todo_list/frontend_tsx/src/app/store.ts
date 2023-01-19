import { configureStore } from "@reduxjs/toolkit";
import thunk from "redux-thunk";
import { combineReducers } from "@reduxjs/toolkit";
import { TodosReducer } from "../components/CounterRedux";
import { WebReducer } from "../components/WebReducer";

import * as reducers from "../components/reducers";

// @ts-ignore
export const reducer = combineReducers({
  todosStore: TodosReducer,
  webStore: WebReducer,
  todoListStore: reducers.reducerTodoList,
  todoDetailStore: reducers.reducerTodoDetail,
});

const preloadedState = {
  // @ts-ignore
  // userLoginStore: {
  //   data:
  //     accessToken && refreshToken
  //       ? { access: accessToken, refresh: refreshToken }
  //       : undefined,
  // },
};

export const store = configureStore({
  reducer: reducer,
  devTools: process.env.NODE_ENV !== "production",
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk),
  preloadedState: preloadedState,
});