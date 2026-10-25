/**
 * File: TimelineFilters.tsx
 * Purpose: Biomarker filter pills for selecting historical trend views (All, Hemoglobin, Glucose, Cholesterol, BP).
 * Module: Frontend / Components / History
 * Used By: HistoryPage Component
 * Future Phase: Phase 3B Longitudinal Health Intelligence
 */

import React from 'react';
import { Filter } from 'lucide-react';

interface TimelineFiltersProps {
  selectedFilter: string;
  onSelectFilter: (filter: string) => void;
  availableBiomarkers: string[];
}

export const TimelineFilters: React.FC<TimelineFiltersProps> = ({
  selectedFilter,
  onSelectFilter,
  availableBiomarkers,
}) => {
  return (
    <div className="flex items-center gap-2 overflow-x-auto pb-2 my-4">
      <div className="flex items-center gap-1.5 text-xs text-slate-400 font-semibold mr-2 shrink-0">
        <Filter className="w-3.5 h-3.5 text-teal-400" /> Filter Biomarkers:
      </div>

      <button
        onClick={() => onSelectFilter('ALL')}
        className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition-all shrink-0 ${
          selectedFilter === 'ALL'
            ? 'bg-teal-500 text-slate-950 shadow-md shadow-teal-500/20 font-bold'
            : 'bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200'
        }`}
      >
        All Biomarkers
      </button>

      {availableBiomarkers.map((b) => (
        <button
          key={b}
          onClick={() => onSelectFilter(b)}
          className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition-all shrink-0 ${
            selectedFilter === b
              ? 'bg-teal-500 text-slate-950 shadow-md shadow-teal-500/20 font-bold'
              : 'bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200'
          }`}
        >
          {b}
        </button>
      ))}
    </div>
  );
};
