/**
 * File: LifestylePanel.tsx
 * Purpose: Tabbed panel displaying Exercise, Sleep, Hydration, and Stress management guidance.
 * Module: Frontend / Components / Nutrition
 * Used By: NutritionPage Component
 * Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
 */

import React, { useState } from 'react';
import { Activity, Dumbbell, Moon, Heart } from 'lucide-react';
import { ExerciseCard, ExercisePlanItem } from './ExerciseCard';
import { SleepCard, SleepHygienePlan } from './SleepCard';

interface LifestylePanelProps {
  exercisePlans: ExercisePlanItem[];
  sleepPlan: SleepHygienePlan;
  stressPlan: any;
  overallSummary: string;
}

export const LifestylePanel: React.FC<LifestylePanelProps> = ({
  exercisePlans,
  sleepPlan,
  stressPlan,
  overallSummary,
}) => {
  const [activeTab, setActiveTab] = useState<'EXERCISE' | 'SLEEP' | 'STRESS'>('EXERCISE');

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between flex-wrap gap-2 mb-4 border-b border-slate-800 pb-3">
        <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
          <Activity className="w-5 h-5 text-teal-400" /> Lifestyle & Physical Activity Guidance
        </h3>
        <p className="text-xs text-slate-400">{overallSummary}</p>
      </div>

      {/* Tabs */}
      <div className="flex items-center gap-2 mb-4">
        <button
          onClick={() => setActiveTab('EXERCISE')}
          className={`px-4 py-2 rounded-xl text-xs font-semibold transition-all flex items-center gap-1.5 ${
            activeTab === 'EXERCISE'
              ? 'bg-teal-500 text-slate-950 font-bold shadow-md shadow-teal-500/20'
              : 'bg-slate-950 border border-slate-800 text-slate-400 hover:text-slate-200'
          }`}
        >
          <Dumbbell className="w-3.5 h-3.5" /> Exercise Plan ({exercisePlans.length})
        </button>

        <button
          onClick={() => setActiveTab('SLEEP')}
          className={`px-4 py-2 rounded-xl text-xs font-semibold transition-all flex items-center gap-1.5 ${
            activeTab === 'SLEEP'
              ? 'bg-teal-500 text-slate-950 font-bold shadow-md shadow-teal-500/20'
              : 'bg-slate-950 border border-slate-800 text-slate-400 hover:text-slate-200'
          }`}
        >
          <Moon className="w-3.5 h-3.5" /> Sleep Hygiene
        </button>

        <button
          onClick={() => setActiveTab('STRESS')}
          className={`px-4 py-2 rounded-xl text-xs font-semibold transition-all flex items-center gap-1.5 ${
            activeTab === 'STRESS'
              ? 'bg-teal-500 text-slate-950 font-bold shadow-md shadow-teal-500/20'
              : 'bg-slate-950 border border-slate-800 text-slate-400 hover:text-slate-200'
          }`}
        >
          <Heart className="w-3.5 h-3.5" /> Stress & Recovery
        </button>
      </div>

      {/* Active Tab Content */}
      {activeTab === 'EXERCISE' && <ExerciseCard exercisePlans={exercisePlans} />}
      {activeTab === 'SLEEP' && <SleepCard sleepPlan={sleepPlan} />}
      {activeTab === 'STRESS' && stressPlan && (
        <div className="bg-slate-950/70 border border-slate-800 rounded-xl p-5 text-xs space-y-2">
          <h4 className="font-bold text-slate-100 text-sm flex items-center gap-2">
            <Heart className="w-4 h-4 text-rose-400" /> {stressPlan.technique_name}
          </h4>
          <p className="text-teal-400 font-semibold text-[11px]">Frequency: {stressPlan.practice_frequency}</p>
          <p className="text-slate-300 text-[11px] leading-relaxed">{stressPlan.autonomic_mechanism}</p>
          <p className="text-slate-400 text-[10px] italic">{stressPlan.recovery_guidance}</p>
        </div>
      )}
    </div>
  );
};
