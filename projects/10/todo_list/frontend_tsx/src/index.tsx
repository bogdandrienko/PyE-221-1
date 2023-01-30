import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./app/store";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./screens/HomePage";
import RegisterPage from "./screens/RegisterPage";
import AboutPage from "./pages/AboutPage";
import TodoList from "./pages/TodoList";
import TodoDetail from "./pages/TodoDetail";
import HttpPage from "./components/Counter";
import "./css/bootstrap/bootstrap.css";
import "./css/my.css";

createRoot(document.getElementById("root")!).render(
  // <React.StrictMode>
  <Provider store={store}>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />}></Route>
        <Route path="/about" element={<AboutPage />}></Route>
        <Route path="/register" element={<RegisterPage />}></Route>
        <Route path="/http" element={<HttpPage />}></Route>
        <Route path="/todos" element={<TodoList />}></Route>
        <Route path="/todos/:id" element={<TodoDetail />}></Route>
        {/*<Route path="/tasks" element={<TaskListPage />}></Route>*/}
        {/*<Route path="/tasks/:id" element={<TaskPage />}></Route>*/}
      </Routes>
    </BrowserRouter>
  </Provider>
  // </React.StrictMode>
);
