import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

import * as actions from "../components/actions";
import * as bases from "../components/ui/base";
import * as constants from "../components/constants";

export default function Page() {
  const dispatch = useDispatch();
  // @ts-ignore
  const todoListStoreOld = useSelector((state) => state.todoListStoreOld);
  // @ts-ignore
  const todoListStore = useSelector((state) => state.todoListStore);
  // @ts-ignore
  const todoDetailStore1 = useSelector((state) => state.todoDetailStore1);

  useEffect(() => {
    // actions.getTodoList(dispatch);
  }, []);

  useEffect(() => {
    console.log(todoListStore);
  }, [todoListStore]);

  useEffect(() => {
    console.log(todoDetailStore1);
  }, [todoDetailStore1]);

  async function getTodos1() {
    console.log("getTodos1");

    // @ts-ignore
    dispatch(actions.getAllTodos());
    // @ts-ignore
    dispatch(actions.getDetailTodo(1));

    // actions.getDetailTodo(1);
  }

  async function getTodos() {
    try {
      // TODO load
      dispatch({ type: constants.listTodos.load });
      // const response = await axios.get("http://127.0.0.1:8000/api/todos/");
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/todos"
      );
      if (response.status === 200 || response.status === 201) {
        // TODO success
        dispatch({ type: constants.listTodos.success, payload: response.data });
      } else {
        // TODO error
        dispatch({
          type: constants.listTodos.error,
          payload: response.statusText,
        });
      }
    } catch (error) {
      console.log("error: ", error);
      // TODO fail
      dispatch({
        type: constants.listTodos.fail,
        // @ts-ignore
        payload: error.toString(),
      });
    }
  }

  async function getTodo(id: number) {
    try {
      // TODO load
      dispatch({ type: constants.listTodos.load });
      // const response = await axios.get("http://127.0.0.1:8000/api/todos/");
      const response = await axios.get(
        `https://jsonplaceholder.typicode.com/todos/${id}`
      );
      if (response.status === 200 || response.status === 201) {
        // TODO success
        dispatch({ type: constants.listTodos.success, payload: response.data });
      } else {
        // TODO error
        dispatch({
          type: constants.listTodos.error,
          payload: response.statusText,
        });
      }
    } catch (error) {
      console.log("error: ", error);
      // TODO fail
      dispatch({
        type: constants.listTodos.fail,
        // @ts-ignore
        payload: error.toString(),
      });
    }
  }

  return (
    <bases.Base2>
      <h1 className={"lead text-danger text-center"}>Todos list</h1>
      <button className={"btn btn-danger"} onClick={getTodos1}>
        getTodos 2
      </button>
      <div className={"container container-fluid text-center"}>
        {todoListStoreOld.load === true && (
          <div className={"small fw-light"}>Идёт загрузка</div>
        )}
        {todoListStoreOld.fail && (
          <div className={"small fw-light"}>Обратитесь к администатору</div>
        )}
        {todoListStoreOld.error && (
          <div className={"small fw-light"}>{todoListStoreOld.error}</div>
        )}
        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
          {!todoListStoreOld.data
            ? "данных пока нет"
            : // @ts-ignore
              todoListStoreOld.data.map((item, index) => (
                <div key={item.id} className="col">
                  <div className="card shadow-sm">
                    <svg
                      className="bd-placeholder-img card-img-top"
                      width="100%"
                      height="225"
                      xmlns="http://www.w3.org/2000/svg"
                      role="img"
                      aria-label="Placeholder: Thumbnail"
                      preserveAspectRatio="xMidYMid slice"
                      focusable="false"
                    >
                      <title>{item.title}</title>
                      <rect width="100%" height="100%" fill="#55595c"></rect>
                      <text x="50%" y="50%" fill="#eceeef" dy=".3em">
                        {item.title} ({item.id})
                      </text>
                    </svg>

                    <div
                      className={
                        item.completed
                          ? "card-body border border-3 border-success"
                          : "card-body border border-3 border-warning"
                      }
                    >
                      <p className="card-text">
                        This is a wider card with supporting text below as a
                        natural lead-in to additional content. This content is a
                        little bit longer. ({item.id})
                      </p>
                      <div className="d-flex justify-content-between align-items-center">
                        <div className="btn-group">
                          <Link to={`/todos/${item.id}`}>
                            <button
                              type="button"
                              className="btn btn-sm btn-outline-secondary"
                            >
                              View
                            </button>
                          </Link>
                          <button
                            type="button"
                            className="btn btn-sm btn-outline-secondary"
                          >
                            Edit
                          </button>
                        </div>
                        <small className="text-muted">{item.userId}</small>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
        </div>
      </div>
    </bases.Base2>
  );
}
