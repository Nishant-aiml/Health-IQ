/**
 * File: TranscriptViewer.tsx
 * Purpose: Real-time voice transcript display with Voice Medical Safety Filter badge.
 * Module: Frontend / Components / Voice
 * Used By: VoiceAssistantPage Component
 * Future Phase: Phase 3D Multilingual & Voice AI
 */

import React from 'react';
import { ShieldCheck, MessageSquareQuote } from 'lucide-react';

interface TranscriptViewerProps {
  rawTranscript: string;
  validatedTranscript: string;
  detectedLanguage: string;
  isSafe: boolean;
}

export const TranscriptViewer: React.FC<TranscriptViewerProps> = ({
  rawTranscript,
  validatedTranscript,
  detectedLanguage,
  isSafe,
}) => {
  if (!rawTranscript) return null;

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 mb-6 shadow-xl space-y-3">
      <div className="flex items-center justify-between border-b border-slate-800 pb-2">
        <h4 className="text-xs font-bold text-slate-100 flex items-center gap-2">
          <MessageSquareQuote className="w-4 h-4 text-teal-400" /> Recognized Speech Transcript
        </h4>
        <div className="flex items-center gap-2">
          <span className="text-[10px] bg-slate-950 text-slate-300 px-2 py-0.5 rounded font-bold uppercase">
            Lang: {detectedLanguage}
          </span>
          {isSafe ? (
            <span className="text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-500/30 px-2 py-0.5 rounded-full font-bold flex items-center gap-1">
              <ShieldCheck className="w-3 h-3 text-emerald-400" /> Voice Safety Verified
            </span>
          ) : (
            <span className="text-[10px] bg-rose-950 text-rose-300 border border-rose-500/30 px-2 py-0.5 rounded-full font-bold">
              Dosage Check Alert
            </span>
          )}
        </div>
      </div>

      <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-xs text-slate-200 leading-relaxed font-medium italic">
        "{validatedTranscript}"
      </div>
    </div>
  );
};
