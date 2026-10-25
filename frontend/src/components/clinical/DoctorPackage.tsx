/**
 * File: DoctorPackage.tsx
 * Purpose: Immutable Clinical Case Package card showing SHA-256 hash, lifecycle status, evidence graph, and questions for physician.
 * Module: Frontend / Components / Clinical
 * Used By: ClinicalSummaryPage Component
 * Future Phase: Phase 4 Clinical Collaboration & Digital Health Ecosystem
 */

import React, { useState } from 'react';
import { FileText, ShieldCheck, Hash, GitBranch, ChevronDown, ChevronUp } from 'lucide-react';

interface EvidenceNode {
  node_id: string;
  source_type: string;
  title: string;
  description: string;
  connected_to: string[];
  confidence_score: number;
}

interface DoctorPackageProps {
  packageData: any;
}

export const DoctorPackage: React.FC<DoctorPackageProps> = ({ packageData }) => {
  const [showEvidence, setShowEvidence] = useState(false);

  if (!packageData) return null;

  const statusColor: Record<string, string> = {
    'AI Generated': 'bg-teal-500/20 text-teal-300 border-teal-500/30',
    'Reviewed': 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30',
    'Shared': 'bg-indigo-500/20 text-indigo-300 border-indigo-500/30',
    'Draft': 'bg-slate-500/20 text-slate-300 border-slate-500/30',
    'Archived': 'bg-amber-500/20 text-amber-300 border-amber-500/30',
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-5">
      {/* Header */}
      <div className="flex items-center justify-between flex-wrap gap-3 border-b border-slate-800 pb-4">
        <h3 className="text-lg font-bold text-slate-100 flex items-center gap-2">
          <FileText className="w-5 h-5 text-teal-400" /> {packageData.header_title || 'Clinical Case Package'}
        </h3>
        <div className="flex items-center gap-2 flex-wrap">
          <span className={`text-[10px] px-2.5 py-0.5 rounded-full font-bold border ${statusColor[packageData.status] || 'bg-slate-800 text-slate-300'}`}>
            {packageData.status}
          </span>
          <span className="text-[10px] bg-slate-950 text-slate-400 px-2.5 py-0.5 rounded border border-slate-700 font-mono">
            v{packageData.package_version} · Engine {packageData.ai_engine_version}
          </span>
          <span className="text-[10px] bg-slate-950 text-slate-400 px-2.5 py-0.5 rounded border border-slate-700">
            {packageData.audience}
          </span>
        </div>
      </div>

      {/* Active Summary */}
      <div className="bg-slate-950/70 p-4 rounded-xl border border-slate-800 text-xs text-slate-200 leading-relaxed">
        <p className="font-semibold text-teal-300 text-[10px] uppercase tracking-wider mb-1">Clinical Summary</p>
        <p>{packageData.active_summary}</p>
      </div>

      {/* Sub-summaries */}
      <div className="grid sm:grid-cols-2 gap-3 text-xs">
        {[
          { label: 'Medication Summary', value: packageData.medication_summary },
          { label: 'Nutrition Focus', value: packageData.nutrition_summary },
          { label: 'Historical Context', value: packageData.historical_summary },
          { label: 'Timeline', value: packageData.timeline_summary },
        ].map((item, idx) => (
          <div key={idx} className="bg-slate-950/60 p-3 rounded-xl border border-slate-800">
            <p className="text-[10px] text-slate-400 uppercase tracking-wider font-bold mb-1">{item.label}</p>
            <p className="text-slate-200 text-xs leading-relaxed">{item.value}</p>
          </div>
        ))}
      </div>

      {/* Questions for Physician */}
      {packageData.questions_for_physician?.length > 0 && (
        <div className="space-y-2">
          <p className="text-xs font-bold text-slate-200 flex items-center gap-1.5">
            <ShieldCheck className="w-3.5 h-3.5 text-teal-400" /> Questions for Physician ({packageData.questions_for_physician.length})
          </p>
          {packageData.questions_for_physician.map((q: any, idx: number) => (
            <div key={idx} className="bg-slate-950/70 p-3 rounded-xl border border-slate-800 text-xs space-y-1">
              <p className="font-semibold text-teal-300 text-[10px] uppercase">{q.category}</p>
              <p className="text-slate-100 font-medium">{q.question}</p>
              <p className="text-slate-400 italic text-[11px]">Rationale: {q.rationale}</p>
            </div>
          ))}
        </div>
      )}

      {/* Evidence Graph Toggle */}
      <div>
        <button
          onClick={() => setShowEvidence(!showEvidence)}
          className="flex items-center gap-1.5 text-xs font-bold text-indigo-300 hover:text-indigo-200 transition-colors"
        >
          <GitBranch className="w-3.5 h-3.5" />
          Evidence Graph ({packageData.evidence_graph?.length || 0} Nodes)
          {showEvidence ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
        </button>

        {showEvidence && packageData.evidence_graph?.length > 0 && (
          <div className="mt-3 space-y-2">
            {packageData.evidence_graph.map((node: EvidenceNode, idx: number) => (
              <div key={idx} className="bg-slate-950/70 p-3 rounded-xl border border-indigo-900/40 text-xs space-y-1">
                <div className="flex items-center justify-between">
                  <span className="font-bold text-slate-100">{node.title}</span>
                  <span className="text-[10px] bg-indigo-900/40 text-indigo-300 px-2 py-0.5 rounded font-bold uppercase">{node.source_type.replace('_', ' ')}</span>
                </div>
                <p className="text-slate-300 leading-relaxed">{node.description}</p>
                {node.connected_to.length > 0 && (
                  <p className="text-[10px] text-slate-500 font-mono">↓ Connects to: {node.connected_to.join(', ')}</p>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* SHA-256 Hash Footer */}
      <div className="flex items-center gap-2 bg-slate-950/80 p-2.5 rounded-xl border border-slate-800 text-[10px] font-mono text-slate-400">
        <Hash className="w-3.5 h-3.5 text-amber-400 shrink-0" />
        <span>SHA-256: {packageData.sha256_integrity_hash?.slice(0, 32)}...</span>
        <span className="ml-auto text-amber-400 font-bold">Immutable</span>
      </div>
    </div>
  );
};
