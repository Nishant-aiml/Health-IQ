/**
 * File: FHIRPreview.tsx
 * Purpose: Preview and download FHIR R4 Bundle (Patient + Observations + DiagnosticReport) for EHR integration.
 * Module: Frontend / Components / Clinical
 * Used By: ClinicalSummaryPage
 */

import React, { useState } from 'react';
import { Database, Download, ChevronDown, ChevronUp, Code2 } from 'lucide-react';

interface FHIRPreviewProps {
  fhirBundle: any;
}

export const FHIRPreview: React.FC<FHIRPreviewProps> = ({ fhirBundle }) => {
  const [expanded, setExpanded] = useState(false);

  if (!fhirBundle) return null;

  const entries = fhirBundle.entry || [];
  const resourceTypes = entries.map((e: any) => e.resource?.resourceType).filter(Boolean);
  const counts: Record<string, number> = {};
  resourceTypes.forEach((rt: string) => { counts[rt] = (counts[rt] || 0) + 1; });

  const handleDownload = () => {
    const blob = new Blob([JSON.stringify(fhirBundle, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'healthlens_fhir_bundle.json';
    a.click();
    URL.revokeObjectURL(url);
  };

  const TYPE_BADGE: Record<string, string> = {
    'Patient': 'bg-teal-900/30 text-teal-300 border-teal-700/30',
    'Observation': 'bg-indigo-900/30 text-indigo-300 border-indigo-700/30',
    'DiagnosticReport': 'bg-amber-900/30 text-amber-300 border-amber-700/30',
    'Bundle': 'bg-purple-900/30 text-purple-300 border-purple-700/30',
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-5">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4 flex-wrap gap-3">
        <h3 className="text-base font-bold text-slate-100 flex items-center gap-2">
          <Database className="w-5 h-5 text-green-400" /> FHIR R4 Export
        </h3>
        <button
          onClick={handleDownload}
          className="flex items-center gap-1.5 text-xs bg-green-700 hover:bg-green-600 text-white px-3 py-1.5 rounded-lg font-bold transition-colors"
        >
          <Download className="w-3.5 h-3.5" /> Download Bundle
        </button>
      </div>

      {/* Bundle Summary */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
        {Object.entries(counts).map(([type, count]) => (
          <div key={type} className={`p-3 rounded-xl border text-center ${TYPE_BADGE[type] || 'bg-slate-950/50 text-slate-300 border-slate-700'}`}>
            <p className="text-xl font-black">{count}</p>
            <p className="text-[10px] font-bold uppercase tracking-wider">{type}</p>
          </div>
        ))}
      </div>

      {/* Bundle metadata */}
      <div className="text-xs space-y-1.5">
        {[
          { label: 'Bundle Type', value: fhirBundle.type },
          { label: 'FHIR Version', value: 'R4' },
          { label: 'Timestamp', value: fhirBundle.timestamp },
          { label: 'Total Entries', value: entries.length },
        ].map(({ label, value }) => (
          <div key={label} className="flex justify-between items-center bg-slate-950/60 px-3 py-2 rounded-lg border border-slate-800">
            <span className="text-slate-400 font-bold">{label}</span>
            <span className="text-slate-200 font-mono text-[11px]">{String(value)}</span>
          </div>
        ))}
      </div>

      {/* Raw JSON Preview Toggle */}
      <div>
        <button
          onClick={() => setExpanded(!expanded)}
          className="flex items-center gap-1.5 text-xs font-bold text-slate-400 hover:text-slate-200 transition-colors"
        >
          <Code2 className="w-3.5 h-3.5" /> Raw JSON Preview
          {expanded ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
        </button>

        {expanded && (
          <div className="mt-3 bg-slate-950 rounded-xl border border-slate-800 overflow-auto max-h-64">
            <pre className="text-[10px] text-green-300/80 p-4 whitespace-pre-wrap leading-relaxed font-mono">
              {JSON.stringify(fhirBundle, null, 2).slice(0, 2000)}
              {JSON.stringify(fhirBundle, null, 2).length > 2000 ? '\n... (truncated)' : ''}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
};
