/**
 * File: InteractionAlert.tsx
 * Purpose: Severity-coded clinical safety and drug-drug interaction warning alert banner.
 * Module: Frontend / Components / Prescription
 * Used By: Prescription Summary & Prescription Page
 * Future Phase: Phase 3A Medicine Intelligence
 */

import React from 'react';
import { AlertTriangle, Info, AlertOctagon } from 'lucide-react';

export interface DrugInteractionItem {
  drug_a: string;
  drug_b?: string;
  severity: 'HIGH' | 'MEDIUM' | 'LOW';
  interaction_type: string;
  title: string;
  description: string;
  recommendation: string;
  evidence_source?: string;
}

interface InteractionAlertProps {
  interaction: DrugInteractionItem;
}

export const InteractionAlert: React.FC<InteractionAlertProps> = ({ interaction }) => {
  const getSeverityStyle = () => {
    switch (interaction.severity) {
      case 'HIGH':
        return {
          bg: 'bg-rose-950/40 border-rose-500/50 text-rose-200',
          badge: 'bg-rose-500/20 text-rose-300 border-rose-500/40',
          icon: <AlertOctagon className="w-5 h-5 text-rose-400 shrink-0 mt-0.5" />,
        };
      case 'MEDIUM':
        return {
          bg: 'bg-amber-950/40 border-amber-500/50 text-amber-200',
          badge: 'bg-amber-500/20 text-amber-300 border-amber-500/40',
          icon: <AlertTriangle className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />,
        };
      default:
        return {
          bg: 'bg-sky-950/40 border-sky-500/50 text-sky-200',
          badge: 'bg-sky-500/20 text-sky-300 border-sky-500/40',
          icon: <Info className="w-5 h-5 text-sky-400 shrink-0 mt-0.5" />,
        };
    }
  };

  const style = getSeverityStyle();

  return (
    <div className={`p-4 rounded-xl border ${style.bg} mb-3 transition-all`}>
      <div className="flex gap-3">
        {style.icon}
        <div className="flex-1">
          <div className="flex items-center justify-between gap-2 flex-wrap mb-1">
            <h4 className="font-semibold text-sm">{interaction.title}</h4>
            <span className={`text-xs px-2.5 py-0.5 rounded-full font-bold border ${style.badge}`}>
              {interaction.severity} SEVERITY
            </span>
          </div>

          <p className="text-xs text-slate-300 mb-2 leading-relaxed">{interaction.description}</p>

          <div className="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80 text-xs">
            <span className="font-semibold text-teal-300">Clinical Recommendation: </span>
            <span className="text-slate-300">{interaction.recommendation}</span>
          </div>

          {interaction.evidence_source && (
            <p className="text-[10px] text-slate-400 mt-2 text-right italic">
              Source: {interaction.evidence_source}
            </p>
          )}
        </div>
      </div>
    </div>
  );
};
