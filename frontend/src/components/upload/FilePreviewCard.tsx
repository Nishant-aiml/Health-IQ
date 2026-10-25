/* --------------------------------------------------
 * File: FilePreviewCard.tsx
 * Purpose: Pre-upload file inspection and removal component.
 * Module: Frontend Upload Components
 * Used By: UploadPage
 * Future Phase: Phase 2A Ingestion UI
 * -------------------------------------------------- */

import React from 'react';
import { FileText, Trash2 } from 'lucide-react';
import { Card } from '../ui/Card';
import { Button } from '../ui/Button';

interface FilePreviewCardProps {
  files: File[];
  onRemoveFile: (index: number) => void;
  onClearAll: () => void;
  onSubmitUpload: () => void;
  isSubmitting?: boolean;
}

export const FilePreviewCard: React.FC<FilePreviewCardProps> = ({
  files,
  onRemoveFile,
  onClearAll,
  onSubmitUpload,
  isSubmitting = false,
}) => {
  if (files.length === 0) return null;

  return (
    <Card header={
      <div className="flex justify-between items-center">
        <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100">
          Selected Files ({files.length})
        </h4>
        <button
          onClick={onClearAll}
          className="text-xs text-rose-600 dark:text-rose-400 hover:underline min-h-[44px] px-2 flex items-center"
        >
          Clear All
        </button>
      </div>
    }>
      <div className="space-y-3">
        <div className="divide-y divide-slate-100 dark:divide-slate-800 border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden">
          {files.map((file, index) => (
            <div key={index} className="p-3 bg-white dark:bg-slate-900 flex items-center justify-between">
              <div className="flex items-center space-x-3 truncate">
                <div className="p-2 bg-slate-100 dark:bg-slate-800 rounded-lg text-slate-500">
                  <FileText className="w-4 h-4" />
                </div>
                <div className="truncate">
                  <p className="text-sm font-medium text-slate-900 dark:text-slate-100 truncate">
                    {file.name}
                  </p>
                  <p className="text-xs text-slate-400">
                    {(file.size / 1024).toFixed(1)} KB
                  </p>
                </div>
              </div>
              <button
                onClick={() => onRemoveFile(index)}
                className="p-2 text-slate-400 hover:text-rose-600 dark:hover:text-rose-400 transition-colors min-h-[44px] min-w-[44px] flex items-center justify-center"
                aria-label="Remove file"
              >
                <Trash2 className="w-4 h-4" />
              </button>
            </div>
          ))}
        </div>

        <div className="pt-2">
          <Button
            onClick={onSubmitUpload}
            isLoading={isSubmitting}
            className="w-full min-h-[44px]"
            size="lg"
          >
            Submit Document Batch ({files.length})
          </Button>
        </div>
      </div>
    </Card>
  );
};
