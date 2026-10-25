/* --------------------------------------------------
 * File: SuggestedQuestions.tsx
 * Purpose: Quick-suggestion question chips shown before and during chat interaction.
 * Module: Frontend Chat Components
 * Used By: ChatWindow
 * Future Phase: Phase 2D Grounded Chat
 * -------------------------------------------------- */

import React from 'react';
import { HelpCircle } from 'lucide-react';

interface SuggestedQuestionsProps {
  onSelectQuestion: (question: string) => void;
}

const SUGGESTIONS = [
  "What does my health score mean?",
  "Explain my abnormal lab values.",
  "What should I discuss with my doctor?",
  "Summarize this lab report.",
];

export const SuggestedQuestions: React.FC<SuggestedQuestionsProps> = ({ onSelectQuestion }) => {
  return (
    <div className="space-y-2">
      <div className="flex items-center space-x-1.5 text-xs font-semibold text-slate-500 dark:text-slate-400">
        <HelpCircle className="w-3.5 h-3.5 text-brand-600 dark:text-brand-400" />
        <span>Suggested Questions:</span>
      </div>
      <div className="flex flex-wrap gap-2">
        {SUGGESTIONS.map((q, idx) => (
          <button
            key={idx}
            onClick={() => onSelectQuestion(q)}
            className="text-xs text-left bg-white dark:bg-slate-800 hover:bg-brand-50 dark:hover:bg-slate-700/80 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 px-3 py-2 rounded-xl shadow-xs transition-colors font-medium min-h-[44px] sm:min-h-[36px]"
          >
            "{q}"
          </button>
        ))}
      </div>
    </div>
  );
};
