/**
 * File: HydrationCard.tsx
 * Purpose: Displays personalized fluid intake targets, fluid pacing, and urine color indicator.
 * Module: Frontend / Components / Nutrition
 * Used By: NutritionPage Component
 * Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
 */

import React from 'react';
import { Droplet, Info, CheckCircle2 } from 'lucide-react';

export interface HydrationGuidanceTarget {
  daily_volume_liters: number;
  daily_glasses_count: number;
  pacing_guideline: string;
  urine_color_target: string;
  electrolyte_advice: string;
  clinical_note: string;
}

interface HydrationCardProps {
  hydration: HydrationGuidanceTarget;
}

export const HydrationCard: React.FC<HydrationCardProps> = ({ hydration }) => {
  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between flex-wrap gap-2 mb-4 border-b border-slate-800 pb-3">
        <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
          <Droplet className="w-5 h-5 text-sky-400" /> Daily Hydration Target & Pacing
        </h3>
        <span className="text-xs text-sky-300 bg-sky-950/60 border border-sky-500/30 px-3 py-1 rounded-full font-bold">
          Target: {hydration.daily_volume_liters} Liters ({hydration.daily_glasses_count} Glasses)
        </span>
      </div>

      <div className="grid md:grid-cols-2 gap-6 items-center">
        {/* Hydration Meter */}
        <div className="bg-slate-950/70 p-4 rounded-xl border border-slate-800 space-y-3">
          <div className="flex items-center justify-between text-xs">
            <span className="text-slate-300 font-semibold">Daily Fluid Goal</span>
            <span className="text-sky-300 font-bold">{hydration.daily_volume_liters} L / day</span>
          </div>

          <div className="w-full bg-slate-900 h-3.5 rounded-full overflow-hidden p-0.5 border border-slate-800">
            <div className="bg-gradient-to-r from-sky-500 to-teal-400 h-full rounded-full w-[85%] animate-pulse" />
          </div>

          <div className="flex items-center gap-2 text-[11px] text-slate-400">
            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 shrink-0" />
            <span>Target Urine Color: <strong>{hydration.urine_color_target}</strong></span>
          </div>
        </div>

        {/* Pacing & Electrolyte Advice */}
        <div className="space-y-2 text-xs text-slate-300">
          <div className="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <strong className="text-slate-200 block mb-0.5">Pacing Guideline:</strong>
            <p className="text-[11px] text-slate-400 leading-relaxed">{hydration.pacing_guideline}</p>
          </div>

          <div className="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <strong className="text-slate-200 block mb-0.5">Electrolyte Balance:</strong>
            <p className="text-[11px] text-slate-400 leading-relaxed">{hydration.electrolyte_advice}</p>
          </div>
        </div>
      </div>

      <p className="text-[11px] text-slate-400 mt-4 pt-2 border-t border-slate-800/80 flex items-center gap-1.5">
        <Info className="w-3.5 h-3.5 text-slate-500 shrink-0" /> {hydration.clinical_note}
      </p>
    </div>
  );
};
