import { ComputerIndex } from "~/components/editorial-feed";
import { computerEntries } from "~/lib/content";
import styles from "./editorial-pages.module.css";

export const meta = () => [{ title: "Computer — Juns" }, { name: "description", content: "Six concise tips for reliable computer and agent workflows." }];

export default function Computer() {
  return (
    <main className={styles.computerPage}>
      <h1>How to Computer Better</h1>
      <p>Concise tips for more reliable everyday computer work.</p>
      <ComputerIndex entries={computerEntries} />
    </main>
  );
}
