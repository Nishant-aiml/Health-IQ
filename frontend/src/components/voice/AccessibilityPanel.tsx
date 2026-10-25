/**
 * File: AccessibilityPanel.tsx
 * Purpose: Accessibility profile selector (Standard, Senior Mode, Low Vision, Cognitive Support).
 * Module: Frontend / Components / Voice
 * Used By: VoiceAssistantPage Component
 * Future Phase: Phase 3D Multilingual & Voice AI
 */

import React from 'react';
import { Eye, Shield, Sparkles, UserCheck } from 'lucide-react';

export type AccessibilityProfile = 'Standard' | 'Senior' | 'LowVision' | 'Cognitive';

interface AccessibilityPanelProps {
  currentProfile: AccessibilityProfile;
  onProfileChange: (profile: AccessibilityProfile) => void;
  seniorMode: boolean;
  onToggleSeniorMode: (enabled: boolean) => void;
}

export const AccessibilityPanel: React.FC<AccessibilityPanelProps> = ({
  currentProfile,
  onProfileChange,
  seniorMode,
  onToggleSeniorMode,
}) => {
  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 mb-6 shadow-xl space-y-3">
      <div className="flex items-center justify-between border-b border-slate-800 pb-2">
        <h4 className="text-sm font-bold text-slate-100 flex items-center gap-2">
          <Eye className="w-4 h-4 text-teal-400" /> Accessibility & Reading Profiles
        </h4>
        <span className="text-[10px] bg-teal-950 text-teal-300 px-2 py-0.5 rounded-full font-semibold border border-teal-500/30">
          Patient Inclusive AI
        </span>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-2.5 text-xs">
        <button
          onClick={() => {
            onProfileChange('Standard');
            onToggleSeniorMode(false);
          }}
          className={`p-2.5 rounded-xl border text-left transition-all ${
            currentProfile === 'Standard'
              ? 'bg-teal-500/20 border-teal-500 text-teal-200 font-bold'
              : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
          }`}
        >
          <UserCheck className="w-3.5 h-3.5 mb-1 text-teal-400" />
          <span className="block font-bold">Standard</span>
          <span className="text-[10px] text-slate-400 font-normal">Normal reading & speed</span>
        </button>

        <button
          onClick={() => {
            onProfileChange('Senior');
            onToggleSeniorMode(true);
          }}
          className={`p-2.5 rounded-xl border text-left transition-all ${
            currentProfile === 'Senior' || seniorMode
              ? 'bg-amber-500/20 border-amber-500 text-amber-200 font-bold'
              : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
          }`}
        >
          <Shield className="w-3.5 h-3.5 mb-1 text-amber-400" />
          <span className="block font-bold">Senior Mode</span>
          <span className="text-[10px] text-slate-400 font-normal">Large text & 0.85x audio</span>
        </button>

        <button
          onClick={() => {
            onProfileChange('LowVision');
            onToggleSeniorMode(false);
          }}
          className={`p-2.5 rounded-xl border text-left transition-all ${
            currentProfile === 'LowVision'
              ? 'bg-indigo-500/20 border-indigo-500 text-indigo-200 font-bold'
              : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
          }`}
        >
          <Eye className="w-3.5 h-3.5 mb-1 text-indigo-400" />
          <span className="block font-bold">Low Vision</span>
          <span className="text-[10px] text-slate-400 font-normal">High contrast display</span>
        </button>

        <button
          onClick={() => {
            onProfileChange('Cognitive');
            onToggleSeniorMode(true);
          }}
          className={`p-2.5 rounded-xl border text-left transition-all ${
            currentProfile === 'Cognitive'
              ? 'bg-purple-500/20 border-purple-500 text-purple-200 font-bold'
              : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
          }`}
        >
          <Sparkles className="w-3.5 h-3.5 mb-1 text-purple-400" />
          <span className="block font-bold">Cognitive Support</span>
          <span className="text-[10px] text-slate-400 font-normal">Simplified ELI10 language</span>
        </button>
      </div>
    </div>
  );
};
