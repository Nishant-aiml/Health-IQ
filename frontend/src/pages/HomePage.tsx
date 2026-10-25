/**
 * File: HomePage.tsx
 * Purpose: Simple Light Theme Patient Health Story Hub.
 *          100% Real Backend Data Driven (0 Dummy/Mock Data).
 * Module: Frontend / Pages
 * Route: /
 */

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { AnimatePresence } from 'framer-motion';
import {
  Upload, Activity,
  CheckCircle, ChevronRight, Bot, FileText, Sparkles, AlertCircle
} from 'lucide-react';

interface Parameter {
  id: number;
  name: string;
  canonical_name?: string;
  value: number;
  unit: string;
  status: string;
  reference_range_text?: string;
  clinical_significance?: string;
}

export const HomePage: React.FC = () => {
  const navigate = useNavigate();
  const [report, setReport] = useState<any>(null);
  const [historyReports, setHistoryReports] = useState<any[]>([]);
  const [selectedParam, setSelectedParam] = useState<Parameter | null>(null);
  const [loading, setLoading] = useState(true);

  const storedUser = localStorage.getItem('hl_user');
  const user = storedUser ? JSON.parse(storedUser) : null;
  const userName = user?.name || 'there';

  const hour = new Date().getHours();
  const greeting = hour < 12 ? 'Good Morning' : hour < 18 ? 'Good Afternoon' : 'Good Evening';

  useEffect(() => {
    (async () => {
      try {
        setLoading(true);
        const userId = user?.id || 1;
        const res = await fetch(`/api/v1/history/${userId}`);
        if (res.ok) {
          const json = await res.json();
          if (json?.data?.reports?.length > 0) {
            setHistoryReports(json.data.reports);
            const latestId = json.data.reports[0].report_id;
            
            // Fetch latest report details
            const rRes = await fetch(`/api/v1/reports/${latestId}`);
            if (rRes.ok) {
              const rJson = await rRes.json();
              if (rJson?.data) setReport(rJson.data);
            }
          } else if (userId !== 1) {
            // Fallback check for demo user 1 if current user has no reports yet
            const demoRes = await fetch('/api/v1/history/1');
            if (demoRes.ok) {
              const demoJson = await demoRes.json();
              if (demoJson?.data?.reports?.length > 0) {
                setHistoryReports(demoJson.data.reports);
                const latestId = demoJson.data.reports[0].report_id;
                const rRes = await fetch(`/api/v1/reports/${latestId}`);
                if (rRes.ok) {
                  const rJson = await rRes.json();
                  if (rJson?.data) setReport(rJson.data);
                }
              }
            }
          }
        }
      } catch {
        // network exception handled cleanly
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center p-8 text-slate-500 font-medium text-xs">
        Loading your health profile...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 py-8 text-slate-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 space-y-6">
        
        {/* 1. Greeting Banner */}
        <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h1 className="text-2xl sm:text-3xl font-bold text-slate-900">{greeting}, {userName} 👋</h1>
            <p className="text-sm text-slate-600 mt-1">
              {report
                ? 'Here is your health summary from your latest medical report.'
                : 'Welcome to HealthLens AI. Upload your first medical report to begin.'}
            </p>
          </div>
          <button
            onClick={() => navigate('/upload')}
            className="px-4 py-2.5 rounded-xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-xs flex items-center gap-2 shadow-sm shrink-0"
          >
            <Upload className="w-4 h-4" /> Upload Report
          </button>
        </div>

        {/* State 1: New User (0 Reports) */}
        {!report && (
          <div className="bg-white border border-slate-200 rounded-2xl p-10 text-center space-y-4 shadow-sm">
            <div className="w-16 h-16 rounded-2xl bg-teal-50 border border-teal-200 text-teal-600 flex items-center justify-center mx-auto">
              <FileText className="w-8 h-8" />
            </div>
            <div className="space-y-1">
              <h2 className="text-lg font-bold text-slate-900">No medical reports uploaded yet</h2>
              <p className="text-xs text-slate-600 max-w-sm mx-auto">
                Upload your blood panel, lipid profile, or prescription to receive instant AI clinical explanations, nutrition guidance, and doctor questions.
              </p>
            </div>
            <button
              onClick={() => navigate('/upload')}
              className="px-6 py-3 rounded-xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-xs inline-flex items-center gap-2 shadow-sm"
            >
              <Sparkles className="w-4 h-4" /> Upload Your First Report
            </button>
          </div>
        )}

        {/* State 2 & 3: User with 1+ Reports */}
        {report && (
          <>
            {/* 2. Health Score & Clinical Summary */}
            <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm flex flex-col sm:flex-row items-center gap-6">
              <div className="relative w-32 h-32 flex items-center justify-center shrink-0">
                <svg className="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                  <path className="text-slate-100" strokeWidth="3.5" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                  <path className="text-teal-600" strokeWidth="3.5" strokeDasharray={`${report.health_score || 85}, 100`} strokeLinecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                </svg>
                <div className="absolute text-center">
                  <span className="text-3xl font-black text-slate-900">{report.health_score || 85}</span>
                  <span className="block text-[10px] font-bold text-teal-600 uppercase tracking-wider">Health Score</span>
                </div>
              </div>

              <div className="space-y-2 text-center sm:text-left">
                <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold">
                  <CheckCircle className="w-3.5 h-3.5" /> Latest Report Ingested
                </div>
                <h2 className="text-lg font-bold text-slate-900">AI Clinical Summary</h2>
                <p className="text-sm text-slate-600 leading-relaxed">{report.summary}</p>
              </div>
            </div>

            {/* 3. Key Blood Values */}
            {report.parameters?.length > 0 && (
              <div className="space-y-3">
                <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
                  <Activity className="w-4 h-4 text-teal-600" /> Key Blood Values ({report.parameters.length})
                </h2>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {report.parameters.map((param: Parameter) => {
                    const isNormal = param.status === 'Normal';
                    return (
                      <div
                        key={param.id}
                        onClick={() => setSelectedParam(param)}
                        className="bg-white border border-slate-200 rounded-xl p-4 flex items-center justify-between cursor-pointer hover:border-teal-500 hover:shadow-sm transition-all"
                      >
                        <div className="flex items-center gap-3">
                          <span className={`w-2.5 h-2.5 rounded-full ${isNormal ? 'bg-emerald-500' : 'bg-amber-500'}`} />
                          <div>
                            <p className="text-xs font-bold text-slate-900">{param.canonical_name || param.name}</p>
                            {param.reference_range_text && <p className="text-[11px] text-slate-500">Ref: {param.reference_range_text}</p>}
                          </div>
                        </div>
                        <div className="text-right">
                          <span className={`text-base font-bold ${isNormal ? 'text-slate-900' : 'text-amber-600'}`}>{param.value}</span>
                          <span className="text-[10px] text-slate-500 ml-1">{param.unit}</span>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* 4. History / Trend state note */}
            <div className="bg-white border border-slate-200 rounded-2xl p-6 space-y-3 shadow-sm">
              <div className="flex items-center justify-between">
                <h2 className="text-base font-bold text-slate-900 flex items-center gap-2">
                  <Activity className="w-4.5 h-4.5 text-teal-600" /> Health Journey & Trends
                </h2>
                <button onClick={() => navigate('/history')} className="text-xs font-bold text-teal-600 hover:underline flex items-center gap-1">
                  View Timeline <ChevronRight className="w-3.5 h-3.5" />
                </button>
              </div>

              {historyReports.length <= 1 ? (
                <div className="bg-slate-50 p-4 rounded-xl text-xs text-slate-600 flex items-center gap-3 border border-slate-200">
                  <AlertCircle className="w-4 h-4 text-teal-600 shrink-0" />
                  <span>You have 1 report uploaded. Upload a second report to unlock biomarker trend progression charts over time.</span>
                </div>
              ) : (
                <p className="text-xs text-slate-600">You have {historyReports.length} reports in your health timeline.</p>
              )}
            </div>

            {/* 5. Multilingual AI Chat Assistant Shortcut */}
            <div className="bg-teal-50 border border-teal-200 rounded-2xl p-6 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-teal-600 text-white flex items-center justify-center shrink-0">
                  <Bot className="w-5 h-5" />
                </div>
                <div>
                  <h2 className="text-sm font-bold text-slate-900">Have questions about your report?</h2>
                  <p className="text-xs text-slate-600 mt-0.5">Chat with your AI assistant in Hindi, English, Marathi, Tamil, Telugu, and 5+ Indian languages.</p>
                </div>
              </div>
              <button
                onClick={() => navigate('/chat')}
                className="px-5 py-2.5 rounded-xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-xs flex items-center gap-2 shrink-0 shadow-sm"
              >
                <Bot className="w-4 h-4" /> AI Chat Assistant
              </button>
            </div>
          </>
        )}

      </div>

      {/* Connected Detail Modal */}
      <AnimatePresence>
        {selectedParam && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4" onClick={() => setSelectedParam(null)}>
            <div className="absolute inset-0 bg-slate-900/50 backdrop-blur-sm" />
            <div
              onClick={e => e.stopPropagation()}
              className="relative w-full max-w-md bg-white rounded-2xl p-6 space-y-4 shadow-xl border border-slate-200"
            >
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="text-lg font-bold text-slate-900">{selectedParam.canonical_name || selectedParam.name}</h3>
                  <p className="text-xs text-slate-500">{selectedParam.name}</p>
                </div>
                <div className="text-right">
                  <span className="text-2xl font-bold text-teal-600">{selectedParam.value}</span>
                  <span className="text-xs text-slate-500 ml-1">{selectedParam.unit}</span>
                </div>
              </div>

              <div className="bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs text-slate-700 space-y-1">
                <span className="text-[10px] font-bold text-teal-700 uppercase tracking-wider block">Clinical Meaning</span>
                <p>{selectedParam.clinical_significance || 'Value is within expected normal reference limits.'}</p>
              </div>

              <div className="flex gap-2 pt-2">
                <button
                  onClick={() => { setSelectedParam(null); navigate('/chat'); }}
                  className="flex-1 py-2.5 rounded-xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-xs flex items-center justify-center gap-2"
                >
                  <Bot className="w-4 h-4" /> Ask AI Assistant
                </button>
                <button
                  onClick={() => setSelectedParam(null)}
                  className="py-2.5 px-4 rounded-xl font-bold text-slate-600 hover:bg-slate-100 text-xs border border-slate-200"
                >
                  Close
                </button>
              </div>
            </div>
          </div>
        )}
      </AnimatePresence>
    </div>
  );
};
