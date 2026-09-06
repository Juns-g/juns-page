import { useMemo, useState } from "react";

import { CatalogList, CatalogSelect } from "~/components/catalog-list";
import catalogStyles from "~/components/catalog.module.css";
import { stackEntries } from "~/lib/content";

export const meta = () => [{ title: "Stack — Juns" }, { name: "description", content: "A small catalog of public tools and services." }];

export default function Stack() {
  const [category, setCategory] = useState("All categories");
  const [context, setContext] = useState("All contexts");
  const categories = useMemo(() => ["All categories", ...new Set(stackEntries.map((entry) => entry.category))], []);
  const contexts = useMemo(() => ["All contexts", ...new Set(stackEntries.map((entry) => entry.meta))], []);
  const entries = stackEntries.filter((entry) =>
    (category === "All categories" || entry.category === category) &&
    (context === "All contexts" || entry.meta === context));

  return (
    <main>
      <h1 className="srOnly">Stack</h1>
      <div className={catalogStyles.controls}>
        <CatalogSelect label="Filter by category" onChange={setCategory} options={categories} value={category} />
        <CatalogSelect label="Filter by context" onChange={setContext} options={contexts} value={context} />
      </div>
      <CatalogList entries={entries} variant="stack" />
    </main>
  );
}
