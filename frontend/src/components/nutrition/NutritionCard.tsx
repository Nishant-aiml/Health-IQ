/**
 * File: NutritionCard.tsx
 * Purpose: Displays categorized food guidance (Increase, Reduce, Maintain, Monitor) with supporting evidence citations.
 * Module: Frontend / Components / Nutrition
 * Used By: NutritionPage Component
 * Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
 */

import React from 'react';
import { Apple, ArrowUpRight, ArrowDownRight, Minus, AlertTriangle, ShieldCheck } from 'lucide-react';

export interface NutritionRecommendationItem {
  action: 'INCREASE' | 'REDUCE' | 'MAINTAIN' | 'MONITOR';
  target_food_or_group: string;
  category: string;
  reasoning: string;
  biomarker_trigger: string;
  supporting_evidence: string;
  limitations: string;
  priority: string;
}

interface NutritionCardProps {
  recommendations: NutritionRecommendationItem[];
  overallFocus: string;
}

export const NutritionCard: React.FC<NutritionCardProps> = ({ recommendations, overallFocus }) => {
  const getActionBadge = (action: string) => {
    switch (action) {
      case 'INCREASE':
        return (
          <span className="bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1">
            <ArrowUpRight className="w-3.5 h-3.5" /> INCREASE
          </span>
        );
      case 'REDUCE':
        return (
          <span className="bg-rose-500/20 text-rose-300 border border-rose-500/30 px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1">
            <ArrowDownRight className="w-3.5 h-3.5" /> REDUCE / LIMIT
          </span>
        );
      case 'MONITOR':
        return (
          <span className="bg-amber-500/20 text-amber-300 border border-amber-500/30 px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1">
            <AlertTriangle className="w-3.5 h-3.5" /> MONITOR
          </span>
        );
      default:
        return (
          <span className="bg-slate-800 text-slate-300 border border-slate-700 px-2.5 py-1 rounded-lg text-xs font-bold flex items-center gap-1">
            <Minus className="w-3.5 h-3.5" /> MAINTAIN
          </span>
        );
    }
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between flex-wrap gap-2 mb-4 border-b border-slate-800 pb-3">
        <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
          <Apple className="w-5 h-5 text-teal-400" /> Evidence-Based Nutrition Guidance
        </h3>
        <span className="text-xs text-teal-300 bg-teal-950/60 border border-teal-500/30 px-3 py-1 rounded-full font-bold">
          Focus: {overallFocus}
        </span>
      </div>

      <div className="space-y-3">
        {recommendations.map((rec, idx) => (
          <div key={idx} className="bg-slate-950/60 border border-slate-800 rounded-xl p-4 text-xs">
            <div className="flex items-center justify-between flex-wrap gap-2 mb-2">
              <div className="flex items-center gap-2">
                {getActionBadge(rec.action)}
                <h4 className="text-sm font-bold text-slate-100">{rec.target_food_or_group}</h4>
              </div>
              <span className="text-[10px] text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">
                Triggered by: {rec.biomarker_trigger}
              </span>
            </div>

            <p className="text-slate-300 mt-1 leading-relaxed">{rec.reasoning}</p>

            <div className="mt-3 pt-2 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400 flex-wrap gap-2">
              <span className="flex items-center gap-1 text-teal-400 font-medium">
                <ShieldCheck className="w-3.5 h-3.5" /> {rec.supporting_evidence}
              </span>
              <span className="italic">{rec.limitations}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
