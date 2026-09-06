import type { ReactNode } from "react";

import styles from "./page-frame.module.css";

export function PageFrame({
  children,
  reading = false,
}: {
  children: ReactNode;
  reading?: boolean;
}) {
  return (
    <main className={styles.shell}>
      <div className={`${styles.body} ${reading ? styles.reading : ""}`}>{children}</div>
    </main>
  );
}

export function PageIntro({
  eyebrow,
  title,
  children,
  variant = "default",
}: {
  eyebrow?: string;
  title: string;
  children: ReactNode;
  variant?: "default" | "editorial";
}) {
  return (
    <section className={`${styles.intro} ${styles[variant]}`}>
      {eyebrow ? <p className={styles.eyebrow}>{eyebrow}</p> : null}
      <h1>{title}</h1>
      {children}
    </section>
  );
}
