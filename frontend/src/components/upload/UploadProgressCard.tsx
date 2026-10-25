/* --------------------------------------------------
 * File: UploadProgressCard.tsx
 * Purpose: Real-time per-file job status checklist progress component.
 * Module: Frontend Upload Components
 * Used By: UploadPage
 * Future Phase: Phase 2A Ingestion UI
 * -------------------------------------------------- */

import React, { useEffect, useState } from 'react';
import { Card } from '../ui/Card';
import { Badge } from '../ui/Badge';
import { CheckCircle2, AlertCircle, Loader2 } from 'lucide-react';

export interface JobStatusItem {
  job_id?: number;
  report_id: number;
  filename?: string;
  stage: string;
  status: string;
  error_reason?: string;
}

interface UploadProgressCardProps {
  batchId: string;
  jobIds: number[];
  onBatchComplete?: () => void;
}

export const UploadProgressCard: React.FC<UploadProgressCardProps> = ({
  batchId,
  jobIds,
  onBatchComplete,
}) => {
  const [statuses, setStatuses] = useState<JobStatusItem[]>([]);
  const [isDone, setIsDone] = useState(false);

  useEffect(() => {
    if (!batchId || jobIds.length === 0 || isDone) return;

    const pollStatus = async () => {
      try {
        const queryParams = jobIds.map((id) => `job_ids=${id}`).join('&');
        const response = await fetch(`/api/v1/documents/batch/${batchId}/status?${queryParams}`);
        if (response.ok) {
          const json = await response.json();
          if (json.data) {
            setStatuses(json.data);
            const allFinished = json.data.every(
              (item: JobStatusItem) => item.status === 'completed' || item.status === 'failed'
            );
            if (allFinished) {
              setIsDone(true);
              if (onBatchComplete) onBatchComplete();
            }
          }
        }
      } catch (err) {
        console.error('Status polling error:', err);
      }
    };

    pollStatus();
    const interval = setInterval(pollStatus, 2000);
    return () => clearInterval(interval);
  }, [batchId, jobIds, isDone, onBatchComplete]);

  const getStageBadge = (stage: string, status: string) => {
    if (status === 'completed') return <Badge variant="success">Completed ✓</Badge>;
    if (status === 'failed') return <Badge variant="danger">Failed ✕</Badge>;
    if (stage === 'extracting') return <Badge variant="info">Extracting (OCR)...</Badge>;
    if (stage === 'parsing') return <Badge variant="warning">Parsing Parameters...</Badge>;
    return <Badge variant="default">Queued</Badge>;
  };

  return (
    <Card header={
      <div className="flex justify-between items-center">
        <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100">
          Batch Processing Progress ({statuses.length}/{jobIds.length})
        </h4>
        {isDone ? (
          <Badge variant="success">Batch Finished</Badge>
        ) : (
          <div className="flex items-center text-xs text-brand-600 dark:text-brand-400 font-semibold">
            <Loader2 className="w-3.5 h-3.5 mr-1 animate-spin" /> Processing...
          </div>
        )}
      </div>
    }>
      <div className="space-y-3">
        {statuses.map((item, idx) => (
          <div
            key={item.job_id || item.report_id || idx}
            className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-xl border border-slate-200/80 dark:border-slate-800 flex items-center justify-between"
          >
            <div className="flex items-center space-x-3 truncate">
              {item.status === 'completed' ? (
                <CheckCircle2 className="w-5 h-5 text-emerald-500 flex-shrink-0" />
              ) : item.status === 'failed' ? (
                <AlertCircle className="w-5 h-5 text-rose-500 flex-shrink-0" />
              ) : (
                <Loader2 className="w-5 h-5 text-brand-500 animate-spin flex-shrink-0" />
              )}
              <div className="truncate">
                <p className="text-sm font-medium text-slate-900 dark:text-slate-100 truncate">
                  {item.filename || `Report #${item.report_id}`}
                </p>
                <p className="text-xs text-slate-400">Job #{item.job_id || item.report_id}</p>
              </div>
            </div>
            <div>{getStageBadge(item.stage, item.status)}</div>
          </div>
        ))}
      </div>
    </Card>
  );
};
