/**
 * File: ReportDashboardPage.tsx
 * Purpose: Simple Light Theme Patient Results Dashboard.
 * Module: Frontend / Pages
 * Route: /reports/:reportId
 */

import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  ArrowLeft, Sparkles, Smile,
  Bot, AlertTriangle, Download,
  BarChart3, Stethoscope, CheckCircle
} from 'lucide-react';
import { ChatWindow } from '../components/chat/ChatWindow';

interface Parameter {
  id: number;
  name: string;
  canonical_name?: string;
  value: number;
  unit: string;
  status: string;
  reference_range_low?: number;
  reference_range_high?: number;
  reference_range_text?: string;
  clinical_significance?: string;
}

interface Pattern {
  pattern_name: string;
  confidence: string;
  triggered_by: string[];
  summary: string;
}

interface ReportData {
  report_id: number;
  source_filename: string;
  status: string;
  health_score: number;
  health_score_details?: any;
  summary: string;
  parameters: Parameter[];
  critical_alerts: { parameter_name: string; value: number; unit: string; severity: string; message: string }[];
  detected_patterns: Pattern[];
}

interface Recommendation {
  category: string;
  priority: string;
  recommendation: string;
  explanation: string;
  evidence_source: string;
}

interface Bundle {
  recommendations: Recommendation[];
  evidence_chains: any[];
  limitations: any[];
  doctor_questions: { category: string; question: string; rationale: string }[];
  eli10_explanation: string;
}

