/**
 * File: HealthScoreHistory.tsx
 * Purpose: Recharts LineChart displaying overall 0-100 Health Score trajectory across historical reports.
 * Module: Frontend / Components / History
 * Used By: HistoryPage Component
 * Future Phase: Phase 3B Longitudinal Health Intelligence
 */

import React from 'react';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import { Activity, TrendingUp } from 'lucide-react';

export interface ReportItem {
  id: number;
  source_filename: string;
  collection_date: string;
  health_score: number;
  total_parameters: number;
  abnormal_parameters_count: number;
}

interface HealthScoreHistoryProps {
  reports: ReportItem[];
}

export const HealthScoreHistory: React.FC<HealthScoreHistoryProps> = ({ reports }) => {
  const chartData = reports.map((r) => ({
    date: new Date(r.collection_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
    score: r.health_score,
    name: r.source_filename,
  }));

  const latestScore = reports.length > 0 ? reports[reports.length - 1].health_score : 100;
  const firstScore = reports.length > 0 ? reports[0].health_score : 100;
  const scoreDelta = Math.round(latestScore - firstScore);

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl mb-6">
      <div className="flex items-center justify-between flex-wrap gap-2 mb-4">
        <div>
          <h3 className="text-base font-bold text-slate-100 flex items-center gap-2">
            <Activity className="w-5 h-5 text-teal-400" /> Overall Health Score Trajectory
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Transparent 0-100 Health Score evolution across {reports.length} report(s).
          </p>
        </div>

        <div className="flex items-center gap-2 bg-slate-950 px-3 py-1.5 rounded-xl border border-slate-800 text-xs">
          <span className="text-slate-400">Net Trajectory:</span>
          <span className={`font-bold flex items-center gap-1 ${scoreDelta >= 0 ? 'text-emerald-400' : 'text-rose-400'}`}>
            <TrendingUp className="w-3.5 h-3.5" /> {scoreDelta >= 0 ? `+${scoreDelta} pts` : `${scoreDelta} pts`}
          </span>
        </div>
      </div>

      <div className="h-56 w-full pt-2">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={chartData} margin={{ top: 10, right: 20, left: -20, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
            <XAxis dataKey="date" stroke="#64748b" fontSize={11} />
            <YAxis domain={[0, 100]} stroke="#64748b" fontSize={11} />
            <Tooltip
              contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
              labelStyle={{ color: '#94a3b8', fontWeight: 'bold' }}
            />
            <Line
              type="monotone"
              dataKey="score"
              stroke="#0d9488"
              strokeWidth={3}
              dot={{ r: 5, fill: '#14b8a6', strokeWidth: 2, stroke: '#0f172a' }}
              activeDot={{ r: 7, fill: '#2dd4bf' }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
