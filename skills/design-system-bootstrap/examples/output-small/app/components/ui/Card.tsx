import styles from "./Card.module.css";

type CardVariant = "default" | "elevated" | "outlined" | "ghost";

interface CardProps {
  variant?: CardVariant;
  as?: "div" | "article" | "section" | "li";
  onClick?: () => void;
  className?: string;
  children: React.ReactNode;
}

const variantClass: Record<CardVariant, string> = {
  default:  styles.default,
  elevated: styles.elevated,
  outlined: styles.outlined,
  ghost:    styles.ghost,
};

export function Card({
  variant = "default",
  as: Tag = "div",
  onClick,
  className,
  children,
}: CardProps) {
  const isClickable = !!onClick;

  return (
    <Tag
      className={[
        styles.card,
        variantClass[variant],
        isClickable ? styles.clickable : "",
        className ?? "",
      ]
        .filter(Boolean)
        .join(" ")}
      onClick={onClick}
      role={isClickable ? "button" : undefined}
      tabIndex={isClickable ? 0 : undefined}
      onKeyDown={
        isClickable
          ? (e) => {
              if (e.key === "Enter" || e.key === " ") onClick();
            }
          : undefined
      }
    >
      {children}
    </Tag>
  );
}

function CardHeader({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <div className={[styles.header, className ?? ""].filter(Boolean).join(" ")}>{children}</div>
  );
}

function CardBody({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <div className={[styles.body, className ?? ""].filter(Boolean).join(" ")}>{children}</div>
  );
}

function CardFooter({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <div className={[styles.footer, className ?? ""].filter(Boolean).join(" ")}>{children}</div>
  );
}

Card.Header = CardHeader;
Card.Body = CardBody;
Card.Footer = CardFooter;
