/* --------------------------------------------------
 * File: ParameterDetailModal.tsx
 * Purpose: Modal drawer component for inspecting plain-language parameter details.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2B Results Dashboard
 * -------------------------------------------------- */

import React from 'react';
import { ParameterItem } from './ParameterCard';
import { X } from 'lucide-react';
import { Button } from '../ui/Button';

interface ParameterDetailModalProps {
  parameter: ParameterItem | null;
  onClose: () => void;
}

export const ParameterDetailModal: React.FC<ParameterDetailModalProps> = ({
  parameter,
  onClose,
}) => {
  if (!parameter) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm animate-fade-in">
      <div className="bg-white dark:bg-slate-900 rounded-3xl max-w-lg w-full p-6 shadow-xl border border-slate-200 dark:border-slate-800 space-y-5">
        <div className="flex items-center justify-between">
          <h3 className="text-xl font-bold text-slate-900 dark:text-slate-100">
            {parameter.canonical_name}
          </h3>
          <button
            onClick={onClose}
            className="p-2 min-h-[44px] min-w-[44px] flex items-center justify-center text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="p-4 bg-slate-50 dark:bg-slate-800/50 rounded-2xl flex items-center justify-between">
          <div>
            <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Observed Value</span>
            <div className="text-2xl font-black text-slate-900 dark:text-slate-100">
              {parameter.value} <span className="text-sm font-semibold text-slate-400">{parameter.unit}</span>
            </div>
          </div>
          <div className="text-right">
            <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Demographic Baseline</span>
            <div className="text-sm font-bold text-slate-700 dark:text-slate-300">
              {parameter.normal_range_low} - {parameter.normal_range_high} {parameter.unit}
            </div>
          </div>
        </div>

        <div className="space-y-2 text-sm text-slate-600 dark:text-slate-400">
          <p className="font-semibold text-slate-900 dark:text-slate-100">Clinical Severity Status:</p>
          <div className="p-3 rounded-xl bg-brand-50/50 dark:bg-brand-950/30 text-brand-800 dark:text-brand-200 border border-brand-200/50 dark:border-brand-900/50">
            Severity level evaluated as <strong className="capitalize">{parameter.severity}</strong> based on demographic-adjusted reference range midpoints.
          </div>
        </div>

        <div className="pt-2">
          <Button onClick={onClose} className="w-full min-h-[44px]">
            Close Breakdown
          </Button>
        </div>
      </div>
    </div>
  );
};
