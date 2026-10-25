/**
 * File: SleepCard.tsx
 * Purpose: Sleep hygiene, bedtime window, and circadian light exposure guidance card.
 * Module: Frontend / Components / Nutrition
 * Used By: LifestylePanel Component
 * Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
 */

import React from 'react';
import { Moon, CheckCircle2 } from 'lucide-react';

export interface SleepHygieneItem {
  habit_title: string;
  recommendation: string;
  circadian_mechanism: string;
}

export interface SleepHygienePlan {
  target_sleep_duration_hours: string;
  recommended_bedtime_window: string;
  habits: SleepHygieneItem[];
}

interface SleepCardProps {
  sleepPlan: SleepHygienePlan;
}

export const SleepCard: React.FC<SleepCardProps> = ({ sleepPlan }) => {
  return (
    <div className="bg-slate-950/70 border border-slate-800 rounded-xl p-5 text-xs space-y-4">
      <div className="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
        <div className="flex items-center gap-2 font-bold text-slate-100 text-sm">
          <Moon className="w-4 h-4 text-indigo-400" />
          <h4>Sleep Duration & Circadian Bedtime Window</h4>
        </div>
        <span className="text-[10px] text-indigo-300 bg-indigo-950/60 border border-indigo-500/30 px-3 py-1 rounded-full font-bold">
          Target: {sleepPlan.target_sleep_duration_hours} ({sleepPlan.recommended_bedtime_window})
        </span>
      </div>

      <div className="space-y-3">
        {sleepPlan.habits.map((h, idx) => (
          <div key={idx} className="bg-slate-900/80 p-3 rounded-lg border border-slate-800 space-y-1">
            <h5 className="font-bold text-slate-200 text-xs flex items-center gap-1.5">
              <CheckCircle2 className="w-3.5 h-3.5 text-teal-400" /> {h.habit_title}
            </h5>
            <p className="text-slate-300 text-[11px] leading-relaxed">{h.recommendation}</p>
            <p className="text-[10px] text-slate-400 italic">{h.circadian_mechanism}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
