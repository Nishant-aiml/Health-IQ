/**
 * File: ComparisonCard.tsx
 * Purpose: Side-by-side report comparison component displaying delta badges (Improved, Unchanged, Worsened).
 * Module: Frontend / Components / History
 * Used By: HistoryPage Component
 * Future Phase: Phase 3B Longitudinal Health Intelligence
 */

import React from 'react';
import { ArrowLeftRight, CheckCircle2, AlertCircle, Minus } from 'lucide-react';

export interface BiomarkerChangeItem {
  canonical_name: string;
  unit: string;
  target_value: number;
  reference_value: number;
  absolute_change: number;
  percentage_change: number;
  change_status: string;
  clinical_significance: string;
  summary_note: string;
}

export interface ComparisonResultPayload {
  comparison_mode: string;
  target_report_id: number;
  reference_report_id: number;
  health_score_delta: number;
  improved_count: number;
  unchanged_count: number;
  worsened_count: number;
  biomarker_changes: BiomarkerChangeItem[];
  overall_clinical_assessment: string;
}

interface ComparisonCardProps {
  comparison: ComparisonResultPayload;
}

export const ComparisonCard: React.FC<ComparisonCardProps> = ({ comparison }) => {
  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 mb-6 shadow-xl">
      <div className="flex items-center justify-between flex-wrap gap-2 mb-4">
        <div>
          <h3 className="text-base font-bold text-slate-100 flex items-center gap-2">
            <ArrowLeftRight className="w-5 h-5 text-teal-400" /> Longitudinal Report Comparison ({comparison.comparison_mode})
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">{comparison.overall_clinical_assessment}</p>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-lg border border-emerald-500/30 font-bold">
            {comparison.improved_count} Improved
          </span>
          <span className="text-xs bg-slate-800 text-slate-300 px-2.5 py-1 rounded-lg border border-slate-700 font-bold">
            {comparison.unchanged_count} Unchanged
          </span>
          <span className="text-xs bg-rose-500/20 text-rose-300 px-2.5 py-1 rounded-lg border border-rose-500/30 font-bold">
            {comparison.worsened_count} Worsened
          </span>
        </div>
      </div>

      <div className="space-y-2">
        {comparison.biomarker_changes.map((item, idx) => (
          <div
            key={idx}
            className="bg-slate-950/60 border border-slate-800/80 rounded-xl p-3 flex items-center justify-between text-xs"
          >
            <div>
              <span className="font-semibold text-slate-200">{item.canonical_name}</span>
              <p className="text-[11px] text-slate-400">{item.summary_note}</p>
            </div>

            <div className="flex items-center gap-4 text-right">
              <div>
                <span className="text-slate-400 block text-[10px]">Reference → Current</span>
                <span className="font-bold text-slate-200">
                  {item.reference_value} → {item.target_value} {item.unit}
                </span>
              </div>

              <span
                className={`px-2.5 py-1 rounded-lg font-bold text-xs flex items-center gap-1 ${
                  item.change_status === 'Improved'
                    ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                    : item.change_status === 'Worsened'
                    ? 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                    : 'bg-slate-800 text-slate-400'
                }`}
              >
                {item.change_status === 'Improved' && <CheckCircle2 className="w-3.5 h-3.5" />}
                {item.change_status === 'Worsened' && <AlertCircle className="w-3.5 h-3.5" />}
                {item.change_status === 'Unchanged' && <Minus className="w-3.5 h-3.5" />}
                {item.change_status} ({item.percentage_change}%)
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
