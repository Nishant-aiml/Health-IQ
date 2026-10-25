import React from 'react';

interface TypographyProps {
  variant?: 'h1' | 'h2' | 'h3' | 'h4' | 'body' | 'caption';
  children: React.ReactNode;
  className?: string;
}

export const Typography: React.FC<TypographyProps> = ({
  variant = 'body',
  children,
  className = '',
}) => {
  switch (variant) {
    case 'h1':
      return <h1 className={`text-4xl font-extrabold tracking-tight text-slate-900 dark:text-slate-100 sm:text-5xl ${className}`}>{children}</h1>;
    case 'h2':
      return <h2 className={`text-3xl font-bold tracking-tight text-slate-900 dark:text-slate-100 ${className}`}>{children}</h2>;
    case 'h3':
      return <h3 className={`text-xl font-semibold text-slate-900 dark:text-slate-100 ${className}`}>{children}</h3>;
    case 'h4':
      return <h4 className={`text-lg font-medium text-slate-900 dark:text-slate-100 ${className}`}>{children}</h4>;
    case 'caption':
      return <p className={`text-xs text-slate-500 dark:text-slate-400 ${className}`}>{children}</p>;
    case 'body':
    default:
      return <p className={`text-base text-slate-600 dark:text-slate-300 leading-relaxed ${className}`}>{children}</p>;
  }
};
