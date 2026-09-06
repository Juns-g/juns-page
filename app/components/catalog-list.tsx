import { useEffect, useId, useRef, useState, type KeyboardEvent } from "react";

import type { CatalogEntry } from "~/lib/content";
import { ExternalLink } from "./external-link";
import styles from "./catalog.module.css";

export function CatalogSelect({
  label,
  onChange,
  options,
  value,
}: {
  label: string;
  onChange: (value: string) => void;
  options: string[];
  value: string;
}) {
  const listboxId = useId();
  const rootRef = useRef<HTMLDivElement>(null);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const selectedIndex = Math.max(0, options.indexOf(value));
  const [open, setOpen] = useState(false);
  const [highlightedIndex, setHighlightedIndex] = useState(selectedIndex);

  useEffect(() => {
    if (!open) return;

    function handlePointerDown(event: PointerEvent) {
      if (event.target instanceof Node && !rootRef.current?.contains(event.target)) setOpen(false);
    }

    document.addEventListener("pointerdown", handlePointerDown);
    return () => document.removeEventListener("pointerdown", handlePointerDown);
  }, [open]);

  function showOptions(index = selectedIndex) {
    setHighlightedIndex(index);
    setOpen(true);
  }

  function selectOption(index: number) {
    onChange(options[index]);
    setHighlightedIndex(index);
    setOpen(false);
    triggerRef.current?.focus();
  }

  function handleKeyDown(event: KeyboardEvent<HTMLButtonElement>) {
    const lastIndex = options.length - 1;

    if (event.key === "Escape" && open) {
      event.preventDefault();
      setOpen(false);
      return;
    }

    if (event.key === "Tab") {
      setOpen(false);
      return;
    }

    if (event.key === "ArrowDown" || event.key === "ArrowUp") {
      event.preventDefault();
      const direction = event.key === "ArrowDown" ? 1 : -1;
      if (!open) {
        showOptions((selectedIndex + direction + options.length) % options.length);
      } else {
        setHighlightedIndex((index) => (index + direction + options.length) % options.length);
      }
      return;
    }

    if (event.key === "Home" || event.key === "End") {
      event.preventDefault();
      showOptions(event.key === "Home" ? 0 : lastIndex);
      return;
    }

    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      if (open) selectOption(highlightedIndex);
      else showOptions();
    }
  }

  return (
    <div className={styles.selectWrap} ref={rootRef}>
      <button
        aria-activedescendant={open ? `${listboxId}-option-${highlightedIndex}` : undefined}
        aria-controls={listboxId}
        aria-expanded={open}
        aria-haspopup="listbox"
        aria-label={`${label}: ${value}`}
        className={styles.selectTrigger}
        onClick={() => open ? setOpen(false) : showOptions()}
        onKeyDown={handleKeyDown}
        ref={triggerRef}
        role="combobox"
        type="button"
      >
        <span className={styles.selectValue}>{value}</span>
        <svg aria-hidden="true" className={styles.selectChevron} viewBox="0 0 24 24"><path d="m7 10 5 5 5-5" /></svg>
      </button>
      <div aria-label={label} className={styles.selectMenu} hidden={!open} id={listboxId} role="listbox">
        {options.map((option, index) => (
          <div
            aria-selected={option === value}
            className={`${styles.selectOption} ${index === highlightedIndex ? styles.highlightedOption : ""}`}
            id={`${listboxId}-option-${index}`}
            key={option}
            onClick={() => selectOption(index)}
            onMouseDown={(event) => event.preventDefault()}
            onMouseEnter={() => setHighlightedIndex(index)}
            role="option"
          >
            {option === value ? <svg aria-hidden="true" className={styles.optionCheck} viewBox="0 0 16 16"><path d="m3 8 3 3 7-7" /></svg> : null}
            {option}
          </div>
        ))}
      </div>
    </div>
  );
}

export function ViewToggle({ view, onChange }: { view: "list" | "grid"; onChange: (view: "list" | "grid") => void }) {
  return (
    <div aria-label="View" className={styles.viewToggle} role="group">
      <button aria-label="List view" aria-pressed={view === "list"} onClick={() => onChange("list")} type="button"><span className={styles.listIcon} /></button>
      <button aria-label="Grid view" aria-pressed={view === "grid"} onClick={() => onChange("grid")} type="button"><span className={styles.gridIcon}><i /><i /><i /><i /></span></button>
    </div>
  );
}

function siteLabel(href: string) {
  try {
    return new URL(href).hostname.replace(/^www\./, "");
  } catch {
    return href;
  }
}

export function CatalogList({
  entries,
  variant,
  view = "list",
}: {
  entries: CatalogEntry[];
  variant: "stack" | "sites";
  view?: "list" | "grid";
}) {
  const sites = variant === "sites";
  return (
    <div className={`${styles.list} ${styles[variant]} ${view === "grid" ? styles.gridView : ""}`} role="table" aria-label={sites ? "Sites" : "Stack"}>
      <div className={styles.tableHead} role="row">
        <span role="columnheader">Name</span>
        <span role="columnheader">{sites ? "Site" : "Description"}</span>
        <span role="columnheader">Category</span>
        <span role="columnheader">Context</span>
      </div>
      <div className={styles.rows} role="rowgroup">
        {entries.map((entry) => {
          const secondary = sites ? siteLabel(entry.href) : entry.description;
          return (
            <ExternalLink className={styles.row} href={entry.href} key={entry.name} role="row">
              <span className={styles.identity} role="cell">
                <span className={styles.marker} aria-hidden="true">{entry.marker}</span>
                <span className={styles.primaryCopy}>
                  <strong>{entry.name}</strong>
                  <span className={styles.mobileSecondary}>{secondary}</span>
                  {sites ? <span className="srOnly"> — {entry.description}</span> : null}
                </span>
              </span>
              <span className={styles.detail} role="cell">{sites ? siteLabel(entry.href) : entry.description}</span>
              <span className={styles.category} role="cell">{entry.category}</span>
              <span className={styles.meta} role="cell">{entry.meta}</span>
              <span className={styles.mobileChip} aria-hidden="true">{entry.category}</span>
            </ExternalLink>
          );
        })}
      </div>
    </div>
  );
}
