import { parse } from "yaml";

import catalogsRaw from "../../content/catalogs.yaml?raw";
import homeRaw from "../../content/home.yaml?raw";

export type CatalogEntry = {
  name: string;
  marker: string;
  category: string;
  description: string;
  href: string;
  meta: string;
};

export type ListeningEntry = {
  record: string;
  artist: string;
  format: string;
  status: string;
  marker: string;
};

export type CollectionItem = {
  name: string;
  description: string;
  href: string;
  marker: string;
  kind: "project" | "collection";
  external?: boolean;
};

export type RecentNote = { title: string; label: string; href: string };

export type EditorialEntry = {
  number: string;
  title: string;
  summary: string;
  tag: string;
  source?: { label: string; href: string };
};

const home = parse(homeRaw) as {
  recentNotes: RecentNote[];
  collections: CollectionItem[];
};

const catalogs = parse(catalogsRaw) as {
  stack: CatalogEntry[];
  sites: CatalogEntry[];
  listening: ListeningEntry[];
};

const markdownFiles = import.meta.glob("../../content/{til,computer}/*.md", {
  eager: true,
  query: "?raw",
  import: "default",
}) as Record<string, string>;

function parseMarkdownDocument(source: string): EditorialEntry {
  const match = source.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) throw new Error("Content file is missing YAML frontmatter");

  const attributes = parse(match[1]) as {
    number: string;
    title: string;
    tag: string;
    sourceLabel?: string;
    sourceHref?: string;
  };

  return {
    number: attributes.number,
    title: attributes.title,
    tag: attributes.tag,
    summary: match[2].trim(),
    source:
      attributes.sourceLabel && attributes.sourceHref
        ? { label: attributes.sourceLabel, href: attributes.sourceHref }
        : undefined,
  };
}

function entriesFor(folder: "til" | "computer") {
  return Object.entries(markdownFiles)
    .filter(([path]) => path.includes(`/content/${folder}/`))
    .map(([, source]) => parseMarkdownDocument(source))
    .sort((a, b) => a.number.localeCompare(b.number));
}

export const recentNotes = home.recentNotes;
export const collections = home.collections;
export const stackEntries = catalogs.stack;
export const siteEntries = catalogs.sites;
export const listeningSamples = catalogs.listening;
export const tilEntries = entriesFor("til");
export const computerEntries = entriesFor("computer");
