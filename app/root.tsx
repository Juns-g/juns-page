import {
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
  isRouteErrorResponse,
  useRouteError,
} from "react-router";

import { SiteShell } from "./components/site-shell";
import "./styles/globals.css";

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="#000000" />
        <Meta />
        <Links />
      </head>
      <body>
        {children}
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export default function App() {
  return <SiteShell><Outlet /></SiteShell>;
}

export function ErrorBoundary() {
  const error = useRouteError();
  const title = isRouteErrorResponse(error) && error.status === 404 ? "Page not found" : "Something went wrong";
  return (
    <main style={{ width: "min(calc(100% - 32px), 680px)", margin: "20vh auto" }}>
      <p style={{ color: "var(--accent)", fontFamily: "var(--font-mono)" }}>Juns / {isRouteErrorResponse(error) ? error.status : "Error"}</p>
      <h1>{title}</h1>
      <p><a href="/" style={{ textDecoration: "underline" }}>Return home</a></p>
    </main>
  );
}
