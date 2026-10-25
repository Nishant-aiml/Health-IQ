/**
 * File: UploadPage.tsx
 * Purpose: Simple Light Theme Document Upload & Progress Pipeline Visualizer.
 * Module: Frontend / Pages
 * Route: /upload
 */

import React, { useState, useCallback, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Upload, FileText, X, AlertCircle,
  Loader2, Sparkles, ClipboardList,
  Check
} from 'lucide-react';

interface FileItem {
  id: string;
  file: File;
  previewUrl?: string;
}

interface JobStatus {
  job_id: number;
  report_id?: number;
  filename: string;
  status: string;
  stage?: string;
  error_reason?: string;
}

const PIPELINE_STAGES = [
  { id: 'ocr', label: '1. Scanning Document & Tables', desc: 'Running multi-tier OCR text extraction' },
  { id: 'parsing', label: '2. Normalizing Biomarkers', desc: 'Standardizing units & reference ranges' },
  { id: 'reasoning', label: '3. Clinical Pattern Reasoning', desc: 'Checking guidelines & calculating health score' },
  { id: 'dashboard', label: '4. Assembling Personal Dashboard', desc: 'Preparing plain-language insights & recommendations' },
];

export const UploadPage: React.FC = () => {
  const navigate = useNavigate();
  const [mode, setMode] = useState<'file' | 'text'>('file');
  const [files, setFiles] = useState<FileItem[]>([]);
  const [pastedText, setPastedText] = useState('');
  const [isDragging, setIsDragging] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Batch Job Processing State
  const [batchId, setBatchId] = useState<string | null>(null);
  const [jobStatuses, setJobStatuses] = useState<JobStatus[]>([]);
  const [currentStageIdx, setCurrentStageIdx] = useState(0);

  const addFiles = useCallback((incomingFiles: FileList | File[]) => {
    const valid: FileItem[] = [];
    Array.from(incomingFiles).forEach(file => {
      const ext = file.name.split('.').pop()?.toLowerCase();
      if (!['pdf', 'png', 'jpg', 'jpeg', 'docx', 'txt'].includes(ext || '')) {
        setError(`"${file.name}" is not supported. Please upload PDF, PNG, JPG, DOCX, or TXT.`);
        return;
      }
      const item: FileItem = { id: `${file.name}-${Date.now()}`, file };
      if (file.type.startsWith('image/')) item.previewUrl = URL.createObjectURL(file);
      valid.push(item);
    });

    setFiles(prev => [...prev, ...valid]);
  }, []);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files.length) addFiles(e.dataTransfer.files);
  }, [addFiles]);

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.length) addFiles(e.target.files);
  };

  const removeFile = (id: string) => setFiles(prev => prev.filter(f => f.id !== id));

  useEffect(() => {
    if (!batchId) return;
    const interval = setInterval(() => {
      setCurrentStageIdx(prev => (prev < PIPELINE_STAGES.length - 1 ? prev + 1 : prev));
    }, 2000);
    return () => clearInterval(interval);
  }, [batchId]);

  const pollStatus = async (bId: string, jobIds: number[], filenames: string[]) => {
    const statuses: JobStatus[] = jobIds.map((id, i) => ({ job_id: id, status: 'queued', filename: filenames[i] }));
    setJobStatuses([...statuses]);

    let allDone = false;
    let attempts = 0;
    while (!allDone && attempts < 60) {
      await new Promise(r => setTimeout(r, 1200));
      attempts++;
      try {
        const query = jobIds.map(id => `job_ids=${id}`).join('&');
        const res = await fetch(`/api/v1/documents/batch/${bId}/status?${query}`);
        if (!res.ok) continue;
        const json = await res.json();
        const rawData = json.data;
        const jobs: JobStatus[] = Array.isArray(rawData) ? rawData : (rawData?.jobs || []);
        
        if (jobs.length > 0) {
          setJobStatuses(jobs.map((j: any, i: number) => ({ ...j, filename: filenames[i] || j.filename || `File ${i + 1}` })));
          allDone = jobs.every((j: any) => j.status === 'completed' || j.status === 'failed');
          const completed = jobs.find((j: any) => j.status === 'completed');
          if (completed?.report_id && allDone) {
            setTimeout(() => navigate(`/reports/${completed.report_id}`), 800);
          }
        }
      } catch {
        // continue polling
      }
    }
  };

  const handleUpload = async () => {
    if (isUploading) return;
    setError(null);
    setIsUploading(true);

    try {
      let filesToUpload: File[];

      if (mode === 'text') {
        if (!pastedText.trim()) { setError('Please enter some text first.'); setIsUploading(false); return; }
        const filename = `pasted_report_${Date.now()}.txt`;
        filesToUpload = [new File([pastedText], filename, { type: 'text/plain' })];
      } else {
        if (files.length === 0) { setError('Please add at least one file.'); setIsUploading(false); return; }
        filesToUpload = files.map(f => f.file);
      }

      const storedUser = localStorage.getItem('hl_user');
      const userId = storedUser ? JSON.parse(storedUser)?.id : 1;

      const formData = new FormData();
      filesToUpload.forEach(f => formData.append('files', f));
      formData.append('doc_type', 'lab_report');
      if (userId) formData.append('user_id', String(userId));

      const res = await fetch('/api/v1/documents/batch', { method: 'POST', body: formData });
      if (!res.ok) {
        const errJson = await res.json().catch(() => ({}));
        throw new Error(errJson.error?.message || `Upload failed (${res.status})`);
      }
      const json = await res.json();
      const { batch_id, job_ids } = json.data || {};
      if (batch_id && job_ids) {
        setBatchId(batch_id);
        const filenames = filesToUpload.map(f => f.name);
        setJobStatuses(job_ids.map((id: number, i: number) => ({ job_id: id, status: 'queued', filename: filenames[i] })));
        await pollStatus(batch_id, job_ids, filenames);
      }
    } catch (err: any) {
      setError(err.message || 'Upload failed. Please try again.');
    } finally {
      setIsUploading(false);
    }
  };

  // Processing Screen (Light Theme)
  if (batchId) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center px-4 py-12">
        <div className="w-full max-w-xl bg-white border border-slate-200 rounded-2xl p-8 space-y-6 shadow-sm">
          <div className="text-center space-y-2">
            <div className="w-16 h-16 rounded-2xl bg-teal-50 border border-teal-200 text-teal-600 flex items-center justify-center mx-auto">
              <Sparkles className="w-8 h-8" />
            </div>
            <h2 className="text-2xl font-bold text-slate-900">Analyzing Medical Report</h2>
            <p className="text-xs text-slate-600">Cross-referencing parameters against clinical guidelines.</p>
          </div>

          {/* Pipeline Stage Progress */}
          <div className="space-y-3 bg-slate-50 p-5 rounded-xl border border-slate-200">
            {PIPELINE_STAGES.map((stage, idx) => {
              const isDone = idx < currentStageIdx || jobStatuses.every(j => j.status === 'completed');
              const isCurrent = idx === currentStageIdx && !jobStatuses.every(j => j.status === 'completed');
              return (
                <div
                  key={stage.id}
                  className={`flex items-start gap-3 p-3 rounded-lg transition-all ${
                    isCurrent
                      ? 'bg-white border border-teal-300 text-slate-900 shadow-sm'
                      : isDone
                      ? 'text-slate-800'
                      : 'text-slate-400 opacity-60'
                  }`}
                >
                  <div className="mt-0.5 shrink-0">
                    {isDone ? (
                      <div className="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center text-xs font-bold">
                        <Check className="w-3.5 h-3.5" />
                      </div>
                    ) : isCurrent ? (
                      <Loader2 className="w-5 h-5 text-teal-600 animate-spin" />
                    ) : (
                      <div className="w-5 h-5 rounded-full bg-slate-200 text-slate-500 flex items-center justify-center text-[10px] font-bold">
                        {idx + 1}
                      </div>
                    )}
                  </div>
                  <div>
                    <h3 className="text-xs font-bold text-slate-900">{stage.label}</h3>
                    <p className="text-[11px] text-slate-500 mt-0.5">{stage.desc}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 py-8 text-slate-900">
      <div className="max-w-3xl mx-auto px-4 space-y-6">
        
        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-2xl sm:text-3xl font-bold text-slate-900">Upload Medical Report</h1>
          <p className="text-sm text-slate-600">Upload blood panel, lipid profile, or prescription for instant AI insights.</p>
        </div>

        {/* Mode Selector */}
        <div className="flex bg-white p-1 rounded-2xl border border-slate-200 shadow-sm max-w-xs mx-auto">
          <button
            onClick={() => setMode('file')}
            className={`flex-1 py-2 rounded-xl text-xs font-bold flex items-center justify-center gap-2 transition-all ${
              mode === 'file' ? 'bg-teal-600 text-white shadow-sm' : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <Upload className="w-4 h-4" /> Upload File
          </button>
          <button
            onClick={() => setMode('text')}
            className={`flex-1 py-2 rounded-xl text-xs font-bold flex items-center justify-center gap-2 transition-all ${
              mode === 'text' ? 'bg-teal-600 text-white shadow-sm' : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <ClipboardList className="w-4 h-4" /> Paste Text
          </button>
        </div>

        {error && (
          <div className="flex items-center gap-2 p-4 rounded-2xl bg-red-50 border border-red-200 text-red-700 text-xs font-medium">
            <AlertCircle className="w-4 h-4 shrink-0 text-red-600" />
            <span>{error}</span>
          </div>
        )}

        {/* Dropzone Card */}
        {mode === 'file' ? (
          <div className="space-y-4">
            <div
              onDragOver={e => { e.preventDefault(); setIsDragging(true); }}
              onDragLeave={() => setIsDragging(false)}
              onDrop={handleDrop}
              className={`bg-white border-2 border-dashed rounded-3xl p-10 text-center transition-all ${
                isDragging ? 'border-teal-500 bg-teal-50/50' : 'border-slate-300 hover:border-slate-400'
              }`}
            >
              <div className="w-14 h-14 rounded-2xl bg-teal-50 border border-teal-200 text-teal-600 flex items-center justify-center mx-auto mb-4">
                <Upload className="w-7 h-7" />
              </div>
              <h3 className="text-base font-bold text-slate-900">Drag & drop your medical report</h3>
              <p className="text-xs text-slate-500 mt-1">Supports PDF, PNG, JPG, DOCX, TXT (Up to 25MB)</p>

              <label className="inline-block mt-5 px-6 py-2.5 rounded-xl text-xs font-bold bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200 cursor-pointer transition-colors shadow-sm">
                Browse Files
                <input type="file" multiple accept=".pdf,.png,.jpg,.jpeg,.docx,.txt" onChange={handleFileInput} className="hidden" />
              </label>
            </div>

            {/* Selected File Previews */}
            {files.length > 0 && (
              <div className="space-y-2">
                <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider">Selected Files ({files.length})</h4>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {files.map(f => (
                    <div key={f.id} className="bg-white border border-slate-200 rounded-2xl p-3 flex items-center justify-between shadow-sm">
                      <div className="flex items-center gap-3 overflow-hidden">
                        {f.previewUrl ? (
                          <img src={f.previewUrl} alt="preview" className="w-10 h-10 object-cover rounded-lg border border-slate-200" />
                        ) : (
                          <div className="w-10 h-10 rounded-lg bg-teal-50 border border-teal-200 text-teal-600 flex items-center justify-center">
                            <FileText className="w-5 h-5" />
                          </div>
                        )}
                        <div className="truncate">
                          <p className="text-xs font-bold text-slate-900 truncate">{f.file.name}</p>
                          <p className="text-[10px] text-slate-500">{(f.file.size / 1024).toFixed(0)} KB</p>
                        </div>
                      </div>
                      <button onClick={() => removeFile(f.id)} className="text-slate-400 hover:text-red-600 p-1">
                        <X className="w-4 h-4" />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        ) : (
          /* Paste Text Mode */
          <div className="bg-white border border-slate-200 rounded-3xl p-6 space-y-3 shadow-sm">
            <label className="block text-xs font-bold text-slate-700">Paste Lab Report Text</label>
            <textarea
              rows={8}
              value={pastedText}
              onChange={e => setPastedText(e.target.value)}
              placeholder="Paste text from lab report, e.g. Hemoglobin 14.2 g/dL, Fasting Blood Sugar 98 mg/dL..."
              className="w-full p-4 border border-slate-200 rounded-2xl focus:outline-none focus:border-teal-600 text-xs text-slate-900"
            />
          </div>
        )}

        {/* Submit Button */}
        <button
          onClick={handleUpload}
          disabled={isUploading || (mode === 'file' && files.length === 0) || (mode === 'text' && !pastedText.trim())}
          className="w-full py-4 rounded-2xl font-bold text-sm bg-teal-600 hover:bg-teal-700 disabled:opacity-50 text-white flex items-center justify-center gap-2 shadow-md transition-all"
        >
          {isUploading ? <Loader2 className="w-5 h-5 animate-spin" /> : <Sparkles className="w-5 h-5" />}
          <span>{isUploading ? 'Analyzing Report...' : 'Analyze Report with AI'}</span>
        </button>

      </div>
    </div>
  );
};
