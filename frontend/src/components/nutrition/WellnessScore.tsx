/**
 * File: WellnessScore.tsx
 * Purpose: Recharts Wellness Radar & composite Wellness Score breakdown visualizer.
 * Module: Frontend / Components / Nutrition
 * Used By: NutritionPage Component
 * Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
 */

import React from 'react';
import { ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, Tooltip } from 'recharts';
import { Sparkles, HeartPulse } from 'lucide-react';

export interface WellnessScoreBreakdown {
  health_score_reused: number;
  nutrition_score: number;
  lifestyle_score: number;
  hydration_score: number;
  sleep_score: number;
  overall_wellness_score: number;
  formula_explanation: string;
}

interface WellnessScoreProps {
  wellness: WellnessScoreBreakdown;
}

export const WellnessScore: React.FC<WellnessScoreProps> = ({ wellness }) => {
  const radarData = [
    { subject: 'Health Baseline', score: wellness.health_score_reused, fullMark: 100 },
    { subject: 'Nutrition', score: wellness.nutrition_score, fullMark: 100 },
    { subject: 'Lifestyle', score: wellness.lifestyle_score, fullMark: 100 },
    { subject: 'Hydration', score: wellness.hydration_score, fullMark: 100 },
    { subject: 'Sleep', score: wellness.sleep_score, fullMark: 100 },
  ];

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between flex-wrap gap-4 mb-4 border-b border-slate-800 pb-4">
        <div>
          <h2 className="text-xl font-extrabold text-slate-100 flex items-center gap-2">
            <HeartPulse className="w-6 h-6 text-teal-400" /> Overall Wellness Score & Radar
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">{wellness.formula_explanation}</p>
        </div>

        <div className="flex items-center gap-3 bg-gradient-to-r from-teal-950/80 to-indigo-950/80 px-5 py-2.5 rounded-2xl border border-teal-500/40">
          <Sparkles className="w-6 h-6 text-teal-300 animate-pulse" />
          <div>
            <span className="text-[10px] uppercase tracking-wider text-teal-300 font-bold block">Composite Score</span>
            <span className="text-2xl font-black text-slate-100">{wellness.overall_wellness_score} / 100</span>
          </div>
        </div>
      </div>

      <div className="grid md:grid-cols-2 gap-6 items-center">
        {/* Recharts Radar */}
        <div className="h-60 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <RadarChart cx="50%" cy="50%" outerRadius="75%" data={radarData}>
              <PolarGrid stroke="#1e293b" />
              <PolarAngleAxis dataKey="subject" stroke="#94a3b8" fontSize={11} />
              <PolarRadiusAxis angle={30} domain={[0, 100]} stroke="#475569" fontSize={9} />
              <Radar name="Wellness Score" dataKey="score" stroke="#0d9488" fill="#14b8a6" fillOpacity={0.4} />
              <Tooltip contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }} />
            </RadarChart>
          </ResponsiveContainer>
        </div>

        {/* Breakdown Metric Cards */}
        <div className="grid grid-cols-2 gap-3 text-xs">
          <div className="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <span className="text-slate-400 block text-[11px]">Health Baseline</span>
            <span className="font-bold text-slate-100 text-base">{wellness.health_score_reused}</span>
            <span className="text-[10px] text-teal-400 block font-semibold mt-0.5">Phase 2B Baseline</span>
          </div>

          <div className="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <span className="text-slate-400 block text-[11px]">Nutrition Score</span>
            <span className="font-bold text-teal-300 text-base">{wellness.nutrition_score}</span>
            <span className="text-[10px] text-slate-400 block font-semibold mt-0.5">Food Quality</span>
          </div>

          <div className="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <span className="text-slate-400 block text-[11px]">Lifestyle Score</span>
            <span className="font-bold text-indigo-300 text-base">{wellness.lifestyle_score}</span>
            <span className="text-[10px] text-slate-400 block font-semibold mt-0.5">Physical Activity</span>
          </div>

          <div className="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <span className="text-slate-400 block text-[11px]">Hydration Score</span>
            <span className="font-bold text-sky-300 text-base">{wellness.hydration_score}</span>
            <span className="text-[10px] text-slate-400 block font-semibold mt-0.5">Fluid Target</span>
          </div>
        </div>
      </div>
    </div>
  );
};
