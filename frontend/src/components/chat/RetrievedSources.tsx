/* --------------------------------------------------
 * File: RetrievedSources.tsx
 * Purpose: Collapsible Evidence Drawer displaying retrieved guideline chunks, organization badges, and relevance scores.
 * Module: Frontend Chat Components
 * Used By: MessageBubble
 * Future Phase: Phase 2D Grounded Chat
 * -------------------------------------------------- */

import React, { useState } from 'react';
import { ChevronDown, ChevronUp, Database, ExternalLink } from 'lucide-react';

export interface RetrievedChunkItem {
  chunk_id: string;
  title: string;
  source: string;
  score: number;
  excerpt: string;
}

interface RetrievedSourcesProps {
  sources: RetrievedChunkItem[];
}

export const RetrievedSources: React.FC<RetrievedSourcesProps> = ({ sources }) => {
  const [isOpen, setIsOpen] = useState(false);

  if (!sources || sources.length === 0) return null;

  return (
    <div className="border border-slate-200/80 dark:border-slate-800 rounded-2xl overflow-hidden bg-slate-50/50 dark:bg-slate-800/40 mt-2">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full p-2.5 flex items-center justify-between text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-100/60 dark:hover:bg-slate-800/60 transition-colors min-h-[44px]"
      >
        <div className="flex items-center space-x-2">
          <Database className="w-3.5 h-3.5 text-brand-600 dark:text-brand-400" />
          <span>Retrieved Guideline Evidence ({sources.length} sources)</span>
        </div>
        {isOpen ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
      </button>

      {isOpen && (
        <div className="p-3 pt-0 space-y-2 text-xs divide-y divide-slate-200/60 dark:divide-slate-800 animate-fade-in">
          {sources.map((src, idx) => (
            <div key={idx} className="pt-2 space-y-1">
              <div className="flex items-center justify-between font-bold text-slate-900 dark:text-slate-100">
                <span className="flex items-center">
                  <ExternalLink className="w-3 h-3 mr-1 text-slate-400" />
                  {src.title}
                </span>
                <span className="text-[10px] font-semibold bg-brand-100 dark:bg-brand-950 text-brand-700 dark:text-brand-300 px-2 py-0.5 rounded-md">
                  {src.source} • Score: {src.score}
                </span>
              </div>
              <p className="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed italic">
                "{src.excerpt}"
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
