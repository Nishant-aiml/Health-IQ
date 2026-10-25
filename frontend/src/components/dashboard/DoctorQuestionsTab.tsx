/* --------------------------------------------------
 * File: DoctorQuestionsTab.tsx
 * Purpose: Pattern-aware doctor consultation discussion questions list component.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2C Results Dashboard
 * -------------------------------------------------- */

import React from 'react';
import { Card } from '../ui/Card';
import { Badge } from '../ui/Badge';
import { MessageSquare, CheckSquare } from 'lucide-react';

export interface DoctorQuestionItem {
  question_text: string;
  target_parameter: string;
  clinical_rationale: string;
  priority: string;
}

interface DoctorQuestionsTabProps {
  questions: DoctorQuestionItem[];
}

export const DoctorQuestionsTab: React.FC<DoctorQuestionsTabProps> = ({ questions }) => {
  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-bold text-slate-900 dark:text-slate-100 flex items-center">
          <MessageSquare className="w-5 h-5 mr-2 text-brand-600 dark:text-brand-400" />
          Doctor Consultation Discussion Checklist ({questions.length})
        </h3>
      </div>
      <p className="text-xs text-slate-500 dark:text-slate-400">
        Bring these pattern-aware questions to your next physician or specialist consultation.
      </p>

      <div className="space-y-3">
        {questions.map((q, idx) => (
          <Card key={idx} className="space-y-2">
            <div className="flex items-start justify-between">
              <div className="flex items-start space-x-3">
                <CheckSquare className="w-5 h-5 text-brand-600 dark:text-brand-400 flex-shrink-0 mt-0.5" />
                <div>
                  <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100 leading-snug">
                    "{q.question_text}"
                  </h4>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                    <strong className="text-slate-700 dark:text-slate-300">Why ask this:</strong> {q.clinical_rationale}
                  </p>
                </div>
              </div>
              <Badge variant={q.priority === 'HIGH' || q.priority === 'CRITICAL' ? 'danger' : 'info'}>
                {q.target_parameter}
              </Badge>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
