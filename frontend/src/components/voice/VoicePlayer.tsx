/**
 * File: VoicePlayer.tsx
 * Purpose: Speech synthesis audio player with Senior Mode speed controls (1.0x / 0.85x).
 * Module: Frontend / Components / Voice
 * Used By: VoiceAssistantPage & ConversationHistory Components
 * Future Phase: Phase 3D Multilingual & Voice AI
 */

import React, { useState } from 'react';
import { Volume2, Play, Pause, FastForward } from 'lucide-react';

interface VoicePlayerProps {
  text: string;
  languageCode: string;
  seniorMode: boolean;
}

export const VoicePlayer: React.FC<VoicePlayerProps> = ({ text, languageCode, seniorMode }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [rate, setRate] = useState<number>(seniorMode ? 0.85 : 1.0);

  const handlePlaySpeech = () => {
    if ('speechSynthesis' in window) {
      if (isPlaying) {
        window.speechSynthesis.cancel();
        setIsPlaying(false);
        return;
      }

      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = rate;
      
      const langCodes: Record<string, string> = {
        hi: 'hi-IN',
        mr: 'mr-IN',
        ta: 'ta-IN',
        te: 'te-IN',
        gu: 'gu-IN',
        pa: 'pa-IN',
        bn: 'bn-IN',
        ml: 'ml-IN',
        kn: 'kn-IN',
        en: 'en-US',
      };
      utterance.lang = langCodes[languageCode] || 'en-US';

      utterance.onend = () => setIsPlaying(false);
      utterance.onerror = () => setIsPlaying(false);

      setIsPlaying(true);
      window.speechSynthesis.speak(utterance);
    }
  };

  return (
    <div className="flex items-center justify-between bg-slate-950/90 border border-slate-800 p-3 rounded-xl text-xs mt-3">
      <div className="flex items-center gap-2">
        <button
          onClick={handlePlaySpeech}
          className="p-2 bg-teal-500 hover:bg-teal-400 text-slate-950 rounded-lg font-bold flex items-center gap-1 transition-all"
        >
          {isPlaying ? <Pause className="w-4 h-4 fill-current" /> : <Play className="w-4 h-4 fill-current" />}
          <span>{isPlaying ? 'Pause Audio' : 'Listen to Answer'}</span>
        </button>

        <span className="text-slate-400 font-semibold flex items-center gap-1">
          <Volume2 className="w-3.5 h-3.5 text-teal-400" /> TTS Voice Synthesizer
        </span>
      </div>

      <div className="flex items-center gap-1.5 bg-slate-900 px-2 py-1 rounded-lg border border-slate-800">
        <FastForward className="w-3 h-3 text-slate-400" />
        <span className="text-[10px] text-slate-400 font-bold">Speed:</span>
        <button
          onClick={() => setRate(0.85)}
          className={`px-1.5 py-0.5 rounded text-[10px] font-bold ${
            rate === 0.85 ? 'bg-amber-500 text-slate-950' : 'text-slate-400 hover:text-slate-200'
          }`}
        >
          0.85x (Senior)
        </button>
        <button
          onClick={() => setRate(1.0)}
          className={`px-1.5 py-0.5 rounded text-[10px] font-bold ${
            rate === 1.0 ? 'bg-teal-500 text-slate-950' : 'text-slate-400 hover:text-slate-200'
          }`}
        >
          1.0x
        </button>
      </div>
    </div>
  );
};
