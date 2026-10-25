/**
 * File: TrendChart.tsx
 * Purpose: Recharts LineChart for individual canonical biomarker historical trends with reference range bands.
 * Module: Frontend / Components / History
 * Used By: HistoryPage Component
 * Future Phase: Phase 3B Longitudinal Health Intelligence
 */

import React from 'react';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ReferenceArea } from 'recharts';
import { TrendingUp, TrendingDown, Minus, AlertCircle, CheckCircle2 } from 'lucide-react';

export interface ParameterReading {
  report_id: number;
  collection_date: string;
  value: number;
  unit: string;
  reference_range_low?: number;
  reference_range_high?: number;
  severity: string;
}

export interface BiomarkerTrendPayload {
  canonical_name: string;
  unit: string;
  trend: {
    direction: string;
    trend_confidence: string;
    percentage_change: number;
    clinical_summary: string;
  };
  statistics: {
    mean_value: number;
    min_value: number;
    max_value: number;
    std_dev: number;
    variability_index: number;
    variability_level: string;
  };
  readings: ParameterReading[];
}

interface TrendChartProps {
  biomarkerTrend: BiomarkerTrendPayload;
}

export const TrendChart: React.FC<TrendChartProps> = ({ biomarkerTrend }) => {
  const { canonical_name, unit, trend, statistics, readings } = biomarkerTrend;

  const chartData = readings.map((r) => ({
    date: new Date(r.collection_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
    value: r.value,
  }));

  const refLow = readings.length > 0 && readings[0].reference_range_low ? readings[0].reference_range_low : null;
  const refHigh = readings.length > 0 && readings[0].reference_range_high ? readings[0].reference_range_high : null;

  const getDirectionBadge = () => {
    switch (trend.direction) {
      case 'recovery':
        return (
          <span className="bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 px-2.5 py-0.5 rounded-full text-xs font-bold flex items-center gap-1">
            <CheckCircle2 className="w-3.5 h-3.5" /> RECOVERY
          </span>
        );
      case 'persistent_abnormality':
        return (
          <span className="bg-rose-500/20 text-rose-300 border border-rose-500/40 px-2.5 py-0.5 rounded-full text-xs font-bold flex items-center gap-1">
            <AlertCircle className="w-3.5 h-3.5" /> PERSISTENT ABNORMALITY
          </span>
        );
      case 'increasing':
        return (
          <span className="bg-amber-500/20 text-amber-300 border border-amber-500/40 px-2.5 py-0.5 rounded-full text-xs font-bold flex items-center gap-1">
            <TrendingUp className="w-3.5 h-3.5" /> INCREASING (+{trend.percentage_change}%)
          </span>
        );
      case 'decreasing':
        return (
          <span className="bg-sky-500/20 text-sky-300 border border-sky-500/40 px-2.5 py-0.5 rounded-full text-xs font-bold flex items-center gap-1">
            <TrendingDown className="w-3.5 h-3.5" /> DECREASING ({trend.percentage_change}%)
          </span>
        );
      default:
        return (
          <span className="bg-slate-800 text-slate-300 border border-slate-700 px-2.5 py-0.5 rounded-full text-xs font-bold flex items-center gap-1">
            <Minus className="w-3.5 h-3.5" /> STABLE
          </span>
        );
    }
  };

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 mb-5 shadow-lg">
      <div className="flex items-center justify-between flex-wrap gap-2 mb-3">
        <div>
          <div className="flex items-center gap-2">
            <h4 className="text-base font-bold text-slate-100">{canonical_name}</h4>
            <span className="text-xs text-slate-400">({unit})</span>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">{trend.clinical_summary}</p>
        </div>
        <div>{getDirectionBadge()}</div>
      </div>

      {/* Quick Statistics Row */}
      <div className="grid grid-cols-4 gap-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-[11px] mb-3 text-center">
        <div>
          <span className="text-slate-400 block">Mean</span>
          <span className="font-bold text-slate-200">{statistics.mean_value}</span>
        </div>
        <div>
          <span className="text-slate-400 block">Range</span>
          <span className="font-bold text-slate-200">{statistics.min_value} - {statistics.max_value}</span>
        </div>
        <div>
          <span className="text-slate-400 block">Std Dev</span>
          <span className="font-bold text-slate-200">±{statistics.std_dev}</span>
        </div>
        <div>
          <span className="text-slate-400 block">Variability</span>
          <span className="font-bold text-teal-300">{statistics.variability_index}% ({statistics.variability_level})</span>
        </div>
      </div>

      {/* Recharts Visualizer */}
      <div className="h-44 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={chartData} margin={{ top: 10, right: 15, left: -20, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
            <XAxis dataKey="date" stroke="#64748b" fontSize={11} />
            <YAxis stroke="#64748b" fontSize={11} />
            <Tooltip
              contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
              labelStyle={{ color: '#94a3b8', fontWeight: 'bold' }}
            />
            {refLow !== null && refHigh !== null && (
              <ReferenceArea y1={refLow} y2={refHigh} fill="#0d9488" fillOpacity={0.1} />
            )}
            <Line
              type="monotone"
              dataKey="value"
              stroke="#2dd4bf"
              strokeWidth={2.5}
              dot={{ r: 4, fill: '#14b8a6' }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
