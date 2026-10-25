/* --------------------------------------------------
 * File: EmptyState.tsx
 * Purpose: Intentional empty state component for missing recommendations, evidence, or chat history.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage & Tabs
 * Future Phase: Phase 2E Complete UX States
 * -------------------------------------------------- */

import React from 'react';
import { Card } from '../ui/Card';
import { CheckCircle2, Info } from 'lucide-react';

interface EmptyStateProps {
  title: string;
  description: string;
  type?: 'success' | 'info';
}

export const EmptyState: React.FC<EmptyStateProps> = ({
  title,
  description,
  type = 'info',
}) => {
  return (
    <Card className="text-center p-8 space-y-3 bg-slate-50/50 dark:bg-slate-900/50">
      <div className="flex justify-center">
        {type === 'success' ? (
          <CheckCircle2 className="w-10 h-10 text-emerald-500" />
        ) : (
          <Info className="w-10 h-10 text-brand-600 dark:text-brand-400" />
        )}
      </div>
      <h3 className="text-base font-bold text-slate-900 dark:text-slate-100">
        {title}
      </h3>
      <p className="text-xs text-slate-500 dark:text-slate-400 max-w-md mx-auto leading-relaxed">
        {description}
      </p>
    </Card>
  );
};
