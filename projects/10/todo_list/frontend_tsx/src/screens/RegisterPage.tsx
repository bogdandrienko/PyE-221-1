import * as bases from "../components/ui/base";
import { FormEvent, useState } from "react";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";

import * as actions from "../components/actions";

export default function Page() {
  const dispatch = useDispatch();
  // @ts-ignore
  const storeRegisterUser = useSelector((state) => state.storeRegisterUser);

  const [user, setUser] = useState({
    username: "",
    password: "",
    name: "",
    surname: "",
    patronymic: "",
    age: 18,
  });

  async function sendForm(event: FormEvent<HTMLFormElement>) {
    event.preventDefault(); // stop reload page (!SPA)
    if (storeRegisterUser.load !== true) {
      await actions.postRegisterUser(
        dispatch,
        `http://127.0.0.1:8000/api/register`,
        { ...user }
      );
    }
  }

  // @ts-ignore
  return (
    <bases.Base2 title={"top"}>
      <div className={"container container-fluid"}>
        <form onSubmit={(event) => sendForm(event)} className={"form-signin"}>
          <div className={"card"}>
            <div className={"card-header"}>
              <h2 className={"lead fw-bold text-center"}>Please sign in</h2>
              {storeRegisterUser.data && storeRegisterUser.data}
              {storeRegisterUser.error && storeRegisterUser.error}
              {storeRegisterUser.fail && storeRegisterUser.fail}
            </div>
            <div className={"card-body"}>
              <div className="form-floating m-1">
                <input
                  type="text"
                  className="form-control"
                  id="floatingInput"
                  placeholder="bogdan"
                  value={user.username}
                  onChange={(event) =>
                    setUser({
                      ...user,
                      username: event.target.value,
                    })
                  }
                  //
                />
                <label htmlFor="floatingInput">
                  Username ({user.username})
                </label>
              </div>
              <div className="form-floating m-1">
                <input
                  type="password"
                  className="form-control"
                  id="floatingPassword"
                  placeholder="Password"
                  value={user.password}
                  onChange={(event) =>
                    setUser({
                      ...user,
                      password: event.target.value,
                    })
                  }
                />
                <label htmlFor="floatingPassword">Password</label>
              </div>

              <div className="form-check form-switch m-1">
                <input
                  className="form-check-input"
                  type="checkbox"
                  id="flexSwitchCheckDefault"
                />
                <label
                  className="form-check-label"
                  htmlFor="flexSwitchCheckDefault"
                >
                  Remember me
                </label>
              </div>
            </div>
            <div className={"card-footer p-0 m-0"}>
              <button
                className="w-100 btn btn-lg btn-primary p-3 m-0"
                type="submit"
              >
                Sign in
              </button>
            </div>
          </div>
        </form>
      </div>
    </bases.Base2>
  );
}
