/**
 * File: MedicineCard.tsx
 * Purpose: All-in-one card component rendering medicine details, confidence badges, ELI10, and evidence citations.
 * Module: Frontend / Components / Prescription
 * Used By: Prescription Page & Dashboard
 * Future Phase: Phase 3A Medicine Intelligence
 */

import React, { useState } from 'react';
import { Pill, Shield, AlertCircle, Sparkles, BookOpen, Clock, HeartHandshake } from 'lucide-react';
import { ScheduleTimeline, NormalizedSchedule } from './ScheduleTimeline';

export interface MedicinePayload {
  medicine_name_raw: string;
  brand_name: string;
  generic_name: string;
  active_ingredient: string;
  drug_class: string;
  category: string;
  dosage: string;
  purpose: string;
  mechanism: string;
  schedule: NormalizedSchedule;
  side_effects: string[];
  contraindications: string[];
  food_warnings: string[];
  driving_warning: string;
  pregnancy_warning: string;
  pregnancy_category: string;
  storage: string;
  explanation: string;
  eli10: string;
  disclaimer: string;
  evidence: Array<{
    citation_id: string;
    source_organization: string;
    title: string;
    excerpt: string;
    relevance_score: number;
  }>;
  ocr_confidence: number;
  resolution_confidence: number;
  knowledge_confidence: number;
  is_unknown: boolean;
  possible_matches?: string[];
}

interface MedicineCardProps {
  medicine: MedicinePayload;
}

