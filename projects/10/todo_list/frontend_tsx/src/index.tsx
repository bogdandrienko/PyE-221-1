import React from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./app/store";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";

createRoot(document.getElementById("root")!).render(
  // <React.StrictMode>
  <Provider store={store}>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />}></Route>
        {/*<Route path="/tasks" element={<TaskListPage />}></Route>*/}
        {/*<Route path="/tasks/:id" element={<TaskPage />}></Route>*/}
      </Routes>
    </BrowserRouter>
  </Provider>
  // </React.StrictMode>
);
