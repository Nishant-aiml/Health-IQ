/**
 * File: FoodInteractionAlert.tsx
 * Purpose: Food-Medicine interaction warning card displaying mechanism, severity, and timing advice.
 * Module: Frontend / Components / Nutrition
 * Used By: NutritionPage Component
 * Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
 */

import React from 'react';
import { ShieldAlert, Pill, Clock } from 'lucide-react';

export interface FoodMedicineInteraction {
  drug_name: string;
  interacting_food_or_substance: string;
  severity: 'HIGH' | 'MEDIUM' | 'LOW';
  mechanism_and_reason: string;
  actionable_timing_guidance: string;
  evidence_level: string;
}

interface FoodInteractionAlertProps {
  interactions: FoodMedicineInteraction[];
}

export const FoodInteractionAlert: React.FC<FoodInteractionAlertProps> = ({ interactions }) => {
  if (!interactions || interactions.length === 0) {
    return null;
  }

  return (
    <div className="bg-rose-950/40 border border-rose-500/50 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between border-b border-rose-500/30 pb-3 mb-4">
        <h3 className="text-lg font-bold text-rose-200 flex items-center gap-2">
          <ShieldAlert className="w-5 h-5 text-rose-400" /> Food–Medicine Interaction Warnings ({interactions.length})
        </h3>
        <span className="text-xs text-rose-300 bg-rose-900/60 border border-rose-500/40 px-3 py-1 rounded-full font-bold">
          Prescription Safety Alert
        </span>
      </div>

      <div className="space-y-4">
        {interactions.map((inter, idx) => (
          <div key={idx} className="bg-slate-950/80 border border-rose-900/60 rounded-xl p-4 text-xs space-y-2">
            <div className="flex items-center justify-between flex-wrap gap-2">
              <div className="flex items-center gap-2 font-bold text-slate-100 text-sm">
                <Pill className="w-4 h-4 text-amber-400" />
                <span>{inter.drug_name} ↔ {inter.interacting_food_or_substance}</span>
              </div>
              <span className="text-[10px] bg-rose-500/20 text-rose-300 px-2 py-0.5 rounded font-bold border border-rose-500/30">
                {inter.severity} SEVERITY
              </span>
            </div>

            <p className="text-slate-300 text-xs leading-relaxed">{inter.mechanism_and_reason}</p>

            <div className="bg-slate-900/80 p-2.5 rounded-lg border border-slate-800 flex items-start gap-2 text-amber-300 text-[11px]">
              <Clock className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
              <span><strong>Actionable Timing:</strong> {inter.actionable_timing_guidance}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
