/**
 * File: HistoryTimeline.tsx
 * Purpose: Chronological health journey milestone timeline feed displaying typed events.
 * Module: Frontend / Components / History
 * Used By: HistoryPage Component
 * Future Phase: Phase 3B Longitudinal Health Intelligence
 */

import React from 'react';
import { Calendar, FileText, AlertTriangle, ShieldCheck, Pill, Activity } from 'lucide-react';

export interface TimelineEventItem {
  event_id?: number;
  event_type: string;
  title: string;
  description: string;
  event_date: string;
  severity_level: string;
  icon_hint: string;
}

interface HistoryTimelineProps {
  events: TimelineEventItem[];
}

export const HistoryTimeline: React.FC<HistoryTimelineProps> = ({ events }) => {
  const getEventIcon = (type: string, severity: string) => {
    if (type === 'UPLOAD') return <FileText className="w-4 h-4 text-teal-400" />;
    if (type === 'ALERT_CREATED' || severity === 'CRITICAL') return <AlertTriangle className="w-4 h-4 text-rose-400" />;
    if (type === 'PATTERN_RESOLVED' || type === 'ALERT_RESOLVED') return <ShieldCheck className="w-4 h-4 text-emerald-400" />;
    if (type === 'PRESCRIPTION_UPDATED') return <Pill className="w-4 h-4 text-amber-400" />;
    return <Activity className="w-4 h-4 text-indigo-400" />;
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl mb-6">
      <h3 className="text-base font-bold text-slate-100 mb-4 flex items-center gap-2">
        <Calendar className="w-5 h-5 text-teal-400" /> Patient Health Journey Milestones ({events.length})
      </h3>

      <div className="relative border-l-2 border-slate-800 ml-4 pl-6 space-y-6">
        {events.map((e, idx) => (
          <div key={idx} className="relative group">
            {/* Circle Node */}
            <div className="absolute -left-[31px] top-0.5 p-1.5 rounded-full bg-slate-950 border border-slate-700 shadow-md">
              {getEventIcon(e.event_type, e.severity_level)}
            </div>

            <div>
              <div className="flex items-center gap-2 flex-wrap">
                <span className="text-xs text-slate-400 font-medium">
                  {new Date(e.event_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}
                </span>
                <span className="text-[10px] bg-slate-800 text-slate-300 font-bold px-2 py-0.5 rounded-md border border-slate-700">
                  {e.event_type}
                </span>
              </div>
              <h4 className="text-sm font-bold text-slate-100 mt-1">{e.title}</h4>
              <p className="text-xs text-slate-300 mt-0.5 leading-relaxed">{e.description}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
