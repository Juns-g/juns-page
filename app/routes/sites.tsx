import { useMemo, useState } from "react";

import { CatalogList, CatalogSelect, ViewToggle } from "~/components/catalog-list";
import catalogStyles from "~/components/catalog.module.css";
import { siteEntries } from "~/lib/content";

export const meta = () => [{ title: "Sites — Juns" }, { name: "description", content: "A public collection of useful web resources and documentation." }];

export default function Sites() {
  const [category, setCategory] = useState("All");
  const [view, setView] = useState<"list" | "grid">("list");
  const categories = useMemo(() => ["All", ...new Set(siteEntries.map((entry) => entry.category))], []);
  const entries = category === "All" ? siteEntries : siteEntries.filter((entry) => entry.category === category);

  return (
    <main>
      <h1 className="srOnly">Sites</h1>
      <div className={`${catalogStyles.controls} ${catalogStyles.sitesControls}`}>
        <ViewToggle onChange={setView} view={view} />
        <CatalogSelect label="Filter sites by category" onChange={setCategory} options={categories} value={category} />
      </div>
      <CatalogList entries={entries} variant="sites" view={view} />
    </main>
  );
}
