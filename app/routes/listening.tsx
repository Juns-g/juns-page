import { listeningSamples } from "~/lib/content";
import styles from "./listening.module.css";

export const meta = () => [{ title: "Listening — Juns" }, { name: "description", content: "A manual listening collection with no connected music account." }];

export default function Listening() {
  return (
    <main>
      <h1 className="srOnly">Listening</h1>
      <p className={styles.disclosure}>Layout-only samples · no account or listening history</p>
      <table className={styles.table}>
        <thead><tr><th scope="col">Record</th><th scope="col">Artist</th><th scope="col">Format</th><th scope="col">Status</th></tr></thead>
        <tbody>{listeningSamples.map((item) => (
          <tr key={item.record}>
            <td><span className={styles.record}><span className={styles.marker} aria-hidden="true">{item.marker}</span><strong>{item.record}</strong></span></td>
            <td className={styles.artist}>{item.artist}</td>
            <td className={styles.format}>{item.format}</td>
            <td className={styles.status}>{item.status}</td>
          </tr>
        ))}</tbody>
      </table>
    </main>
  );
}
