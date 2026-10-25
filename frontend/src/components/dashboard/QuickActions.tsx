/* --------------------------------------------------
 * File: QuickActions.tsx
 * Purpose: Export Toolbar component with one-click buttons for Download PDF, Export JSON, Export CSV.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2E Export Toolbar
 * -------------------------------------------------- */

import React, { useState } from 'react';
import { Download, FileText, Code, Table, Check, Loader2 } from 'lucide-react';

interface QuickActionsProps {
  reportId: number;
}

export const QuickActions: React.FC<QuickActionsProps> = ({ reportId }) => {
  const [exporting, setExporting] = useState<'pdf' | 'json' | 'csv' | null>(null);
  const [success, setSuccess] = useState<'pdf' | 'json' | 'csv' | null>(null);

  const handleDownload = async (format: 'pdf' | 'json' | 'csv') => {
    try {
      setExporting(format);
      const url = `/api/v1/reports/${reportId}/${format}`;
      const response = await fetch(url);
      if (!response.ok) throw new Error(`Export failed (${response.status})`);

      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = downloadUrl;

      const ext = format === 'pdf' ? 'pdf' : format === 'json' ? 'json' : 'csv';
      link.download = `HealthLens_Medical_Report_${reportId}.${ext}`;
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(downloadUrl);

      setSuccess(format);
      setTimeout(() => setSuccess(null), 2500);
    } catch (err) {
      console.error(`Export ${format} error:`, err);
    } finally {
      setExporting(null);
    }
  };

  return (
    <div className="flex flex-wrap items-center gap-2.5 p-3 bg-slate-50 dark:bg-slate-900 rounded-2xl border border-slate-200/80 dark:border-slate-800">
      <div className="flex items-center space-x-1 text-xs font-bold text-slate-500 dark:text-slate-400 mr-2">
        <Download className="w-4 h-4 text-brand-600 dark:text-brand-400" />
        <span>Export Options:</span>
      </div>

      {/* Button 1: Download PDF */}
      <button
        onClick={() => handleDownload('pdf')}
        disabled={exporting !== null}
        className="inline-flex items-center text-xs font-bold bg-brand-600 hover:bg-brand-700 disabled:opacity-50 text-white px-3.5 py-2 rounded-xl transition-all shadow-xs min-h-[44px] sm:min-h-[36px]"
      >
        {exporting === 'pdf' ? (
          <Loader2 className="w-3.5 h-3.5 mr-1.5 animate-spin" />
        ) : success === 'pdf' ? (
          <Check className="w-3.5 h-3.5 mr-1.5 text-emerald-300" />
        ) : (
          <FileText className="w-3.5 h-3.5 mr-1.5" />
        )}
        <span>{exporting === 'pdf' ? 'Generating PDF...' : success === 'pdf' ? 'Downloaded PDF!' : 'Download PDF Report'}</span>
      </button>

      {/* Button 2: Export JSON */}
      <button
        onClick={() => handleDownload('json')}
        disabled={exporting !== null}
        className="inline-flex items-center text-xs font-semibold bg-white dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700/80 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 px-3 py-2 rounded-xl transition-all min-h-[44px] sm:min-h-[36px]"
      >
        {exporting === 'json' ? (
          <Loader2 className="w-3.5 h-3.5 mr-1.5 animate-spin" />
        ) : success === 'json' ? (
          <Check className="w-3.5 h-3.5 mr-1.5 text-emerald-500" />
        ) : (
          <Code className="w-3.5 h-3.5 mr-1.5 text-slate-500" />
        )}
        <span>{exporting === 'json' ? 'Exporting...' : 'Export JSON'}</span>
      </button>

      {/* Button 3: Export CSV */}
      <button
        onClick={() => handleDownload('csv')}
        disabled={exporting !== null}
        className="inline-flex items-center text-xs font-semibold bg-white dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700/80 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 px-3 py-2 rounded-xl transition-all min-h-[44px] sm:min-h-[36px]"
      >
        {exporting === 'csv' ? (
          <Loader2 className="w-3.5 h-3.5 mr-1.5 animate-spin" />
        ) : success === 'csv' ? (
          <Check className="w-3.5 h-3.5 mr-1.5 text-emerald-500" />
        ) : (
          <Table className="w-3.5 h-3.5 mr-1.5 text-slate-500" />
        )}
        <span>{exporting === 'csv' ? 'Exporting...' : 'Export CSV'}</span>
      </button>
    </div>
  );
};
