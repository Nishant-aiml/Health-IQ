/* --------------------------------------------------
 * File: FileDropzone.tsx
 * Purpose: Touch-friendly mobile-first file picker supporting PDF, Image, DOCX, and TXT files.
 * Module: Frontend Upload Components
 * Used By: UploadPage
 * Future Phase: Phase 2A Ingestion UI
 * -------------------------------------------------- */

import React, { useRef } from 'react';
import { UploadCloud, FileText } from 'lucide-react';
import { Button } from '../ui/Button';

interface FileDropzoneProps {
  onFilesSelected: (files: File[]) => void;
  disabled?: boolean;
}

export const FileDropzone: React.FC<FileDropzoneProps> = ({ onFilesSelected, disabled }) => {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      onFilesSelected(Array.from(e.target.files));
    }
  };

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onFilesSelected(Array.from(e.dataTransfer.files));
    }
  };

  return (
    <div
      onDragOver={handleDragOver}
      onDrop={handleDrop}
      onClick={() => fileInputRef.current?.click()}
      className="p-6 sm:p-10 border-2 border-dashed border-brand-300 dark:border-brand-800 rounded-3xl bg-brand-50/20 dark:bg-brand-950/10 hover:bg-brand-50/50 dark:hover:bg-brand-950/20 transition-all cursor-pointer text-center flex flex-col items-center justify-center space-y-4 shadow-sm"
    >
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileChange}
        multiple
        accept=".pdf,.png,.jpg,.jpeg,.docx,.txt"
        className="hidden"
        disabled={disabled}
      />
      <div className="p-4 bg-brand-100 dark:bg-brand-950/60 text-brand-700 dark:text-brand-300 rounded-2xl">
        <UploadCloud className="w-8 h-8 sm:w-10 sm:h-10" />
      </div>
      <div>
        <h3 className="text-base sm:text-lg font-bold text-slate-900 dark:text-slate-100">
          Upload Lab Reports or Prescriptions
        </h3>
        <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-xs sm:max-w-md mx-auto">
          Tap or drag and drop single or multiple files (PDF, PNG, JPG, DOCX, TXT).
        </p>
      </div>
      <Button variant="outline" size="sm" className="min-h-[44px]">
        <FileText className="w-4 h-4 mr-2" /> Select Files
      </Button>
    </div>
  );
};
