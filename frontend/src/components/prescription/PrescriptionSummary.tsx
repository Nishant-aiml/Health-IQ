/**
 * File: PrescriptionSummary.tsx
 * Purpose: Executive summary banner displaying total medicines count, high-risk flag, and safety notes.
 * Module: Frontend / Components / Prescription
 * Used By: Prescription Page & Dashboard
 * Future Phase: Phase 3A Medicine Intelligence
 */

import React from 'react';
import { Pill, ShieldAlert, CheckCircle2, AlertOctagon } from 'lucide-react';
import { InteractionAlert, DrugInteractionItem } from './InteractionAlert';

interface PrescriptionSummaryProps {
  totalMedicines: number;
  safetyAnalysis: {
    interactions: DrugInteractionItem[];
    duplicate_therapies: DrugInteractionItem[];
    has_high_risk: boolean;
    monitoring_notes: string[];
  };
}

export const PrescriptionSummary: React.FC<PrescriptionSummaryProps> = ({ totalMedicines, safetyAnalysis }) => {
  const allAlerts = [...safetyAnalysis.interactions, ...safetyAnalysis.duplicate_therapies];

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between flex-wrap gap-4 mb-4">
        <div>
          <h2 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Pill className="w-5 h-5 text-teal-400" /> Prescription Medicine Intelligence Summary
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Verified {totalMedicines} prescribed medicine(s) with automated clinical interaction screening.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <div className="bg-slate-950 px-4 py-2 rounded-xl border border-slate-800 text-center">
            <span className="text-xs text-slate-400 block">Total Medicines</span>
            <span className="text-lg font-bold text-teal-300">{totalMedicines}</span>
          </div>

          <div className="bg-slate-950 px-4 py-2 rounded-xl border border-slate-800 text-center">
            <span className="text-xs text-slate-400 block">Safety Rating</span>
            <span
              className={`text-sm font-bold flex items-center gap-1 justify-center ${
                safetyAnalysis.has_high_risk ? 'text-rose-400' : 'text-emerald-400'
              }`}
            >
              {safetyAnalysis.has_high_risk ? (
                <>
                  <AlertOctagon className="w-4 h-4" /> Action Required
                </>
              ) : (
                <>
                  <CheckCircle2 className="w-4 h-4" /> Low Risk
                </>
              )}
            </span>
          </div>
        </div>
      </div>

      {/* Safety Alerts Section */}
      {allAlerts.length > 0 ? (
        <div className="mt-4">
          <h3 className="text-sm font-bold text-slate-200 mb-3 flex items-center gap-2">
            <ShieldAlert className="w-4 h-4 text-amber-400" /> Detected Safety Warnings & Drug Interactions ({allAlerts.length})
          </h3>
          {allAlerts.map((item, idx) => (
            <InteractionAlert key={idx} interaction={item} />
          ))}
        </div>
      ) : (
        <div className="bg-emerald-950/20 border border-emerald-500/30 rounded-xl p-4 mt-3 flex items-center gap-3 text-xs text-emerald-300">
          <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
          <span>No critical drug-drug interactions or duplicate therapy conflicts detected across prescribed items.</span>
        </div>
      )}

      {/* General Clinical Guidance */}
      <div className="mt-4 pt-4 border-t border-slate-800/80 text-xs text-slate-400 space-y-1">
        {safetyAnalysis.monitoring_notes.map((note, i) => (
          <p key={i} className="flex items-center gap-1.5">
            <span className="w-1.5 h-1.5 rounded-full bg-teal-400 shrink-0"></span> {note}
          </p>
        ))}
      </div>
    </div>
  );
};
