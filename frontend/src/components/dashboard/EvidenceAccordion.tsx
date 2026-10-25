/* --------------------------------------------------
 * File: EvidenceAccordion.tsx
 * Purpose: Reasoning chain evidence accordion component explaining why recommendations were generated.
 * Module: Frontend Dashboard Components
 * Used By: RecommendationsTab
 * Future Phase: Phase 2C Results Dashboard
 * -------------------------------------------------- */

import React, { useState } from 'react';
import { ChevronDown, ChevronUp, Layers, CheckCircle2 } from 'lucide-react';
import { EvidenceItem } from './RecommendationsTab';

interface EvidenceAccordionProps {
  evidenceChains: EvidenceItem[];
}

export const EvidenceAccordion: React.FC<EvidenceAccordionProps> = ({ evidenceChains }) => {
  const [isOpen, setIsOpen] = useState(false);

  if (!evidenceChains || evidenceChains.length === 0) return null;

  return (
    <div className="border border-slate-200/80 dark:border-slate-800 rounded-2xl overflow-hidden bg-slate-50/50 dark:bg-slate-800/30">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full p-3 flex items-center justify-between text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-100/60 dark:hover:bg-slate-800/60 transition-colors min-h-[44px]"
      >
        <div className="flex items-center space-x-2">
          <Layers className="w-4 h-4 text-teal-600 dark:text-teal-400" />
          <span>Why this recommendation? (Explainable Reasoning Chain)</span>
        </div>
        {isOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
      </button>

      {isOpen && (
        <div className="p-3.5 pt-0 space-y-3 divide-y divide-slate-200/60 dark:divide-slate-800 text-xs animate-fade-in">
          {evidenceChains.map((chain, idx) => (
            <div key={idx} className="pt-2 space-y-1.5">
              <div className="flex items-center justify-between font-bold text-slate-900 dark:text-slate-100">
                <span>{chain.parameter_name}</span>
                <span className="text-slate-500">Observed: {chain.observed_value} {chain.unit} (Normal: {chain.normal_range})</span>
              </div>
              <ul className="space-y-1 pl-2">
                {chain.reasoning_chain.map((step, sIdx) => (
                  <li key={sIdx} className="flex items-start space-x-1.5 text-slate-600 dark:text-slate-400">
                    <CheckCircle2 className="w-3.5 h-3.5 text-teal-500 flex-shrink-0 mt-0.5" />
                    <span>{step}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
