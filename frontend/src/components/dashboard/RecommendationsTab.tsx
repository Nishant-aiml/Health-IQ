/* --------------------------------------------------
 * File: RecommendationsTab.tsx
 * Purpose: Prioritized AI recommendation list component with Evidence Accordion & Limitations.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2C Results Dashboard
 * -------------------------------------------------- */

import React from 'react';
import { Card } from '../ui/Card';
import { Badge } from '../ui/Badge';
import { Sparkles, Tag } from 'lucide-react';
import { EvidenceAccordion } from './EvidenceAccordion';
import { LimitationsCard } from './LimitationsCard';

export interface RecommendationItem {
  recommendation_id: string;
  title: string;
  summary: string;
  explanation: string;
  severity: string;
  priority: string;
  category: string;
  supporting_parameters: string[];
  confidence: string;
  recommendation_type: string;
  generated_by: string;
}

export interface EvidenceItem {
  parameter_name: string;
  observed_value: number;
  unit: string;
  normal_range: string;
  severity: string;
  detected_pattern?: string;
  reasoning_chain: string[];
}

export interface LimitationItem {
  notice: string;
  disclaimer_type: string;
  clinical_context_required: boolean;
}

interface RecommendationsTabProps {
  recommendations: RecommendationItem[];
  evidenceChains: EvidenceItem[];
  limitations: LimitationItem[];
}

export const RecommendationsTab: React.FC<RecommendationsTabProps> = ({
  recommendations,
  evidenceChains,
  limitations,
}) => {
  const getPriorityBadge = (priority: string) => {
    if (priority === 'CRITICAL') return <Badge variant="danger">Critical Priority</Badge>;
    if (priority === 'HIGH') return <Badge variant="danger">High Priority</Badge>;
    if (priority === 'MEDIUM') return <Badge variant="warning">Medium Priority</Badge>;
    return <Badge variant="info">Informational</Badge>;
  };

  return (
    <div className="space-y-6">
      {/* Mandatory Limitations Card Header */}
      <LimitationsCard limitations={limitations} />

      <div className="space-y-4">
        <h3 className="text-lg font-bold text-slate-900 dark:text-slate-100 flex items-center">
          <Sparkles className="w-5 h-5 mr-2 text-brand-600 dark:text-brand-400" />
          Clinical Action Recommendations ({recommendations.length})
        </h3>

        <div className="space-y-4">
          {recommendations.map((rec) => (
            <Card key={rec.recommendation_id} className="space-y-3">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div className="flex items-center space-x-2">
                  <h4 className="text-base font-bold text-slate-900 dark:text-slate-100">
                    {rec.title}
                  </h4>
                  {getPriorityBadge(rec.priority)}
                </div>
                <span className="text-xs font-semibold text-slate-400 capitalize">
                  Category: {rec.category.replace('_', ' ')}
                </span>
              </div>

              <p className="text-sm font-semibold text-slate-800 dark:text-slate-200">
                {rec.summary}
              </p>
              <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                {rec.explanation}
              </p>

              <div className="flex flex-wrap items-center gap-1.5 pt-1">
                <Tag className="w-3.5 h-3.5 text-slate-400" />
                <span className="text-xs text-slate-400 font-medium">Supporting Parameters:</span>
                {rec.supporting_parameters.map((param, pIdx) => (
                  <span
                    key={pIdx}
                    className="text-[11px] font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 px-2 py-0.5 rounded-md"
                  >
                    {param}
                  </span>
                ))}
              </div>

              {/* Explicit Evidence Chain Accordion for this recommendation */}
              <div className="pt-2">
                <EvidenceAccordion
                  evidenceChains={evidenceChains.filter((e) =>
                    rec.supporting_parameters.includes(e.parameter_name)
                  )}
                />
              </div>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
};
