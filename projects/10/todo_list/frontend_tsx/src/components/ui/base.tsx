// @ts-ignore
import { useSelector } from "react-redux";

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
