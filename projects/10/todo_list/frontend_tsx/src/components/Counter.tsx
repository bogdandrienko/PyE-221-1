import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

export const load = "load";
export const success = "success";
export const fail = "fail";
export const error = "error";
export const reset = "reset";

export function TodosReducer(
  state = {},
  action: { type: string; payload: any }
) {
  //@ts-ignore
  switch (action.type) {
    case load:
      return { load: true, data: undefined, error: undefined };
    case success:
      return { load: false, data: action.payload, error: undefined };
    case fail:
      return { load: false, data: undefined, error: "Ошибка фронта" };
    case error:
      return { load: false, data: undefined, error: "Ошибка бэка" };
    case reset:
      return { load: undefined, data: undefined, error: undefined };
    default:
      return state;
  }
}

export function Todos1() {
  // @ts-ignore
  const todosStore = useSelector((state) => state.todosStore);

  useEffect(() => {
    console.log(todosStore);
  }, [todosStore]);

  return (
    <div>
      {todosStore.load === true && "Идёт загрузка данных"}
      {todosStore.fail && todosStore.fail}
      {todosStore.error && todosStore.error}
      <ul>
        {todosStore.data &&
          todosStore.data.map(
            // @ts-ignore
            (item, index) => <li key={index}>{item.title}</li>
          )}
      </ul>
    </div>
  );
}
