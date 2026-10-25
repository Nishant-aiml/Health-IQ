/**
 * File: ConversationHistory.tsx
 * Purpose: Turn history for voice conversations displaying transcripts, translated answers, and audio players.
 * Module: Frontend / Components / Voice
 * Used By: VoiceAssistantPage Component
 * Future Phase: Phase 3D Multilingual & Voice AI
 */

import React from 'react';
import { User, Bot, CheckCircle2 } from 'lucide-react';
import { VoicePlayer } from './VoicePlayer';

export interface VoiceTurn {
  id: string;
  transcript: string;
  response: string;
  languageCode: string;
  confidence: number;
  seniorMode: boolean;
  citations?: any[];
}

interface ConversationHistoryProps {
  turns: VoiceTurn[];
}

export const ConversationHistory: React.FC<ConversationHistoryProps> = ({ turns }) => {
  if (turns.length === 0) return null;

  return (
    <div className="space-y-4">
      <h3 className="text-sm font-bold text-slate-200 border-b border-slate-800 pb-2">
        Voice Conversation History ({turns.length} Turn{turns.length > 1 ? 's' : ''})
      </h3>

      {turns.map((turn) => (
        <div key={turn.id} className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3">
          {/* User Turn */}
          <div className="flex items-start gap-3 bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <div className="p-2 bg-teal-500/20 text-teal-400 rounded-lg shrink-0 mt-0.5">
              <User className="w-4 h-4" />
            </div>
            <div className="space-y-0.5 text-xs">
              <span className="text-[10px] text-slate-400 font-bold uppercase">Spoken Query ({turn.languageCode})</span>
              <p className="text-slate-100 font-semibold">{turn.transcript}</p>
            </div>
          </div>

          {/* AI Response Turn */}
          <div className="flex items-start gap-3 bg-slate-950/90 p-4 rounded-xl border border-teal-500/30">
            <div className="p-2 bg-indigo-500/20 text-indigo-400 rounded-lg shrink-0 mt-0.5">
              <Bot className="w-4 h-4" />
            </div>
            <div className="space-y-2 text-xs w-full">
              <div className="flex items-center justify-between">
                <span className="text-[10px] text-teal-300 font-bold uppercase flex items-center gap-1">
                  <CheckCircle2 className="w-3 h-3 text-teal-400" /> Grounded AI Response ({Math.round(turn.confidence * 100)}% Confidence)
                </span>
                {turn.seniorMode && (
                  <span className="text-[9px] bg-amber-950 text-amber-300 px-2 py-0.5 rounded font-bold border border-amber-500/30">
                    Senior Mode Simplified
                  </span>
                )}
              </div>

              <p className="text-slate-200 leading-relaxed text-sm font-medium">{turn.response}</p>

              {/* TTS Audio Player */}
              <VoicePlayer text={turn.response} languageCode={turn.languageCode} seniorMode={turn.seniorMode} />
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};
