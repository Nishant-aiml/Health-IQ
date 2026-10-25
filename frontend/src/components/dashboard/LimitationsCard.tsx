/* --------------------------------------------------
 * File: LimitationsCard.tsx
 * Purpose: Mandatory clinical disclaimer and limitations notice card component.
 * Module: Frontend Dashboard Components
 * Used By: RecommendationsTab
 * Future Phase: Phase 2C Results Dashboard
 * -------------------------------------------------- */

import React from 'react';
import { LimitationItem } from './RecommendationsTab';
import { AlertCircle } from 'lucide-react';

interface LimitationsCardProps {
  limitations: LimitationItem[];
}

export const LimitationsCard: React.FC<LimitationsCardProps> = ({ limitations }) => {
  if (!limitations || limitations.length === 0) return null;

  return (
    <div className="p-4 bg-amber-500/10 dark:bg-amber-950/30 border border-amber-500/30 rounded-2xl space-y-2 text-amber-900 dark:text-amber-200">
      <div className="flex items-center space-x-2 font-bold text-xs">
        <AlertCircle className="w-4 h-4 text-amber-600 dark:text-amber-400 flex-shrink-0" />
        <span>Clinical Context & Mandatory Limitations</span>
      </div>
      <ul className="space-y-1 text-xs opacity-90 pl-6 list-disc">
        {limitations.map((lim, idx) => (
          <li key={idx}>{lim.notice}</li>
        ))}
      </ul>
    </div>
  );
};
