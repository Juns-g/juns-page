import { index, route, type RouteConfig } from "@react-router/dev/routes";

const routes = [
  index("routes/home.tsx"),
  route("stack", "routes/stack.tsx"),
  route("sites", "routes/sites.tsx"),
  route("til", "routes/til.tsx"),
  route("computer", "routes/computer.tsx"),
  route("listening", "routes/listening.tsx"),
] satisfies RouteConfig;

if (process.env.ENABLE_EXPERIMENTS === "true") {
  routes.push(route("workflows", "routes/workflows.tsx"));
}

export default routes;
