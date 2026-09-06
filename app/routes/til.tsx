import { TilFeed } from "~/components/editorial-feed";
import { tilEntries } from "~/lib/content";
import styles from "./editorial-pages.module.css";

export const meta = () => [{ title: "TIL — Juns" }, { name: "description", content: "Five concise, sourced notes about building for the web." }];

export default function Til() {
  return <main className={styles.tilPage}><h1>TIL</h1><TilFeed entries={tilEntries} /></main>;
}
