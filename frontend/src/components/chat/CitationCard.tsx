/* --------------------------------------------------
 * File: CitationCard.tsx
 * Purpose: Grounded medical citation badge component displaying WHO/CDC/NIH/ICMR provenance metadata.
 * Module: Frontend Chat Components
 * Used By: MessageBubble
 * Future Phase: Phase 2D Grounded Chat
 * -------------------------------------------------- */

import React from 'react';
import { Bookmark } from 'lucide-react';

export interface CitationItem {
  citation_id: string;
  source_organization: string;
  title: string;
  medical_topic: string;
  excerpt: string;
  relevance_score: number;
}

interface CitationCardProps {
  citation: CitationItem;
}

export const CitationCard: React.FC<CitationCardProps> = ({ citation }) => {
  const getBadgeColor = (source: string) => {
    if (source === 'WHO') return 'bg-sky-100 text-sky-800 dark:bg-sky-950 dark:text-sky-300';
    if (source === 'CDC') return 'bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300';
    if (source === 'NIH') return 'bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300';
    if (source === 'ICMR') return 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300';
    return 'bg-slate-100 text-slate-800 dark:bg-slate-800 dark:text-slate-300';
  };

  return (
    <div className="p-2.5 bg-white/90 dark:bg-slate-900/90 rounded-xl border border-slate-200/80 dark:border-slate-800 space-y-1 text-xs">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-1.5 font-bold text-slate-800 dark:text-slate-200">
          <Bookmark className="w-3.5 h-3.5 text-brand-600 dark:text-brand-400" />
          <span>{citation.title}</span>
        </div>
        <span className={`text-[10px] font-bold px-2 py-0.5 rounded-md ${getBadgeColor(citation.source_organization)}`}>
          {citation.source_organization}
        </span>
      </div>
      <p className="text-[11px] text-slate-500 dark:text-slate-400 italic">
        "{citation.excerpt}"
      </p>
    </div>
  );
};
