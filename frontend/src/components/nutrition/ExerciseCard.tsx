/**
 * File: ExerciseCard.tsx
 * Purpose: Tailored physical activity & exercise card with intensity and physiological rationale.
 * Module: Frontend / Components / Nutrition
 * Used By: LifestylePanel Component
 * Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
 */

import React from 'react';
import { Dumbbell, AlertCircle } from 'lucide-react';

export interface ExercisePlanItem {
  activity_name: string;
  frequency_weekly: string;
  duration_minutes_per_session: number;
  intensity_level: string;
  physiological_rationale: string;
  safety_precautions: string;
  evidence_source: string;
}

interface ExerciseCardProps {
  exercisePlans: ExercisePlanItem[];
}

export const ExerciseCard: React.FC<ExerciseCardProps> = ({ exercisePlans }) => {
  return (
    <div className="space-y-4">
      {exercisePlans.map((ex, idx) => (
        <div key={idx} className="bg-slate-950/70 border border-slate-800 rounded-xl p-4 text-xs space-y-2">
          <div className="flex items-center justify-between flex-wrap gap-2">
            <div className="flex items-center gap-2 font-bold text-slate-100 text-sm">
              <Dumbbell className="w-4 h-4 text-indigo-400" />
              <h4>{ex.activity_name}</h4>
            </div>
            <span className="text-[10px] bg-indigo-950/60 text-indigo-300 border border-indigo-500/30 px-2.5 py-0.5 rounded-full font-bold">
              {ex.intensity_level}
            </span>
          </div>

          <div className="flex items-center gap-4 text-slate-300 font-semibold text-[11px]">
            <span>Frequency: {ex.frequency_weekly}</span>
            <span>Duration: {ex.duration_minutes_per_session} mins / session</span>
          </div>

          <p className="text-slate-300 leading-relaxed text-[11px]">{ex.physiological_rationale}</p>

          <div className="flex items-center gap-1.5 text-[10px] text-amber-300 bg-slate-900 p-2 rounded-lg border border-slate-800">
            <AlertCircle className="w-3.5 h-3.5 text-amber-400 shrink-0" />
            <span>Precaution: {ex.safety_precautions}</span>
          </div>
        </div>
      ))}
    </div>
  );
};
