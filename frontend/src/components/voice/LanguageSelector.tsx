/**
 * File: LanguageSelector.tsx
 * Purpose: Regional Indian language selector supporting 10 languages (English, Hindi, Marathi, Tamil, Telugu, etc.).
 * Module: Frontend / Components / Voice
 * Used By: VoiceAssistantPage Component
 * Future Phase: Phase 3D Multilingual & Voice AI
 */

import React from 'react';
import { Globe } from 'lucide-react';

export interface LanguageOption {
  code: string;
  name: string;
  nativeName: string;
}

export const LANGUAGES: LanguageOption[] = [
  { code: 'en', name: 'English', nativeName: 'English' },
  { code: 'hi', name: 'Hindi', nativeName: 'हिंदी' },
  { code: 'mr', name: 'Marathi', nativeName: 'मराठी' },
  { code: 'ta', name: 'Tamil', nativeName: 'தமிழ்' },
  { code: 'te', name: 'Telugu', nativeName: 'తెలుగు' },
  { code: 'gu', name: 'Gujarati', nativeName: 'ગુજરાતી' },
  { code: 'pa', name: 'Punjabi', nativeName: 'ਪੰਜਾਬੀ' },
  { code: 'bn', name: 'Bengali', nativeName: 'বাংলা' },
  { code: 'ml', name: 'Malayalam', nativeName: 'മലയാളം' },
  { code: 'kn', name: 'Kannada', nativeName: 'ಕನ್ನಡ' },
];

interface LanguageSelectorProps {
  selectedLang: string;
  onSelectLanguage: (code: string) => void;
}

export const LanguageSelector: React.FC<LanguageSelectorProps> = ({ selectedLang, onSelectLanguage }) => {
  return (
    <div className="flex items-center gap-2 bg-slate-950/80 border border-slate-800 p-2 rounded-xl text-xs">
      <Globe className="w-4 h-4 text-teal-400 shrink-0" />
      <span className="text-slate-400 font-medium">Language:</span>
      <select
        value={selectedLang}
        onChange={(e) => onSelectLanguage(e.target.value)}
        className="bg-slate-900 text-slate-100 font-bold border border-slate-700 rounded-lg px-2.5 py-1 text-xs focus:outline-none focus:border-teal-500"
      >
        {LANGUAGES.map((lang) => (
          <option key={lang.code} value={lang.code}>
            {lang.name} ({lang.nativeName})
          </option>
        ))}
      </select>
    </div>
  );
};
