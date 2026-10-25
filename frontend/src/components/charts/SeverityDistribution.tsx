/* --------------------------------------------------
 * File: SeverityDistribution.tsx
 * Purpose: Visual distribution bar chart showing parameters by severity (Normal, Mild, Moderate, Severe).
 * Module: Frontend Chart Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2E Data Visualizations
 * -------------------------------------------------- */

import React from 'react';
import { Card } from '../ui/Card';
import { BarChart3 } from 'lucide-react';

interface ParameterSeverityItem {
  severity: string;
}

interface SeverityDistributionProps {
  parameters: ParameterSeverityItem[];
}

export const SeverityDistribution: React.FC<SeverityDistributionProps> = ({ parameters }) => {
  const counts = {
    normal: 0,
    mild: 0,
    moderate: 0,
    severe: 0,
  };

  parameters.forEach((p) => {
    const sev = p.severity?.toLowerCase() || 'normal';
    if (sev in counts) {
      counts[sev as keyof typeof counts]++;
    } else {
      counts.normal++;
    }
  });

  const total = parameters.length || 1;
  const normalPct = Math.round((counts.normal / total) * 100);
  const mildPct = Math.round((counts.mild / total) * 100);
  const modPct = Math.round((counts.moderate / total) * 100);
  const severePct = Math.round((counts.severe / total) * 100);

  return (
    <Card header={
      <div className="flex items-center space-x-2">
        <BarChart3 className="w-5 h-5 text-brand-600 dark:text-brand-400" />
        <h3 className="text-base font-bold text-slate-900 dark:text-slate-100">
          Parameter Severity Breakdown ({parameters.length})
        </h3>
      </div>
    }>
      <div className="space-y-4">
        {/* Progress Bar Container */}
        <div className="h-4 w-full bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden flex">
          <div style={{ width: `${normalPct}%` }} className="bg-emerald-500 transition-all duration-500" title={`Normal: ${counts.normal}`} />
          <div style={{ width: `${mildPct}%` }} className="bg-amber-400 transition-all duration-500" title={`Mild: ${counts.mild}`} />
          <div style={{ width: `${modPct}%` }} className="bg-orange-500 transition-all duration-500" title={`Moderate: ${counts.moderate}`} />
          <div style={{ width: `${severePct}%` }} className="bg-rose-600 transition-all duration-500" title={`Severe: ${counts.severe}`} />
        </div>

        {/* Breakdown Legend Badges */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-semibold text-slate-700 dark:text-slate-300">
          <div className="flex items-center space-x-2 p-2 bg-emerald-50 dark:bg-emerald-950/40 rounded-xl border border-emerald-200/60 dark:border-emerald-900/40">
            <span className="w-3 h-3 rounded-full bg-emerald-500 flex-shrink-0" />
            <span>Normal ({counts.normal})</span>
          </div>
          <div className="flex items-center space-x-2 p-2 bg-amber-50 dark:bg-amber-950/40 rounded-xl border border-amber-200/60 dark:border-amber-900/40">
            <span className="w-3 h-3 rounded-full bg-amber-400 flex-shrink-0" />
            <span>Mild ({counts.mild})</span>
          </div>
          <div className="flex items-center space-x-2 p-2 bg-orange-50 dark:bg-orange-950/40 rounded-xl border border-orange-200/60 dark:border-orange-900/40">
            <span className="w-3 h-3 rounded-full bg-orange-500 flex-shrink-0" />
            <span>Moderate ({counts.moderate})</span>
          </div>
          <div className="flex items-center space-x-2 p-2 bg-rose-50 dark:bg-rose-950/40 rounded-xl border border-rose-200/60 dark:border-rose-900/40">
            <span className="w-3 h-3 rounded-full bg-rose-600 flex-shrink-0" />
            <span>Severe ({counts.severe})</span>
          </div>
        </div>
      </div>
    </Card>
  );
};