export const ReportDashboardPage: React.FC = () => {
  const { reportId } = useParams<{ reportId: string }>();
  const navigate = useNavigate();
  const [report, setReport] = useState<ReportData | null>(null);
  const [bundle, setBundle] = useState<Bundle | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<string>('overview');
  const [selectedParam, setSelectedParam] = useState<Parameter | null>(null);

  useEffect(() => {
    if (!reportId) return;
    (async () => {
      try {
        setLoading(true);
        const [rr, br] = await Promise.all([
          fetch(`/api/v1/reports/${reportId}`),
          fetch(`/api/v1/reports/${reportId}/recommendations`),
        ]);
        if (!rr.ok) throw new Error('Report not found.');
        const rj = await rr.json();
        if (rj.data) setReport(rj.data);
        if (br.ok) {
          const bj = await br.json();
          if (bj.data) setBundle(bj.data);
        }
      } catch (e: any) {
        setError(e.message || 'Could not load health report.');
      } finally {
        setLoading(false);
      }
    })();
  }, [reportId]);

  if (loading) return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-8 text-slate-600 font-medium text-sm">
      Loading Report Analysis...
    </div>
  );

  if (error || !report) return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
      <div className="bg-white border border-slate-200 rounded-2xl p-6 text-center space-y-4 max-w-sm">
        <AlertTriangle className="w-8 h-8 text-amber-500 mx-auto" />
        <h2 className="text-base font-bold text-slate-900">Couldn't Load Report</h2>
        <p className="text-xs text-slate-600">{error}</p>
        <button onClick={() => navigate('/upload')} className="w-full py-2.5 rounded-xl font-bold bg-teal-600 text-white text-xs">
          Upload New Report
        </button>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-slate-50 py-8 text-slate-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 space-y-6">
        
        {/* Navigation back */}
        <div className="flex items-center justify-between">
          <button onClick={() => navigate(-1)} className="flex items-center gap-1 text-xs font-bold text-slate-600 hover:text-slate-900">
            <ArrowLeft className="w-4 h-4" /> Back to Dashboard
          </button>
          <button
            onClick={() => window.open(`/api/v1/reports/${report.report_id}/summary`, '_blank')}
            className="flex items-center gap-1.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 px-3.5 py-1.5 rounded-xl"
          >
            <Download className="w-3.5 h-3.5" /> Download PDF
          </button>
        </div>

        {/* Score & Summary Banner */}
        <div className="bg-white border border-slate-200 rounded-2xl p-6 flex flex-col sm:flex-row items-center gap-6 shadow-sm">
          <div className="relative w-32 h-32 flex items-center justify-center shrink-0">
            <svg className="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
              <path className="text-slate-100" strokeWidth="3.5" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
              <path className="text-teal-600" strokeWidth="3.5" strokeDasharray={`${report.health_score}, 100`} strokeLinecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
            </svg>
            <div className="absolute text-center">
              <span className="text-3xl font-black text-slate-900">{report.health_score}</span>
              <span className="block text-[10px] font-bold text-teal-600 uppercase">Health Score</span>
            </div>
          </div>

          <div className="space-y-2 text-center sm:text-left">
            <div className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold">
              <CheckCircle className="w-3.5 h-3.5" /> Analysis Complete
            </div>
            <h1 className="text-xl font-bold text-slate-900">{report.source_filename}</h1>
            <p className="text-xs text-slate-600 leading-relaxed">{report.summary}</p>
          </div>
        </div>

        {/* Tab Navigation */}
        <div className="flex gap-1 bg-white p-1 rounded-xl border border-slate-200 shadow-sm overflow-x-auto no-scrollbar">
          {[
            { id: 'overview', label: 'Overview', icon: <BarChart3 className="w-3.5 h-3.5" /> },
            { id: 'chat', label: 'Report Chat', icon: <Bot className="w-3.5 h-3.5" /> },
            { id: 'recommendations', label: 'Recommendations', icon: <Sparkles className="w-3.5 h-3.5" /> },
            { id: 'questions', label: 'Doctor Questions', icon: <Stethoscope className="w-3.5 h-3.5" /> },
            { id: 'eli10', label: 'Simple View', icon: <Smile className="w-3.5 h-3.5" /> }
          ].map(t => (
            <button
              key={t.id}
              onClick={() => setActiveTab(t.id)}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-xs font-bold whitespace-nowrap transition-all ${
                activeTab === t.id ? 'bg-teal-600 text-white shadow-sm' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              {t.icon} {t.label}
            </button>
          ))}
        </div>

        {/* Tab 1: Overview Parameters */}
        {activeTab === 'overview' && (
          <div className="space-y-4">
            <h2 className="text-sm font-bold text-slate-900">Laboratory Parameters ({report.parameters.length})</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {report.parameters.map(p => (
                <div
                  key={p.id}
                  onClick={() => setSelectedParam(p)}
                  className="bg-white border border-slate-200 rounded-xl p-4 flex items-center justify-between cursor-pointer hover:border-teal-500 hover:shadow-sm"
                >
                  <div>
                    <p className="text-xs font-bold text-slate-900">{p.canonical_name || p.name}</p>
                    <p className="text-[11px] text-slate-500">{p.name} {p.reference_range_text && `· Ref: ${p.reference_range_text}`}</p>
                  </div>
                  <div className="text-right">
                    <span className="text-base font-bold text-slate-900">{p.value}</span>
                    <span className="text-[10px] text-slate-500 ml-1">{p.unit}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Tab 2: Chat */}
        {activeTab === 'chat' && (
          <div className="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm">
            <ChatWindow reportId={report.report_id} />
          </div>
        )}

        {/* Tab 3: Recommendations */}
        {activeTab === 'recommendations' && bundle && (
          <div className="space-y-3">
            {bundle.recommendations.map((r, i) => (
              <div key={i} className="bg-white border border-slate-200 rounded-xl p-4 space-y-1 text-xs">
                <span className="font-bold text-teal-700 uppercase tracking-wider text-[10px]">{r.category}</span>
                <p className="font-bold text-slate-900">{r.recommendation}</p>
                <p className="text-slate-600">{r.explanation}</p>
              </div>
            ))}
          </div>
        )}

        {/* Tab 4: Questions */}
        {activeTab === 'questions' && bundle && (
          <div className="space-y-3">
            {bundle.doctor_questions.map((q, i) => (
              <div key={i} className="bg-white border border-slate-200 rounded-xl p-4 text-xs space-y-1">
                <p className="font-bold text-slate-900">{i + 1}. {q.question}</p>
                <p className="text-slate-500">{q.rationale}</p>
              </div>
            ))}
          </div>
        )}

        {/* Tab 5: ELI10 */}
        {activeTab === 'eli10' && bundle && (
          <div className="bg-white border border-slate-200 rounded-2xl p-6 space-y-3 text-xs">
            <h2 className="font-bold text-slate-900 text-sm">Simple Explanation</h2>
            <p className="text-slate-600 leading-relaxed">{bundle.eli10_explanation}</p>
          </div>
        )}

        {/* Connected Detail Modal */}
        {selectedParam && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4" onClick={() => setSelectedParam(null)}>
            <div className="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" />
            <div
              onClick={e => e.stopPropagation()}
              className="relative w-full max-w-md bg-white rounded-2xl p-6 space-y-4 shadow-xl border border-slate-200"
            >
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="text-base font-bold text-slate-900">{selectedParam.canonical_name || selectedParam.name}</h3>
                  <p className="text-xs text-slate-500">{selectedParam.name}</p>
                </div>
                <div className="text-right">
                  <span className="text-xl font-bold text-teal-600">{selectedParam.value}</span>
                  <span className="text-xs text-slate-500 ml-1">{selectedParam.unit}</span>
                </div>
              </div>

              <div className="bg-slate-50 p-3.5 rounded-xl border border-slate-200 text-xs text-slate-700 space-y-1">
                <span className="text-[10px] font-bold text-teal-700 uppercase block">Clinical Explanation</span>
                <p>{selectedParam.clinical_significance || 'Value is within expected normal reference limits.'}</p>
              </div>

              <div className="flex gap-2 pt-2">
                <button
                  onClick={() => { setSelectedParam(null); navigate('/chat'); }}
                  className="flex-1 py-2 rounded-xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-xs"
                >
                  Ask AI Assistant About This
                </button>
                <button
                  onClick={() => setSelectedParam(null)}
                  className="py-2 px-4 rounded-xl font-bold text-slate-600 hover:bg-slate-100 text-xs border border-slate-200"
                >
                  Close
                </button>
              </div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
};
