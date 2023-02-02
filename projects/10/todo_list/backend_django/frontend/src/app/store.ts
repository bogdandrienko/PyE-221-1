import { configureStore } from "@reduxjs/toolkit";
import thunk from "redux-thunk";
import { combineReducers } from "@reduxjs/toolkit";
import { TodosReducer } from "../components/CounterRedux";
import { WebReducer } from "../components/WebReducer";
import { reducerAboutCounter } from "../pages/AboutPage";

import * as reducers from "../components/reducers";
import * as constants from "../components/constants";
import { listTodos } from "../components/constants";

// @ts-ignore
export const reducer = combineReducers({
  todosStore: TodosReducer,
  webStore: WebReducer,
  todoListStoreOld: reducers.reducerTodoList,
  //todoListStoreOld: reducers.constructorReducer(),
  todoDetailStore: reducers.reducerTodoDetail,
  aboutStoreCounter: reducerAboutCounter,
  storeRegisterUser: reducers.constructorReducer(
    constants.constantRegisterUser
  ),
  todoListStore: reducers.constructorReducer(constants.listTodos),
  todoDetailStore1: reducers.constructorReducer(constants.detailTodo),
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
