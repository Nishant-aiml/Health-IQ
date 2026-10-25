/* --------------------------------------------------
 * File: ParameterCard.tsx
 * Purpose: Severity-tagged lab parameter card with reserved tab placeholders.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2B Results Dashboard & Phase 2C/2D Placeholders
 * -------------------------------------------------- */

import React, { useState } from 'react';
import { Badge } from '../ui/Badge';
import { ChevronRight, Sparkles, BookOpen } from 'lucide-react';

export interface ParameterItem {
  id: number;
  canonical_name: string;
  value: number;
  unit: string;
  normal_range_low?: number;
  normal_range_high?: number;
  severity: string;
  is_critical?: boolean;
}

interface ParameterCardProps {
  parameter: ParameterItem;
  onSelect?: (param: ParameterItem) => void;
}

export const ParameterCard: React.FC<ParameterCardProps> = ({ parameter, onSelect }) => {
  const [activeTab, setActiveTab] = useState<'details' | 'recommendations' | 'evidence' | 'chat'>('details');

  const getSeverityBadge = (severity: string, is_critical?: boolean) => {
    if (is_critical || severity === 'critical') return <Badge variant="danger">Critical Risk</Badge>;
    if (severity === 'severe') return <Badge variant="danger">Severe Deviation</Badge>;
    if (severity === 'moderate') return <Badge variant="warning">Moderate Deviation</Badge>;
    if (severity === 'mild') return <Badge variant="warning">Mild Deviation</Badge>;
    return <Badge variant="success">Normal Range</Badge>;
  };

  return (
    <div className="p-4 sm:p-5 bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/80 dark:border-slate-800 shadow-sm hover:shadow-md transition-all">
      <div className="flex items-start justify-between">
        <div>
          <div className="flex items-center space-x-2">
            <h4 className="text-base sm:text-lg font-bold text-slate-900 dark:text-slate-100">
              {parameter.canonical_name}
            </h4>
            {getSeverityBadge(parameter.severity, parameter.is_critical)}
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Normal Baseline: {parameter.normal_range_low ?? 'N/A'} - {parameter.normal_range_high ?? 'N/A'} {parameter.unit}
          </p>
        </div>
        <div className="text-right">
          <span className="text-xl sm:text-2xl font-black text-slate-900 dark:text-slate-100">
            {parameter.value}
          </span>
          <span className="text-xs font-semibold text-slate-400 ml-1">{parameter.unit}</span>
        </div>
      </div>

      {/* Reserved Sub-tab Placeholders for Phase 2C/2D */}
      <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
        <div className="flex space-x-1">
          <button
            onClick={() => setActiveTab('details')}
            className={`px-2.5 py-1 rounded-lg text-xs font-medium min-h-[36px] ${
              activeTab === 'details' ? 'bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-slate-100' : 'text-slate-400'
            }`}
          >
            Range Details
          </button>
          <button
            onClick={() => setActiveTab('recommendations')}
            className={`px-2.5 py-1 rounded-lg text-xs font-medium min-h-[36px] flex items-center ${
              activeTab === 'recommendations' ? 'bg-brand-50 text-brand-700 dark:bg-brand-950/60 dark:text-brand-300' : 'text-slate-400'
            }`}
          >
            <Sparkles className="w-3 h-3 mr-1 text-brand-500" /> Recommendations
          </button>
          <button
            onClick={() => setActiveTab('evidence')}
            className={`px-2.5 py-1 rounded-lg text-xs font-medium min-h-[36px] flex items-center ${
              activeTab === 'evidence' ? 'bg-brand-50 text-brand-700 dark:bg-brand-950/60 dark:text-brand-300' : 'text-slate-400'
            }`}
          >
            <BookOpen className="w-3 h-3 mr-1 text-teal-500" /> Evidence
          </button>
        </div>

        {onSelect && (
          <button
            onClick={() => onSelect(parameter)}
            className="text-xs font-bold text-brand-600 dark:text-brand-400 flex items-center hover:underline min-h-[44px] px-2"
          >
            Inspect <ChevronRight className="w-4 h-4 ml-0.5" />
          </button>
        )}
      </div>

      {activeTab !== 'details' && (
        <div className="mt-2 p-3 bg-brand-50/40 dark:bg-brand-950/20 rounded-xl text-xs text-brand-700 dark:text-brand-300 border border-brand-200/50 dark:border-brand-900/50 animate-fade-in flex items-center justify-between">
          <span>AI Recommendations & Medical Evidence Engine active in Phase 2C.</span>
          <Badge variant="info">Upcoming Phase 2C</Badge>
        </div>
      )}
    </div>
  );
};
