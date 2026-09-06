import type { EditorialEntry } from "~/lib/content";
import { ExternalLink } from "./external-link";
import styles from "./editorial.module.css";

export function TilFeed({ entries }: { entries: EditorialEntry[] }) {
  return (
    <ol className={styles.tilFeed}>
      {entries.map((entry) => (
        <li className={styles.tilEntry} key={entry.number}>
          <span className={styles.tilTag}>{entry.tag}</span>
          <span className={styles.metric}>{entry.number}</span>
          <article>
            <h2>{entry.title}</h2>
            <p>{entry.summary}</p>
            {entry.source ? <ExternalLink className={styles.source} href={entry.source.href}>Learn more</ExternalLink> : null}
          </article>
        </li>
      ))}
    </ol>
  );
}

export function ComputerIndex({ entries }: { entries: EditorialEntry[] }) {
  return (
    <ol className={styles.computerIndex}>
      {entries.map((entry) => (
        <li key={entry.number}>
          <details className={styles.technique}>
            <summary>
              <span aria-hidden="true">{entry.number}</span>
              <strong>{entry.title}</strong>
            </summary>
            <div className={styles.techniqueDetail}>
              <p>{entry.summary}</p>
              {entry.source ? <ExternalLink href={entry.source.href}>Source: {entry.source.label}</ExternalLink> : null}
            </div>
          </details>
        </li>
      ))}
    </ol>
  );
}
