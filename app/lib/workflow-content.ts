import { parse } from "yaml";

import workflowsRaw from "../../content/workflows.yaml?raw";

export type WorkflowStep = {
  id: string;
  label: string;
  short: string;
  status: string;
  evidence: string;
  purpose: string;
  input: string;
  output: string;
  check: string;
};

export const evidenceWorkflow = parse(workflowsRaw) as WorkflowStep[];
