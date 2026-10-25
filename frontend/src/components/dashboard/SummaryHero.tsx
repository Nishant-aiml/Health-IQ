/* --------------------------------------------------
 * File: SummaryHero.tsx
 * Purpose: Hero banner component summarizing overall report status, score, and critical flags.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2E Dashboard Polish
 * -------------------------------------------------- */

import React from 'react';
import { Badge } from '../ui/Badge';
import { Activity, AlertTriangle, ShieldCheck } from 'lucide-react';

interface SummaryHeroProps {
  score: number;
  summary: string;
  criticalCount: number;
}

export const SummaryHero: React.FC<SummaryHeroProps> = ({ score, summary, criticalCount }) => {
  const getScoreColor = (s: number) => {
    if (s >= 80) return 'text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/40 border-emerald-200/60 dark:border-emerald-900/40';
    if (s >= 60) return 'text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/40 border-amber-200/60 dark:border-amber-900/40';
    return 'text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/40 border-rose-200/60 dark:border-rose-900/40';
  };

  return (
    <div className="p-6 bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-4">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="flex items-center space-x-4">
          <div className={`p-4 rounded-2xl border ${getScoreColor(score)} font-black text-2xl`}>
            {score}
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h2 className="text-xl font-bold text-slate-900 dark:text-slate-100">
                Health Score & Clinical Index
              </h2>
              {criticalCount > 0 ? (
                <Badge variant="danger">
                  <AlertTriangle className="w-3 h-3 mr-1 inline" /> {criticalCount} Critical Alert(s)
                </Badge>
              ) : (
                <Badge variant="success">
                  <ShieldCheck className="w-3 h-3 mr-1 inline" /> All Clear
                </Badge>
              )}
            </div>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">
              {summary}
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2 text-xs font-semibold text-slate-500 dark:text-slate-400 self-start sm:self-auto">
          <Activity className="w-4 h-4 text-brand-600 dark:text-brand-400" />
          <span>Calculated via Reference Interval Penalties</span>
        </div>
      </div>
    </div>
  );
};
