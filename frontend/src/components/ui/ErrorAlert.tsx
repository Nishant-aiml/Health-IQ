import React from 'react';
import { AlertCircle } from 'lucide-react';

interface ErrorAlertProps {
  title?: string;
  message: string;
}

export const ErrorAlert: React.FC<ErrorAlertProps> = ({
  title = 'System Alert',
  message,
}) => {
  return (
    <div className="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900 flex items-start space-x-3 text-rose-800 dark:text-rose-200">
      <AlertCircle className="w-5 h-5 flex-shrink-0 mt-0.5 text-rose-600 dark:text-rose-400" />
      <div>
        <h4 className="text-sm font-semibold">{title}</h4>
        <p className="text-sm mt-0.5 opacity-90">{message}</p>
      </div>
    </div>
  );
};
