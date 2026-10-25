/* --------------------------------------------------
 * File: HealthScoreGauge.tsx
 * Purpose: Transparent 0-100 Health Score visualization component with penalty breakdown modal/drawer.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2B Results Dashboard
 * -------------------------------------------------- */

import React, { useState } from 'react';
import { Card } from '../ui/Card';
import { Info, HelpCircle } from 'lucide-react';

interface PenaltyItem {
  parameter_name: string;
  severity: string;
  points_deducted: number;
}

interface HealthScoreGaugeProps {
  score: number;
  summary: string;
  penalties?: PenaltyItem[];
}

export const HealthScoreGauge: React.FC<HealthScoreGaugeProps> = ({
  score,
  summary,
  penalties = [],
}) => {
  const [showExplanation, setShowExplanation] = useState(false);

  const getScoreColor = (val: number) => {
    if (val >= 90) return 'text-emerald-600 dark:text-emerald-400 stroke-emerald-500';
    if (val >= 75) return 'text-teal-600 dark:text-teal-400 stroke-teal-500';
    if (val >= 60) return 'text-amber-600 dark:text-amber-400 stroke-amber-500';
    return 'text-rose-600 dark:text-rose-400 stroke-rose-500';
  };

  const getScoreBadge = (val: number) => {
    if (val >= 90) return 'Optimal Health Baseline';
    if (val >= 75) return 'Good Health Baseline';
    if (val >= 60) return 'Moderate Parameter Risk';
    return 'Attention Required';
  };

  const circumference = 2 * Math.PI * 45;
  const strokeDashoffset = circumference - (score / 100) * circumference;

  return (
    <Card className="relative overflow-hidden">
      <div className="flex flex-col sm:flex-row items-center sm:items-start justify-between space-y-4 sm:space-y-0 sm:space-x-6">
        <div className="flex flex-col items-center sm:items-start text-center sm:text-left space-y-2 max-w-md">
          <div className="inline-flex items-center px-3 py-1 rounded-full bg-brand-50 dark:bg-brand-950/40 text-brand-700 dark:text-brand-300 text-xs font-semibold">
            <span>{getScoreBadge(score)}</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-slate-100 tracking-tight">
            Lab Health Score
          </h2>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
            {summary}
          </p>
          <button
            onClick={() => setShowExplanation(!showExplanation)}
            className="inline-flex items-center text-xs font-medium text-brand-600 dark:text-brand-400 hover:underline min-h-[44px]"
          >
            <HelpCircle className="w-3.5 h-3.5 mr-1" /> How is this calculated?
          </button>
        </div>

        <div className="relative flex-shrink-0 flex flex-col items-center justify-center">
          <svg className="w-32 h-32 sm:w-36 sm:h-36 transform -rotate-90" viewBox="0 0 100 100">
            <circle
              cx="50"
              cy="50"
              r="45"
              className="stroke-slate-100 dark:stroke-slate-800"
              strokeWidth="8"
              fill="transparent"
            />
            <circle
              cx="50"
              cy="50"
              r="45"
              className={`transition-all duration-1000 ease-out ${getScoreColor(score)}`}
              strokeWidth="8"
              strokeDasharray={circumference}
              strokeDashoffset={strokeDashoffset}
              strokeLinecap="round"
              fill="transparent"
            />
          </svg>
          <div className="absolute flex flex-col items-center justify-center text-center">
            <span className={`text-3xl sm:text-4xl font-black ${getScoreColor(score).split(' ')[0]}`}>
              {score}
            </span>
            <span className="text-[10px] uppercase font-bold text-slate-400">out of 100</span>
          </div>
        </div>
      </div>

      {showExplanation && (
        <div className="mt-4 pt-4 border-t border-slate-100 dark:border-slate-800 text-xs space-y-2 bg-slate-50 dark:bg-slate-800/40 p-4 rounded-2xl animate-fade-in">
          <div className="flex items-center text-slate-700 dark:text-slate-300 font-bold">
            <Info className="w-4 h-4 mr-1 text-brand-500" /> Transparent Score Formula
          </div>
          <p className="text-slate-500 dark:text-slate-400">
            Calculated from a base of 100, deducting points based on parameter severity (Mild -5, Moderate -12, Severe -25, Critical -35).
          </p>
          {penalties.length > 0 ? (
            <div className="space-y-1 pt-1">
              <span className="font-semibold text-slate-700 dark:text-slate-300">Point Deductions:</span>
              <ul className="space-y-1">
                {penalties.map((p, idx) => (
                  <li key={idx} className="flex justify-between text-slate-600 dark:text-slate-400">
                    <span>{p.parameter_name} ({p.severity})</span>
                    <span className="font-semibold text-rose-600 dark:text-rose-400">-{p.points_deducted} pts</span>
                  </li>
                ))}
              </ul>
            </div>
          ) : (
            <p className="text-emerald-600 dark:text-emerald-400 font-semibold">Zero deductions — all parameters in range.</p>
          )}
        </div>
      )}
    </Card>
  );
};
