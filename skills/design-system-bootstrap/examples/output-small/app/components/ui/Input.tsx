import { forwardRef } from "react";
import styles from "./Input.module.css";

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  hideLabel?: boolean;
  error?: string;
  hint?: string;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(function Input(
  { label, hideLabel = false, error, hint, id, className, disabled, ...props },
  ref
) {
  const inputId = id ?? `input-${label.toLowerCase().replace(/\s+/g, "-")}`;
  const errorId = error ? `${inputId}-error` : undefined;
  const hintId = hint && !error ? `${inputId}-hint` : undefined;

  return (
    <div className={[styles.wrapper, className ?? ""].filter(Boolean).join(" ")}>
      <label
        htmlFor={inputId}
        className={[styles.label, hideLabel ? styles.srOnly : ""].filter(Boolean).join(" ")}
      >
        {label}
      </label>

      <input
        ref={ref}
        id={inputId}
        className={[
          styles.input,
          error ? styles.hasError : "",
          disabled ? styles.disabled : "",
        ]
          .filter(Boolean)
          .join(" ")}
        aria-invalid={!!error}
        aria-describedby={errorId ?? hintId}
        disabled={disabled}
        {...props}
      />

      {error && (
        <span id={errorId} className={styles.errorMessage} role="alert">
          {error}
        </span>
      )}

      {hint && !error && (
        <span id={hintId} className={styles.hint}>
          {hint}
        </span>
      )}
    </div>
  );
});
