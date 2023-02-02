import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { Link } from "react-router-dom";

import * as actions from "../components/actions";
import axios from "axios";

export default function Page() {
  const dispatch = useDispatch();
  // @ts-ignore
  const todoListStoreOld = useSelector((state) => state.todoListStoreOld);

  useEffect(() => {
    actions.getTodoList(dispatch);
  }, []);

  async function getTodos() {
    const response = await axios.get("http://127.0.0.1:8000/api/todos/");
    console.log(response);
    console.log(response.data);
  }

  return (
    <div>
      <h1 className={"lead text-danger text-center"}>Todos list</h1>
      <button className={"btn btn-danger"} onClick={getTodos}>
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
    </div>
  );
}
