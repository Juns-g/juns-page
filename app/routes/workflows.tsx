import { PageFrame, PageIntro } from "~/components/page-frame";
import { WorkflowExplorer } from "~/components/workflow-explorer";
import { evidenceWorkflow } from "~/lib/workflow-content";
import styles from "./workflows.module.css";

export const meta = () => [{ title: "Workflow lab — Juns" }, { name: "description", content: "An experimental Evidence Ledger workflow interaction." }, { name: "robots", content: "noindex,nofollow" }];
export default function Workflows() { return <PageFrame><PageIntro eyebrow="Experimental · Hidden route" title="Evidence review pipeline"><p>A safe sample workflow based only on the public Evidence Ledger concept. Select a step to inspect its inputs, outputs, and review boundary.</p></PageIntro><WorkflowExplorer steps={evidenceWorkflow} /><p className={styles.hint}>Keyboard: use Tab to enter the step list, then Arrow, Home, or End to move between steps.</p></PageFrame>; }
