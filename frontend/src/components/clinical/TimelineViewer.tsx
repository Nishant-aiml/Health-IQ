/**
 * File: TimelineViewer.tsx
 * Purpose: Chronological patient health timeline with event type icons, trend indicators, and milestone markers.
 * Module: Frontend / Components / Clinical
 * Used By: ClinicalSummaryPage
 */

import React, { useState } from 'react';
import { Activity, TrendingUp, TrendingDown, Minus, Clock } from 'lucide-react';

interface TimelineEvent {
  event_id: string;
  event_date: string;
  event_type: string;
  title: string;
  description: string;
  parameter_name?: string;
  value?: number;
  unit?: string;
  trend_direction?: string;
  clinical_significance?: string;
  is_milestone?: boolean;
}

interface TimelineViewerProps {
  events: TimelineEvent[];
}

const EVENT_COLORS: Record<string, string> = {
  lab_result: 'border-teal-400/40 bg-teal-900/10',
  diagnosis: 'border-red-400/40 bg-red-900/10',
  medication_change: 'border-amber-400/40 bg-amber-900/10',
  trend_alert: 'border-purple-400/40 bg-purple-900/10',
  wellness_milestone: 'border-emerald-400/40 bg-emerald-900/10',
  lifestyle_change: 'border-indigo-400/40 bg-indigo-900/10',
};

const DOT_COLORS: Record<string, string> = {
  lab_result: 'bg-teal-400',
  diagnosis: 'bg-red-400',
  medication_change: 'bg-amber-400',
  trend_alert: 'bg-purple-400',
  wellness_milestone: 'bg-emerald-400',
  lifestyle_change: 'bg-indigo-400',
};

const TREND_ICON: Record<string, JSX.Element> = {
  improving: <TrendingUp className="w-3.5 h-3.5 text-emerald-400" />,
  worsening: <TrendingDown className="w-3.5 h-3.5 text-red-400" />,
  stable: <Minus className="w-3.5 h-3.5 text-slate-400" />,
};

export const TimelineViewer: React.FC<TimelineViewerProps> = ({ events }) => {
  const [filter, setFilter] = useState<string>('all');

  const types = ['all', ...Array.from(new Set(events.map(e => e.event_type)))];
  const visible = filter === 'all' ? events : events.filter(e => e.event_type === filter);

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-5">
      <div className="flex items-center justify-between flex-wrap gap-3 border-b border-slate-800 pb-4">
        <h3 className="text-base font-bold text-slate-100 flex items-center gap-2">
          <Activity className="w-5 h-5 text-indigo-400" /> Health Timeline
        </h3>
        <div className="flex flex-wrap gap-1.5">
          {types.map(t => (
            <button
              key={t}
              onClick={() => setFilter(t)}
              className={`text-[10px] px-2.5 py-0.5 rounded-full font-bold capitalize transition-all border ${filter === t ? 'bg-indigo-600 text-white border-indigo-500' : 'bg-slate-950 text-slate-400 border-slate-700 hover:border-slate-500'}`}
            >
              {t.replace('_', ' ')}
            </button>
          ))}
        </div>
      </div>

      {visible.length === 0 ? (
        <div className="text-center py-8 text-slate-500 text-sm">No timeline events.</div>
      ) : (
        <ol className="relative border-l border-slate-800/70 ml-3 space-y-5">
          {visible.map((ev, idx) => (
            <li key={idx} className="ml-6 relative">
              <span className={`absolute -left-[1.62rem] top-1 w-3 h-3 rounded-full ring-2 ring-slate-900 ${DOT_COLORS[ev.event_type] || 'bg-slate-400'} ${ev.is_milestone ? 'scale-125 ring-2 ring-amber-400/70' : ''}`} />
              <div className={`p-3.5 rounded-xl border text-xs space-y-1 ${EVENT_COLORS[ev.event_type] || 'border-slate-700 bg-slate-950/50'} ${ev.is_milestone ? 'ring-1 ring-amber-400/20' : ''}`}>
                <div className="flex items-center justify-between gap-2 flex-wrap">
                  <span className="font-bold text-slate-100">{ev.title}</span>
                  <div className="flex items-center gap-1.5">
                    {ev.trend_direction && TREND_ICON[ev.trend_direction]}
                    <span className="text-[10px] text-slate-400 flex items-center gap-1">
                      <Clock className="w-2.5 h-2.5" /> {ev.event_date}
                    </span>
                    {ev.is_milestone && <span className="text-[10px] bg-amber-900/30 text-amber-300 border border-amber-700/30 px-1.5 py-0.5 rounded font-bold">Milestone</span>}
                  </div>
                </div>
                <p className="text-slate-300 leading-relaxed">{ev.description}</p>
                {ev.parameter_name && (
                  <div className="flex items-center gap-2 mt-1 text-[11px] text-slate-400">
                    <span className="font-mono bg-slate-950 px-1.5 py-0.5 rounded">{ev.parameter_name}: <strong className="text-slate-200">{ev.value} {ev.unit}</strong></span>
                    {ev.clinical_significance && (
                      <span className={`px-1.5 py-0.5 rounded font-bold ${ev.clinical_significance === 'Critical' ? 'bg-red-900/30 text-red-300' : ev.clinical_significance === 'Borderline' ? 'bg-amber-900/30 text-amber-300' : 'bg-emerald-900/20 text-emerald-300'}`}>
                        {ev.clinical_significance}
                      </span>
                    )}
                  </div>
                )}
              </div>
            </li>
          ))}
        </ol>
      )}
    </div>
  );
};