export const MedicineCard: React.FC<MedicineCardProps> = ({ medicine }) => {
  const [activeTab, setActiveTab] = useState<'details' | 'schedule' | 'safety' | 'eli10' | 'evidence'>('details');

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 mb-5 shadow-lg hover:border-slate-700 transition-all">
      {/* Header Info */}
      <div className="flex items-start justify-between flex-wrap gap-3 pb-4 border-b border-slate-800">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-teal-500/10 border border-teal-500/30 rounded-xl text-teal-400">
            <Pill className="w-6 h-6" />
          </div>
          <div>
            <div className="flex items-center gap-2 flex-wrap">
              <h3 className="text-lg font-bold text-slate-100">{medicine.brand_name || medicine.generic_name}</h3>
              {medicine.generic_name && (
                <span className="text-xs text-teal-300 bg-teal-950/60 border border-teal-500/30 px-2.5 py-0.5 rounded-full font-medium">
                  {medicine.generic_name}
                </span>
              )}
              {medicine.is_unknown && (
                <span className="text-xs bg-amber-500/20 text-amber-300 border border-amber-500/30 px-2 py-0.5 rounded-full font-semibold flex items-center gap-1">
                  <AlertCircle className="w-3 h-3" /> Unverified Match
                </span>
              )}
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              {medicine.active_ingredient} · <span className="text-slate-300">{medicine.drug_class}</span>
            </p>
          </div>
        </div>

        {/* Confidence Badge */}
        <div className="flex items-center gap-2">
          <span className="text-[11px] text-slate-400">Resolution Match:</span>
          <span
            className={`text-xs px-2.5 py-1 rounded-md font-bold border ${
              medicine.resolution_confidence >= 0.8
                ? 'bg-emerald-500/10 text-emerald-300 border-emerald-500/30'
                : 'bg-amber-500/10 text-amber-300 border-amber-500/30'
            }`}
          >
            {Math.round(medicine.resolution_confidence * 100)}%
          </span>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="flex gap-2 my-4 overflow-x-auto pb-1 border-b border-slate-800/60">
        <button
          onClick={() => setActiveTab('details')}
          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
            activeTab === 'details'
              ? 'bg-teal-500 text-slate-950 font-bold shadow-md shadow-teal-500/20'
              : 'text-slate-400 hover:bg-slate-800'
          }`}
        >
          <BookOpen className="w-3.5 h-3.5" /> Purpose & Action
        </button>

        <button
          onClick={() => setActiveTab('schedule')}
          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
            activeTab === 'schedule'
              ? 'bg-teal-500 text-slate-950 font-bold shadow-md shadow-teal-500/20'
              : 'text-slate-400 hover:bg-slate-800'
          }`}
        >
          <Clock className="w-3.5 h-3.5" /> Dosage & Schedule
        </button>

        <button
          onClick={() => setActiveTab('safety')}
          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
            activeTab === 'safety'
              ? 'bg-teal-500 text-slate-950 font-bold shadow-md shadow-teal-500/20'
              : 'text-slate-400 hover:bg-slate-800'
          }`}
        >
          <Shield className="w-3.5 h-3.5" /> Warnings & Precautions
        </button>

        <button
          onClick={() => setActiveTab('eli10')}
          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
            activeTab === 'eli10'
              ? 'bg-teal-500 text-slate-950 font-bold shadow-md shadow-teal-500/20'
              : 'text-slate-400 hover:bg-slate-800'
          }`}
        >
          <Sparkles className="w-3.5 h-3.5" /> ELI10 Analogy
        </button>

        <button
          onClick={() => setActiveTab('evidence')}
          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
            activeTab === 'evidence'
              ? 'bg-teal-500 text-slate-950 font-bold shadow-md shadow-teal-500/20'
              : 'text-slate-400 hover:bg-slate-800'
          }`}
        >
          <HeartHandshake className="w-3.5 h-3.5" /> RAG Evidence
        </button>
      </div>

      {/* Tab Content */}
      <div className="min-h-[140px] pt-1">
        {activeTab === 'details' && (
          <div className="space-y-3 text-xs text-slate-300">
            <div>
              <h4 className="font-semibold text-slate-200 mb-1">Primary Clinical Purpose</h4>
              <p className="bg-slate-950/60 p-3 rounded-xl border border-slate-800 leading-relaxed">
                {medicine.purpose}
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-slate-200 mb-1">Mechanism of Action</h4>
              <p className="bg-slate-950/60 p-3 rounded-xl border border-slate-800 leading-relaxed text-slate-400">
                {medicine.mechanism}
              </p>
            </div>
          </div>
        )}

        {activeTab === 'schedule' && (
          <div>
            <ScheduleTimeline schedule={medicine.schedule} />
            <p className="text-xs text-slate-400 italic mt-2">
              Food Instruction: {medicine.food_warnings[0] || 'Take as prescribed.'}
            </p>
          </div>
        )}

        {activeTab === 'safety' && (
          <div className="space-y-3 text-xs">
            <div className="grid md:grid-cols-2 gap-3">
              <div className="bg-slate-950/60 p-3 rounded-xl border border-slate-800">
                <h4 className="font-semibold text-amber-300 mb-1">Common Side Effects</h4>
                <ul className="list-disc list-inside text-slate-300 space-y-1">
                  {medicine.side_effects.map((se, i) => (
                    <li key={i}>{se}</li>
                  ))}
                </ul>
              </div>

              <div className="bg-slate-950/60 p-3 rounded-xl border border-slate-800">
                <h4 className="font-semibold text-rose-300 mb-1">Pregnancy & Driving Notes</h4>
                <p className="text-slate-300 mb-1">
                  <span className="font-bold">Pregnancy Category {medicine.pregnancy_category}: </span>
                  {medicine.pregnancy_warning}
                </p>
                <p className="text-slate-400">{medicine.driving_warning}</p>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'eli10' && (
          <div className="bg-gradient-to-r from-teal-950/30 to-indigo-950/30 p-4 rounded-xl border border-teal-500/30">
            <div className="flex items-center gap-2 text-teal-300 font-semibold text-xs mb-2">
              <Sparkles className="w-4 h-4 text-teal-400" /> Explain Like I'm 10 (Plain Language Analogy)
            </div>
            <p className="text-sm text-slate-200 leading-relaxed">{medicine.eli10}</p>
          </div>
        )}

        {activeTab === 'evidence' && (
          <div className="space-y-2">
            {medicine.evidence.map((cit) => (
              <div key={cit.citation_id} className="bg-slate-950/60 p-3 rounded-xl border border-slate-800 text-xs">
                <div className="flex items-center justify-between mb-1">
                  <span className="font-semibold text-teal-300">{cit.source_organization}</span>
                  <span className="text-[10px] text-slate-400">Relevance: {cit.relevance_score}</span>
                </div>
                <p className="text-slate-300 italic">{cit.excerpt}</p>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Safety Disclaimer Footer */}
      <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400">
        <span>{medicine.disclaimer}</span>
        <span className="text-slate-400">Storage: {medicine.storage}</span>
      </div>
    </div>
  );
};
