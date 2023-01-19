import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { useParams } from "react-router-dom";

import * as actions from "../components/actions";

export default function Page() {
  const dispatch = useDispatch();
  const id = useParams().id;

  // @ts-ignore
  const todoDetailStore = useSelector((state) => state.todoDetailStore);

  useEffect(() => {
    actions.getTodoDetail(dispatch, id);
  }, []);

  return (
    <div>
      <h1 className={"lead text-danger text-center"}>Todos list</h1>
      <div className={"container container-fluid text-center"}>
        {todoDetailStore.load === true && (
          <div className={"small fw-light"}>Идёт загрузка</div>
        )}
        {todoDetailStore.fail && (
          <div className={"small fw-light"}>Обратитесь к администатору</div>
        )}
        {todoDetailStore.error && (
          <div className={"small fw-light"}>{todoDetailStore.error}</div>
        )}
        <div className="row row-cols-1 row-cols-sm-1 row-cols-md-1 g-1">
          {!todoDetailStore.data ? (
            "данных пока нет"
          ) : (
            <div className="col">
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
                  <title>
                    {todoDetailStore.data.title} ({todoDetailStore.data.id})
                  </title>
                  <rect width="100%" height="100%" fill="#55595c"></rect>
                  <text x="50%" y="50%" fill="#eceeef" dy=".3em">
                    {todoDetailStore.data.title} ({todoDetailStore.data.id})
                  </text>
                </svg>

                <div
                  className={
                    todoDetailStore.data.completed
                      ? "card-body border border-3 border-success"
                      : "card-body border border-3 border-warning"
                  }
                >
                  <p className="card-text">
                    This is a wider card with supporting text below as a natural
                    lead-in to additional content. This content is a little bit
                    longer. ({todoDetailStore.data.id})
                  </p>
                  <div className="d-flex justify-content-between align-items-center">
                    <div className="btn-group">
                      <button
                        type="button"
                        className="btn btn-sm btn-outline-secondary"
                      >
                        View
                      </button>
                      <button
                        type="button"
                        className="btn btn-sm btn-outline-secondary"
                      >
                        Edit
                      </button>
                    </div>
                    <small className="text-muted">
                      {todoDetailStore.data.userId}
                    </small>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
