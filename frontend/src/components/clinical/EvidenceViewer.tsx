/**
 * File: EvidenceViewer.tsx
 * Purpose: Visualizes the Evidence Graph (Lab Result → Trend → Recommendation → Nutrition → Clinical Summary)
 *          with collapsible node chains and confidence scores.
 * Module: Frontend / Components / Clinical
 * Used By: ClinicalSummaryPage
 */

import React from 'react';
import { GitBranch, ChevronRight, BarChart2 } from 'lucide-react';

interface EvidenceNode {
  node_id: string;
  source_type: string;
  title: string;
  description: string;
  connected_to: string[];
  confidence_score: number;
}

interface EvidenceViewerProps {
  evidenceGraph: EvidenceNode[];
}

const SOURCE_STYLES: Record<string, { badge: string; bar: string }> = {
  lab_result:        { badge: 'bg-teal-900/30 text-teal-300 border-teal-700/30', bar: 'bg-teal-400' },
  trend:             { badge: 'bg-indigo-900/30 text-indigo-300 border-indigo-700/30', bar: 'bg-indigo-400' },
  trend_analysis:    { badge: 'bg-indigo-900/30 text-indigo-300 border-indigo-700/30', bar: 'bg-indigo-400' },
  recommendation:    { badge: 'bg-amber-900/30 text-amber-300 border-amber-700/30', bar: 'bg-amber-400' },
  nutrition:         { badge: 'bg-emerald-900/30 text-emerald-300 border-emerald-700/30', bar: 'bg-emerald-400' },
  nutrition_plan:    { badge: 'bg-emerald-900/30 text-emerald-300 border-emerald-700/30', bar: 'bg-emerald-400' },
  clinical_summary:  { badge: 'bg-purple-900/30 text-purple-300 border-purple-700/30', bar: 'bg-purple-400' },
};

const FLOW_LABELS: Record<string, string> = {
  lab_result: 'Lab Result',
  trend: 'Trend Analysis',
  trend_analysis: 'Trend Analysis',
  recommendation: 'Recommendation',
  nutrition: 'Nutrition Plan',
  nutrition_plan: 'Nutrition Plan',
  clinical_summary: 'Clinical Summary',
};

export const EvidenceViewer: React.FC<EvidenceViewerProps> = ({ evidenceGraph }) => {
  const nodeById: Record<string, EvidenceNode> = {};
  evidenceGraph.forEach(n => { nodeById[n.node_id] = n; });

  // Find root nodes (not connected to by anyone)
  const referenced = new Set(evidenceGraph.flatMap(n => n.connected_to));
  const roots = evidenceGraph.filter(n => !referenced.has(n.node_id));

  const renderChain = (node: EvidenceNode, depth: number = 0): JSX.Element => {
    const style = SOURCE_STYLES[node.source_type] || { badge: 'bg-slate-800 text-slate-300 border-slate-700', bar: 'bg-slate-400' };
    return (
      <div key={node.node_id} className={`pl-${depth * 4}`}>
        <div className={`p-3.5 rounded-xl border text-xs space-y-2 ${depth > 0 ? 'ml-4 mt-2 border-l-2 border-l-slate-600/40' : ''} bg-slate-950/70 border-slate-800/70`}>
          <div className="flex items-center justify-between gap-2 flex-wrap">
            <span className="font-bold text-slate-100">{node.title}</span>
            <span className={`text-[10px] px-2 py-0.5 rounded-full border font-bold ${style.badge}`}>
              {FLOW_LABELS[node.source_type] || node.source_type}
            </span>
          </div>
          <p className="text-slate-300 leading-relaxed">{node.description}</p>
          <div className="flex items-center gap-2 mt-1">
            <BarChart2 className="w-3 h-3 text-slate-500 shrink-0" />
            <div className="flex-1 h-1.5 bg-slate-800 rounded-full overflow-hidden">
              <div className={`h-full ${style.bar} rounded-full transition-all`} style={{ width: `${node.confidence_score * 100}%` }} />
            </div>
            <span className="text-[10px] text-slate-400 font-mono">{(node.confidence_score * 100).toFixed(0)}%</span>
          </div>
          {node.connected_to.length > 0 && (
            <div className="mt-1 space-y-1">
              {node.connected_to.map(childId => {
                const child = nodeById[childId];
                return child ? (
                  <div key={childId} className="flex items-start gap-2 mt-2">
                    <ChevronRight className="w-3.5 h-3.5 text-slate-500 mt-0.5 shrink-0" />
                    {renderChain(child, depth + 1)}
                  </div>
                ) : null;
              })}
            </div>
          )}
        </div>
      </div>
    );
  };

  // Evidence pipeline header
  const flowTypes = ['lab_result', 'trend_analysis', 'recommendation', 'nutrition_plan', 'clinical_summary'];

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-5">
      <h3 className="text-base font-bold text-slate-100 flex items-center gap-2 border-b border-slate-800 pb-4">
        <GitBranch className="w-5 h-5 text-indigo-400" /> Evidence Graph
      </h3>

      {/* Flow legend */}
      <div className="flex items-center gap-1.5 flex-wrap text-[10px]">
        {flowTypes.map((ft, idx) => (
          <React.Fragment key={ft}>
            <span className={`px-2 py-0.5 rounded-full border font-bold ${SOURCE_STYLES[ft]?.badge || ''}`}>{FLOW_LABELS[ft]}</span>
            {idx < flowTypes.length - 1 && <ChevronRight className="w-3 h-3 text-slate-600" />}
          </React.Fragment>
        ))}
      </div>

      {evidenceGraph.length === 0 ? (
        <p className="text-center py-8 text-slate-500 text-sm">No evidence nodes available.</p>
      ) : (
        <div className="space-y-4">
          {roots.length > 0 ? roots.map(root => renderChain(root)) : evidenceGraph.slice(0, 3).map(n => renderChain(n))}
        </div>
      )}
    </div>
  );
};
