/**
 * File: MealSuggestions.tsx
 * Purpose: Circadian meal timing & distribution component.
 * Module: Frontend / Components / Nutrition
 * Used By: NutritionPage Component
 * Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
 */

import React from 'react';
import { Clock, Sun, Sunrise, Sunset } from 'lucide-react';

export interface MealScheduleItem {
  meal_name: string;
  recommended_time_window: string;
  macronutrient_focus: string;
  circadian_rationale: string;
}

export interface CircadianMealGuidance {
  overnight_fasting_window: string;
  meals: MealScheduleItem[];
  key_principle: string;
}

interface MealSuggestionsProps {
  mealPatterns: CircadianMealGuidance;
}

export const MealSuggestions: React.FC<MealSuggestionsProps> = ({ mealPatterns }) => {
  const getMealIcon = (idx: number) => {
    if (idx === 0) return <Sunrise className="w-4 h-4 text-amber-400" />;
    if (idx === 1) return <Sun className="w-4 h-4 text-teal-400" />;
    return <Sunset className="w-4 h-4 text-indigo-400" />;
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between flex-wrap gap-2 mb-4 border-b border-slate-800 pb-3">
        <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
          <Clock className="w-5 h-5 text-teal-400" /> Circadian Meal Timing & Window
        </h3>
        <span className="text-xs text-amber-300 bg-amber-950/60 border border-amber-500/30 px-3 py-1 rounded-full font-bold">
          Window: {mealPatterns.overnight_fasting_window}
        </span>
      </div>

      <p className="text-xs text-slate-300 mb-4 bg-slate-950/60 p-3 rounded-xl border border-slate-800 leading-relaxed">
        {mealPatterns.key_principle}
      </p>

      <div className="grid md:grid-cols-3 gap-4">
        {mealPatterns.meals.map((meal, idx) => (
          <div key={idx} className="bg-slate-950/70 border border-slate-800 rounded-xl p-4 text-xs space-y-2">
            <div className="flex items-center gap-2 font-bold text-slate-100 text-sm">
              {getMealIcon(idx)}
              <h4>{meal.meal_name}</h4>
            </div>
            <div className="text-teal-400 font-semibold text-[11px]">{meal.recommended_time_window}</div>
            <p className="text-slate-300 text-[11px] leading-relaxed">
              <strong className="text-slate-200">Focus:</strong> {meal.macronutrient_focus}
            </p>
            <p className="text-slate-400 text-[10px] italic">{meal.circadian_rationale}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
