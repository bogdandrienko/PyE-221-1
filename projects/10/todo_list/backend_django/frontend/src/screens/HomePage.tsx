import { Link } from "react-router-dom";
import React from "react";

import * as bases from "../components/ui/base";

export default function Page() {
  // @ts-ignore
  return (
    <bases.Base2>
      <div className="text-center border-bottom">
        <h1 className="display-4 fw-bold">Todo list app</h1>
        <div className="col-lg-6 mx-auto">
          <p className="lead mb-4">
            Quickly design and customize responsive mobile-first sites with
            Bootstrap, the world’s most popular front-end open source toolkit,
            featuring Sass variables and mixins, responsive grid system,
            extensive prebuilt components, and powerful JavaScript plugins.
          </p>
          <div className="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">
            <Link
              to={"/todos"}
              className={"btn btn-outline-primary btn-lg px-4 me-sm-3"}
            >
              Todo list
            </Link>
            <Link
              to={"/todos/create"}
              className={"btn btn-outline-success btn-lg px-4 me-sm-3"}
            >
              Post new task
            </Link>
          </div>
        </div>
        <div className="overflow-hidden">
          <div className="container px-5">
            <img
              src="/static/img/to-do-list-apps.png"
              className="img-fluid img-thumbnail border rounded-3 shadow-lg mb-1"
              alt="Example image"
              width="600"
              height="400"
              loading="lazy"
            />
          </div>
        </div>
      </div>
    </bases.Base2>
  );
}
