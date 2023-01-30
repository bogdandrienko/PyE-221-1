import * as bases from "../components/ui/base";
import { useState } from "react";
import * as constants from "../components/constants";
import { useDispatch, useSelector } from "react-redux";

export function reducerAboutCounter(
  state = {},
  action: { type: string; payload: any }
) {
  switch (action.type) {
    case "negative":
      return { data: -1 * action.payload };
    case "positive":
      return { data: action.payload };
    default:
      return state;
  }
}

export default function Page() {
  const dispatch = useDispatch();
  // @ts-ignore
  const aboutStoreCounter = useSelector((state) => state.aboutStoreCounter);
  return (
    // todo visual: HTML + CSS + JSX
    <div>
      <h1>About Page</h1>
      <div>
        {aboutStoreCounter.data ? aboutStoreCounter.data : "нет данных"}
      </div>
      <button
        onClick={() => {
          dispatch({ type: "negative", payload: 1000 });
        }}
      >
        negative
      </button>
      <button
        onClick={() => {
          dispatch({ type: "positive", payload: 1000 });
        }}
      >
        positive
      </button>
    </div>
  );
}
