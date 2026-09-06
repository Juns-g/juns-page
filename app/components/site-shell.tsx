import { useEffect, useRef, useState, type KeyboardEvent, type ReactNode } from "react";
import { Link, useLocation } from "react-router";

import { GitHubIcon, MailIcon } from "./social-icons";
import styles from "./site-shell.module.css";

const routes = [
  { href: "/", label: "Home" },
  { href: "/stack", label: "Stack" },
  { href: "/sites", label: "Sites" },
  { href: "/til", label: "TIL" },
  { href: "/computer", label: "Computer" },
  { href: "/listening", label: "Listening" },
];

const pageNames: Record<string, string> = {
  "/stack": "Stack",
  "/sites": "Sites",
  "/til": "TIL",
  "/computer": "Computer",
  "/listening": "Listening",
  "/workflows": "Workflow lab",
};

export function SiteShell({ children }: { children: ReactNode }) {
  const { pathname } = useLocation();
  const [open, setOpen] = useState(false);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const menuRef = useRef<HTMLDivElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);
  const wasOpen = useRef(false);
  const current = pageNames[pathname];

  useEffect(() => {
    setOpen(false);
  }, [pathname]);

  useEffect(() => {
    const content = contentRef.current;
    if (content) content.inert = open;

    if (!open) {
      document.body.style.overflow = "";
      if (wasOpen.current) triggerRef.current?.focus();
      wasOpen.current = false;
      return;
    }

    wasOpen.current = true;
    document.body.style.overflow = "hidden";
    const frame = window.requestAnimationFrame(() => {
      menuRef.current?.querySelector<HTMLElement>("a")?.focus();
    });

    return () => {
      window.cancelAnimationFrame(frame);
      document.body.style.overflow = "";
    };
  }, [open]);

  function handleMenuKeyDown(event: KeyboardEvent<HTMLDivElement>) {
    if (event.key === "Escape") {
      event.preventDefault();
      setOpen(false);
      return;
    }

    if (event.key !== "Tab") return;
    const focusable = Array.from(menuRef.current?.querySelectorAll<HTMLElement>("a[href]") ?? []);
    if (!focusable.length) return;
    const first = focusable[0];
    const last = focusable.at(-1)!;
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  return (
    <div className={styles.site}>
      <header className={styles.topBar}>
        <button
          aria-controls="site-menu"
          aria-expanded={open}
          aria-label={open ? "Close menu" : "Open menu"}
          className={`${styles.menuButton} ${open ? styles.open : ""}`}
          onClick={() => setOpen((value) => !value)}
          ref={triggerRef}
          type="button"
        >
          <span aria-hidden="true" className={styles.menuGlyph} />
        </button>
        {current && !open ? (
          <nav aria-label="Breadcrumb" className={styles.breadcrumb}>
            <Link to="/" viewTransition>Juns</Link>
            <span aria-hidden="true">/</span>
            <span aria-current="page">{current}</span>
          </nav>
        ) : null}
      </header>

      <div
        aria-label="Site navigation"
        aria-modal="true"
        className={styles.menuLayer}
        hidden={!open}
        id="site-menu"
        onKeyDown={handleMenuKeyDown}
        ref={menuRef}
        role="dialog"
      >
        <nav className={styles.menuNav}>
          <Link aria-current={pathname === "/" ? "page" : undefined} onClick={() => setOpen(false)} to="/" viewTransition>Home</Link>
          <p>Collections</p>
          {routes.slice(1).map((route) => (
            <Link
              aria-current={pathname === route.href ? "page" : undefined}
              key={route.href}
              onClick={() => setOpen(false)}
              to={route.href}
              viewTransition
            >
              {route.label}
            </Link>
          ))}
        </nav>
        <div aria-label="Contact links" className={styles.menuSocials}>
          <a aria-label="GitHub (opens in a new tab)" href="https://github.com/Juns-g" rel="noreferrer noopener" target="_blank"><GitHubIcon /></a>
          <a aria-label="Email Juns" href="mailto:juns.g@foxmail.com"><MailIcon /></a>
        </div>
      </div>

      <div className={styles.content} ref={contentRef}>{children}</div>
    </div>
  );
}
