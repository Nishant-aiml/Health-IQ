/**
 * File: PrescriptionUploader.tsx
 * Purpose: Upload prescription images/PDF/DOCX/TXT files or paste prescription text for analysis.
 * Module: Frontend / Components / Prescription
 * Used By: Prescription Page
 * Future Phase: Phase 3A Medicine Intelligence
 */

import React, { useState } from 'react';
import { Upload, FileText, Clipboard, Sparkles, Loader2 } from 'lucide-react';

interface PrescriptionUploaderProps {
  onAnalyze: (payload: { file?: File; pastedText?: string }) => void;
  isLoading: boolean;
}

export const PrescriptionUploader: React.FC<PrescriptionUploaderProps> = ({ onAnalyze, isLoading }) => {
  const [activeTab, setActiveTab] = useState<'upload' | 'paste'>('upload');
  const [file, setFile] = useState<File | null>(null);
  const [pastedText, setPastedText] = useState<string>('');

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (activeTab === 'upload' && file) {
      onAnalyze({ file });
    } else if (activeTab === 'paste' && pastedText.trim()) {
      onAnalyze({ pastedText });
    }
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 mb-6 shadow-xl">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4 mb-4">
        <div>
          <h2 className="text-lg font-bold text-slate-100 flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-teal-400" /> Prescribe & Analyze Medicines
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Upload prescription images/PDFs/DOCX or paste doctor's prescription text.
          </p>
        </div>

        {/* Mode Switcher */}
        <div className="flex bg-slate-950 p-1 rounded-xl border border-slate-800">
          <button
            onClick={() => setActiveTab('upload')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
              activeTab === 'upload'
                ? 'bg-teal-500 text-slate-950 shadow-md shadow-teal-500/20'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Upload className="w-3.5 h-3.5" /> Upload File
          </button>
          <button
            onClick={() => setActiveTab('paste')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
              activeTab === 'paste'
                ? 'bg-teal-500 text-slate-950 shadow-md shadow-teal-500/20'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Clipboard className="w-3.5 h-3.5" /> Paste Text
          </button>
        </div>
      </div>

      <form onSubmit={handleSubmit}>
        {activeTab === 'upload' ? (
          <div className="border-2 border-dashed border-slate-800 hover:border-teal-500/50 rounded-xl p-8 text-center transition-all bg-slate-950/40">
            <input
              type="file"
              id="prescription-file-input"
              accept=".pdf,.png,.jpg,.jpeg,.docx,.txt"
              onChange={handleFileChange}
              className="hidden"
            />
            <label htmlFor="prescription-file-input" className="cursor-pointer flex flex-col items-center">
              <div className="p-4 bg-teal-500/10 text-teal-400 rounded-2xl mb-3 border border-teal-500/20">
                <FileText className="w-8 h-8" />
              </div>
              <span className="text-sm font-semibold text-slate-200 mb-1">
                {file ? file.name : 'Click to upload prescription file'}
              </span>
              <span className="text-xs text-slate-400">Supports PDF, PNG, JPG, DOCX, TXT</span>
            </label>
          </div>
        ) : (
          <div>
            <textarea
              rows={5}
              value={pastedText}
              onChange={(e) => setPastedText(e.target.value)}
              placeholder="e.g. Tab. Glycomet 500mg BD PC 7 days&#10;Cap. Augmentin 625mg TDS PC 5 days&#10;Tab. Atorvastatin 10mg HS"
              className="w-full bg-slate-950 border border-slate-800 rounded-xl p-4 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-teal-500"
            />
          </div>
        )}

        <div className="mt-4 flex justify-end">
          <button
            type="submit"
            disabled={isLoading || (activeTab === 'upload' && !file) || (activeTab === 'paste' && !pastedText.trim())}
            className="bg-teal-500 hover:bg-teal-400 disabled:opacity-50 text-slate-950 font-bold px-6 py-2.5 rounded-xl text-xs flex items-center gap-2 transition-all shadow-lg shadow-teal-500/20"
          >
            {isLoading ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" /> Analyzing Prescription...
              </>
            ) : (
              <>
                <Sparkles className="w-4 h-4" /> Run Medicine Intelligence Analysis
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
};
