/**
 * File: TrendSummary.tsx
 * Purpose: Executive summary banner with ELI10 plain-language analogies and longitudinal disclaimers.
 * Module: Frontend / Components / History
 * Used By: HistoryPage Component
 * Future Phase: Phase 3B Longitudinal Health Intelligence
 */

import React from 'react';
import { Sparkles, Info } from 'lucide-react';

interface SummaryPayload {
  summary_text: string;
  eli10_notes: string[];
  disclaimer: string;
}

interface TrendSummaryProps {
  summary: SummaryPayload;
  totalReports: number;
}

export const TrendSummary: React.FC<TrendSummaryProps> = ({ summary, totalReports }) => {
  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
        <h2 className="text-lg font-bold text-slate-100 flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-teal-400" /> Longitudinal Health Journey Summary
        </h2>
        <span className="text-xs text-teal-300 bg-teal-950/60 border border-teal-500/30 px-3 py-1 rounded-full font-bold">
          {totalReports} Report(s) Analyzed
        </span>
      </div>

      <div className="space-y-4">
        <div className="bg-slate-950/60 p-4 rounded-xl border border-slate-800 text-xs text-slate-200 leading-relaxed whitespace-pre-line">
          {summary.summary_text}
        </div>

        {summary.eli10_notes && summary.eli10_notes.length > 0 && (
          <div className="bg-gradient-to-r from-teal-950/30 to-indigo-950/30 p-4 rounded-xl border border-teal-500/30 space-y-2">
            <h4 className="text-xs font-bold text-teal-300 flex items-center gap-1.5">
              <Sparkles className="w-4 h-4 text-teal-400" /> Plain-Language Trend Analogies (ELI10)
            </h4>
            {summary.eli10_notes.map((note, idx) => (
              <p key={idx} className="text-xs text-slate-200 flex items-start gap-2">
                <span className="text-teal-400">•</span> {note}
              </p>
            ))}
          </div>
        )}

        <div className="pt-2 flex items-center gap-2 text-[11px] text-slate-400 border-t border-slate-800/80">
          <Info className="w-4 h-4 text-slate-500 shrink-0" />
          <span>{summary.disclaimer}</span>
        </div>
      </div>
    </div>
  );
};
