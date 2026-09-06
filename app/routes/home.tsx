import { Link } from "react-router";

import { ExternalLink } from "~/components/external-link";
import { GitHubIcon, MailIcon } from "~/components/social-icons";
import { collections, recentNotes } from "~/lib/content";
import styles from "./home.module.css";

export const meta = () => [
  { title: "Juns — Front-end engineering and reliable AI workflows" },
  { name: "description", content: "Juns' public home for front-end engineering, reliable AI workflows, projects, and collections." },
];

export default function Home() {
  return (
    <main className={styles.shell}>
      <header className={styles.masthead}>
        <span className={styles.mark} aria-hidden="true">J</span>
        <h1>Juns</h1>
        <p className={styles.intro}>I build front-end systems and reliable AI workflows—clear interfaces, careful tools, and inspectable evidence.</p>
        <div className={styles.contacts} aria-label="Contact links">
          <ExternalLink aria-label="GitHub" href="https://github.com/Juns-g"><GitHubIcon /></ExternalLink>
          <a aria-label="Email Juns" href="mailto:juns.g@foxmail.com"><MailIcon /></a>
        </div>
      </header>

      <section className={styles.section} aria-labelledby="notes-heading">
        <Link className={styles.writingLink} to="/til" viewTransition>
          <h2 id="notes-heading">Writing</h2>
          <svg aria-hidden="true" viewBox="0 0 32 32">
            <path d="m12 8 8 8-8 8" />
          </svg>
        </Link>
        <ol className={styles.notes}>
          {recentNotes.map((note) => <li key={note.title}><Link className={styles.note} to={note.href} viewTransition>{note.title}</Link></li>)}
        </ol>
      </section>

      <section className={styles.section} aria-labelledby="collections-heading">
        <div className={styles.sectionHead}><h2 id="collections-heading">Projects &amp; Collections</h2></div>
        <div className={styles.collections}>
          {collections.map((item) => {
            const content = <><strong>{item.name}</strong>{" "}<span>{item.description}</span></>;
            return item.external ? <ExternalLink className={styles.row} href={item.href} key={item.name}>{content}</ExternalLink> : <Link className={styles.row} to={item.href} key={item.name} viewTransition>{content}</Link>;
          })}
        </div>
      </section>
    </main>
  );
}
