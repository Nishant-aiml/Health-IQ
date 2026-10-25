/* --------------------------------------------------
 * File: CriticalAlertBanner.tsx
 * Purpose: High-visibility emergency critical value alert banner component.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2B Results Dashboard
 * -------------------------------------------------- */

import React from 'react';
import { ShieldAlert } from 'lucide-react';

export interface CriticalAlertItem {
  is_critical: boolean;
  parameter_name: string;
  value: number;
  unit: string;
  reason: string;
  recommended_action: string;
}

interface CriticalAlertBannerProps {
  alerts: CriticalAlertItem[];
}

export const CriticalAlertBanner: React.FC<CriticalAlertBannerProps> = ({ alerts }) => {
  if (!alerts || alerts.length === 0) return null;

  return (
    <div className="p-4 sm:p-5 bg-rose-500/10 dark:bg-rose-950/40 border-2 border-rose-500/30 rounded-3xl space-y-3 shadow-md animate-bounce-short">
      <div className="flex items-center space-x-3 text-rose-700 dark:text-rose-300">
        <div className="p-2 bg-rose-500 text-white rounded-xl shadow-sm">
          <ShieldAlert className="w-6 h-6 animate-pulse" />
        </div>
        <div>
          <h3 className="text-base sm:text-lg font-bold tracking-tight">
            Critical Medical Alert ({alerts.length})
          </h3>
          <p className="text-xs sm:text-sm font-medium opacity-90">
            One or more extracted lab parameters exceed dangerous critical safety thresholds.
          </p>
        </div>
      </div>

      <div className="divide-y divide-rose-200/50 dark:divide-rose-900/50 border border-rose-200 dark:border-rose-900 rounded-2xl overflow-hidden bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm">
        {alerts.map((alert, idx) => (
          <div key={idx} className="p-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div className="space-y-0.5">
              <div className="flex items-center space-x-2">
                <span className="font-bold text-sm text-slate-900 dark:text-slate-100">
                  {alert.parameter_name}
                </span>
                <span className="text-xs font-bold text-rose-600 dark:text-rose-400 bg-rose-100 dark:bg-rose-950 px-2 py-0.5 rounded-md">
                  {alert.value} {alert.unit}
                </span>
              </div>
              <p className="text-xs text-rose-700 dark:text-rose-300 font-medium">
                {alert.reason}
              </p>
            </div>
            <div className="text-xs font-semibold text-rose-800 dark:text-rose-200 bg-rose-50 dark:bg-rose-950/60 px-3 py-1.5 rounded-xl border border-rose-200 dark:border-rose-800">
              {alert.recommended_action}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
