import type { Config } from "@react-router/dev/config";

const experimentsEnabled = process.env.ENABLE_EXPERIMENTS === "true";

const publicRoutes = ["/", "/stack", "/sites", "/til", "/computer", "/listening"];

export default {
  ssr: false,
  prerender: experimentsEnabled ? [...publicRoutes, "/workflows"] : publicRoutes,
} satisfies Config;
