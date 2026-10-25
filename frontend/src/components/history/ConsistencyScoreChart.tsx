/**
 * File: ConsistencyScoreChart.tsx
 * Purpose: Recharts AreaChart displaying biomarker health consistency percentage over time.
 * Module: Frontend / Components / History
 * Used By: HistoryPage Component
 * Future Phase: Phase 3B Longitudinal Health Intelligence
 */

import React from 'react';
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import { ShieldCheck } from 'lucide-react';

interface ReportItem {
  id: number;
  collection_date: string;
  total_parameters: number;
  abnormal_parameters_count: number;
}

interface ConsistencyScoreChartProps {
  reports: ReportItem[];
}

export const ConsistencyScoreChart: React.FC<ConsistencyScoreChartProps> = ({ reports }) => {
  const chartData = reports.map((r) => {
    const total = r.total_parameters || 1;
    const healthy = Math.max(0, total - r.abnormal_parameters_count);
    const percentage = Math.round((healthy / total) * 100);
    return {
      date: new Date(r.collection_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
      consistency: percentage,
    };
  });

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl mb-6">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-base font-bold text-slate-100 flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-indigo-400" /> Biomarker Health Consistency Index
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Percentage of lab biomarkers remaining strictly within standard reference intervals.
          </p>
        </div>
      </div>

      <div className="h-48 w-full pt-2">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={chartData} margin={{ top: 10, right: 20, left: -20, bottom: 0 }}>
            <defs>
              <linearGradient id="colorConsistency" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#6366f1" stopOpacity={0.4} />
                <stop offset="95%" stopColor="#6366f1" stopOpacity={0.0} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
            <XAxis dataKey="date" stroke="#64748b" fontSize={11} />
            <YAxis domain={[0, 100]} stroke="#64748b" fontSize={11} />
            <Tooltip
              contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
              labelStyle={{ color: '#94a3b8', fontWeight: 'bold' }}
            />
            <Area
              type="monotone"
              dataKey="consistency"
              stroke="#6366f1"
              strokeWidth={3}
              fillOpacity={1}
              fill="url(#colorConsistency)"
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
