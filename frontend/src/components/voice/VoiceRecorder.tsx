/**
 * File: VoiceRecorder.tsx
 * Purpose: Interactive microphone recording component with animated soundwave pulses.
 * Module: Frontend / Components / Voice
 * Used By: VoiceAssistantPage Component
 * Future Phase: Phase 3D Multilingual & Voice AI
 */

import React from 'react';
import { Mic, Square, Loader2 } from 'lucide-react';

interface VoiceRecorderProps {
  isRecording: boolean;
  isProcessing: boolean;
  onStartRecording: () => void;
  onStopRecording: () => void;
}

export const VoiceRecorder: React.FC<VoiceRecorderProps> = ({
  isRecording,
  isProcessing,
  onStartRecording,
  onStopRecording,
}) => {
  return (
    <div className="flex flex-col items-center justify-center p-6 bg-slate-950/80 border border-slate-800 rounded-2xl text-center space-y-4">
      <div className="relative">
        {isRecording && (
          <div className="absolute -inset-3 bg-teal-500/30 rounded-full animate-ping pointer-events-none" />
        )}

        <button
          onClick={isRecording ? onStopRecording : onStartRecording}
          disabled={isProcessing}
          className={`relative w-20 h-20 rounded-full flex items-center justify-center transition-all shadow-2xl ${
            isRecording
              ? 'bg-rose-600 hover:bg-rose-500 text-white ring-4 ring-rose-500/40'
              : 'bg-teal-500 hover:bg-teal-400 text-slate-950 ring-4 ring-teal-500/30'
          }`}
        >
          {isProcessing ? (
            <Loader2 className="w-8 h-8 animate-spin" />
          ) : isRecording ? (
            <Square className="w-8 h-8 fill-current" />
          ) : (
            <Mic className="w-9 h-9" />
          )}
        </button>
      </div>

      <div>
        <h4 className="font-extrabold text-slate-100 text-base">
          {isProcessing
            ? 'Processing Voice Query...'
            : isRecording
            ? 'Listening... Speak Your Query'
            : 'Tap Microphone to Speak'}
        </h4>
        <p className="text-xs text-slate-400 mt-0.5">
          Ask questions in Hindi, Marathi, English, Tamil, Telugu & 5 more Indian languages.
        </p>
      </div>
    </div>
  );
};
