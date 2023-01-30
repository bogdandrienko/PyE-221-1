// @ts-ignore
import { useSelector } from "react-redux";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";

import * as navbars from "./navbars";

// @ts-ignore
export function Base1({ children, title }): JSX.Element {
  return (
    <div>
      navbar {title}
      <div>{children}</div>
      footer
    </div>
  );
}

// @ts-ignore
export function Base2({ children, title }): JSX.Element {
  return (
    <main>
      <div>
        <navbars.OffCanvasExample
          name={"Модули"}
          title={"Модули"}
          placement={"top"}
        />
      </div>
      <div className={"mt-5"}>{children}</div>
      footer
      <a href={"http://localhost:3001/"}>внимание</a>
    </main>
  );
}
