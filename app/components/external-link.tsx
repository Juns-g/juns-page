import type { AnchorHTMLAttributes, ReactNode } from "react";

type Props = AnchorHTMLAttributes<HTMLAnchorElement> & { children: ReactNode };

export function ExternalLink({ children, ...props }: Props) {
  return (
    <a {...props} target="_blank" rel="noreferrer noopener">
      {children}
      <span className="srOnly"> (opens in a new tab)</span>
    </a>
  );
}
