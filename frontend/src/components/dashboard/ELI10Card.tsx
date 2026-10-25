/* --------------------------------------------------
 * File: ELI10Card.tsx
 * Purpose: Child-friendly plain-language explanation (Explain Like I'm 10) card component.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2C Results Dashboard
 * -------------------------------------------------- */

import React from 'react';
import { Card } from '../ui/Card';
import { Smile, HeartHandshake } from 'lucide-react';

interface ELI10CardProps {
  explanation: string;
}

export const ELI10Card: React.FC<ELI10CardProps> = ({ explanation }) => {
  return (
    <Card className="space-y-3 bg-teal-50/30 dark:bg-teal-950/20 border-teal-200/60 dark:border-teal-900/50">
      <div className="flex items-center space-x-2 text-teal-700 dark:text-teal-300 font-bold text-base">
        <Smile className="w-5 h-5 text-teal-600 dark:text-teal-400" />
        <span>Simple Explanation (Explain Like I'm 10)</span>
      </div>
      <p className="text-sm text-slate-700 dark:text-slate-300 leading-relaxed bg-white/80 dark:bg-slate-900/80 p-4 rounded-2xl border border-teal-100 dark:border-teal-900/40">
        {explanation}
      </p>
      <div className="flex items-center space-x-1.5 text-xs text-slate-400 font-medium">
        <HeartHandshake className="w-4 h-4 text-teal-500" />
        <span>Designed for non-medical users and family understanding.</span>
      </div>
    </Card>
  );
};
