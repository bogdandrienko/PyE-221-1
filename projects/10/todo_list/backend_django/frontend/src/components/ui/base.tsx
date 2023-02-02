// @ts-ignore
import { useSelector } from "react-redux";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";

import * as navbars from "./navbars";
import * as footers from "./footers";

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
export function Base2({ children }): JSX.Element {
  return (
    <main>
      <navbars.Navbar1 name={"Модули"} title={"Модули"} placement={"top"} />
      <div className={"my-5"}>{children}</div>
      <footers.Footer1 />
    </main>
  );
}
