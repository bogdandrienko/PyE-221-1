import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Offcanvas from "react-bootstrap/Offcanvas";
import NavDropdown from "react-bootstrap/NavDropdown";
import { Link } from "react-router-dom";

// @ts-ignore
export function Navbar1({ name, title, ...props }) {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  return (
    <div>
      <Button
        variant="light"
        onClick={handleShow}
        className={"w-100 p-3 border border-1 border-dark"}
      >
        {name}
      </Button>
      <Offcanvas
        show={show}
        onHide={handleClose}
        className={"offcanvas-top-custom-1"}
        {...props}
      >
        <Offcanvas.Header closeButton onClick={handleClose}>
          <Offcanvas.Title>{title}</Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body>
          <div
            className={
              "row row-cols-1 row-cols-sm-1  row-cols-md-2 row-cols-lg-3"
            }
          >
            <NavDropdown title="Профиль" id="nav-dropdown">
              <NavDropdown.Item>
                <Link
                  to={"/register"}
                  className={"text-decoration-none text-dark"}
                >
                  Зарегистрироваться
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Divider />
              <Link
                to={"/login"}
                className={
                  "btn btn-outline-primary text-decoration-none text-dark"
                }
              >
                Войти
              </Link>
              <Link
                to={"/logout"}
                className={
                  "btn btn-outline-danger text-decoration-none text-dark"
                }
              >
                Выйти
              </Link>
            </NavDropdown>
            <NavDropdown title="Tasks" id="nav-dropdown">
              <NavDropdown.Item>
                <Link
                  to={"/todos"}
                  className={"text-decoration-none text-dark"}
                >
                  Todo list
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item eventKey="4.2">
                Create a new task
              </NavDropdown.Item>
            </NavDropdown>
          </div>
        </Offcanvas.Body>
      </Offcanvas>
    </div>
  );
}
