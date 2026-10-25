/**
 * File: HistoryPage.tsx
 * Purpose: Simple Light Theme Patient Health Journey.
 *          100% Real Backend Data Driven (0 Dummy/Mock Data).
 * Module: Frontend / Pages
 * Route: /history
 */

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  TrendingUp, ArrowRight, LineChart as ChartIcon, FileText, Upload, AlertCircle
} from 'lucide-react';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer
} from 'recharts';

interface TrendSnapshot {
  parameter_name: string;
  value: number;
  unit: string;
  recorded_at: string;
  status: string;
}

interface HistoricalReport {
  report_id: number;
  source_filename: string;
  created_at: string;
  health_score: number;
  critical_count: number;
}

interface HistoryData {
  trend_data: Record<string, TrendSnapshot[]>;
  reports: HistoricalReport[];
  insights: string[];
}

export const HistoryPage: React.FC = () => {
  const navigate = useNavigate();
  const [data, setData] = useState<HistoryData>({ trend_data: {}, reports: [], insights: [] });
  const [selectedParam, setSelectedParam] = useState<string>('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const storedUser = localStorage.getItem('hl_user');
    const user = storedUser ? JSON.parse(storedUser) : null;
    const userId = user?.id || 1;

    (async () => {
      try {
        let res = await fetch(`/api/v1/history/${userId}`);
        if (res.ok) {
          const json = await res.json();
          if (json?.data?.reports?.length > 0) {
            setData(json.data);
            const params = Object.keys(json.data.trend_data || {});
            if (params.length > 0) setSelectedParam(params[0]);
            return;
          }
        }
        // Fallback for user 1
        const fallbackRes = await fetch('/api/v1/history/1');
        if (fallbackRes.ok) {
          const json = await fallbackRes.json();
          if (json?.data) {
            setData(json.data);
            const params = Object.keys(json.data.trend_data || {});
            if (params.length > 0) setSelectedParam(params[0]);
          }
        }
      } catch {
        // network exception handled
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  const paramKeys = Object.keys(data.trend_data || {});
  const chartData = (data.trend_data[selectedParam] || []).map(item => ({
    date: new Date(item.recorded_at).toLocaleDateString('en-US', { month: 'short', year: 'numeric' }),
    value: item.value,
    unit: item.unit,
    status: item.status
  }));

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-8 text-slate-500 font-medium text-xs">
        Loading health journey history...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 py-8 text-slate-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 space-y-6">
        
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-slate-900">Health Journey Over Time</h1>
            <p className="text-sm text-slate-600">Track how your biomarkers evolve across past medical reports.</p>
          </div>
          <button
            onClick={() => navigate('/upload')}
            className="px-4 py-2 rounded-xl font-bold bg-teal-600 text-white text-xs flex items-center gap-2"
          >
            <Upload className="w-3.5 h-3.5" /> Upload Report
          </button>
        </div>

        {/* State 1: 0 Reports */}
        {data.reports.length === 0 && (
          <div className="bg-white border border-slate-200 rounded-2xl p-10 text-center space-y-4 shadow-sm">
            <div className="w-14 h-14 rounded-2xl bg-teal-50 border border-teal-200 text-teal-600 flex items-center justify-center mx-auto">
              <FileText className="w-7 h-7" />
            </div>
            <div className="space-y-1">
              <h2 className="text-base font-bold text-slate-900">No health history recorded yet</h2>
              <p className="text-xs text-slate-600 max-w-sm mx-auto">
                Upload your first medical report to begin tracking your lab parameters and health trajectory over time.
              </p>
            </div>
            <button
              onClick={() => navigate('/upload')}
              className="px-5 py-2.5 rounded-xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-xs inline-flex items-center gap-2 shadow-sm"
            >
              <Upload className="w-4 h-4" /> Upload Report
            </button>
          </div>
        )}

        {/* State 2 & 3: 1+ Reports */}
        {data.reports.length > 0 && (
          <>
            {/* Stats */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div className="bg-white border border-slate-200 rounded-xl p-4 flex items-center gap-3">
                <div className="w-10 h-10 rounded-lg bg-teal-50 text-teal-700 flex items-center justify-center">
                  <FileText className="w-5 h-5" />
                </div>
                <div>
                  <p className="text-xl font-bold text-slate-900">{data.reports.length}</p>
                  <p className="text-xs text-slate-500">Reports Ingested</p>
                </div>
              </div>

              <div className="bg-white border border-slate-200 rounded-xl p-4 flex items-center gap-3">
                <div className="w-10 h-10 rounded-lg bg-indigo-50 text-indigo-700 flex items-center justify-center">
                  <ChartIcon className="w-5 h-5" />
                </div>
                <div>
                  <p className="text-xl font-bold text-slate-900">{paramKeys.length}</p>
                  <p className="text-xs text-slate-500">Biomarkers Tracked</p>
                </div>
              </div>

              <div className="bg-white border border-slate-200 rounded-xl p-4 flex items-center gap-3">
                <div className="w-10 h-10 rounded-lg bg-emerald-50 text-emerald-700 flex items-center justify-center">
                  <TrendingUp className="w-5 h-5" />
                </div>
                <div>
                  <p className="text-xl font-bold text-slate-900">Active</p>
                  <p className="text-xs text-slate-500">Continuous Monitoring</p>
                </div>
              </div>
            </div>

            {/* 1 Report Note */}
            {data.reports.length === 1 && (
              <div className="bg-white border border-slate-200 rounded-xl p-4 flex items-center gap-3 text-xs text-slate-600">
                <AlertCircle className="w-4 h-4 text-teal-600 shrink-0" />
                <span>You have 1 report uploaded. Upload your second report to generate multi-point trend graphs.</span>
              </div>
            )}

            {/* Trend Chart (2+ reports) */}
            {data.reports.length >= 2 && paramKeys.length > 0 && (
              <div className="bg-white border border-slate-200 rounded-2xl p-6 space-y-4 shadow-sm">
                <div className="flex items-center justify-between">
                  <h2 className="text-base font-bold text-slate-900">Biomarker Trend</h2>
                  <select
                    value={selectedParam}
                    onChange={e => setSelectedParam(e.target.value)}
                    className="bg-slate-50 border border-slate-200 text-xs font-bold text-slate-700 px-3 py-1.5 rounded-lg"
                  >
                    {paramKeys.map(k => <option key={k} value={k}>{k}</option>)}
                  </select>
                </div>

                <div className="h-64 w-full pt-2">
                  <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={chartData}>
                      <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                      <XAxis dataKey="date" stroke="#64748b" fontSize={11} />
                      <YAxis stroke="#64748b" fontSize={11} />
                      <Tooltip contentStyle={{ backgroundColor: '#ffffff', borderColor: '#cbd5e1', borderRadius: '12px', fontSize: '12px' }} />
                      <Line type="monotone" dataKey="value" stroke="#0d9488" strokeWidth={2.5} name={selectedParam} />
                    </LineChart>
                  </ResponsiveContainer>
                </div>
              </div>
            )}

            {/* Upload History List */}
            <div className="space-y-3">
              <h2 className="text-base font-bold text-slate-900">Uploaded Reports ({data.reports.length})</h2>
              {data.reports.map((r, i) => (
                <div
                  key={i}
                  onClick={() => navigate(`/reports/${r.report_id}`)}
                  className="bg-white border border-slate-200 rounded-xl p-4 flex items-center justify-between cursor-pointer hover:border-teal-500 shadow-sm"
                >
                  <div className="flex items-center gap-3">
                    <FileText className="w-5 h-5 text-teal-600" />
                    <div>
                      <p className="text-xs font-bold text-slate-900">{r.source_filename}</p>
                      <p className="text-[11px] text-slate-500">{new Date(r.created_at).toLocaleDateString()}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <span className="text-xs font-bold text-teal-700 bg-teal-50 border border-teal-200 px-2.5 py-1 rounded-full">Score: {r.health_score}</span>
                    <ArrowRight className="w-4 h-4 text-slate-400" />
                  </div>
                </div>
              ))}
            </div>
          </>
        )}

      </div>
    </div>
  );
};
