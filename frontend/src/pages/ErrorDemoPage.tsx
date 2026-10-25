/**
 * File: ErrorDemoPage.tsx
 * Purpose: Simple Light Theme Error & Recovery Demo Page.
 * Module: Frontend / Pages
 * Route: /error-demo
 */

import React, { useState } from 'react';
import { AlertTriangle, RefreshCw, CheckCircle, ArrowLeft } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export const ErrorDemoPage: React.FC = () => {
  const navigate = useNavigate();
  const [retrying, setRetrying] = useState(false);

  const handleRetry = () => {
    setRetrying(true);
    setTimeout(() => setRetrying(false), 1200);
  };

  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
      <div className="bg-white border border-slate-200 rounded-2xl p-6 text-center space-y-4 max-w-md shadow-sm">
        <div className="w-12 h-12 rounded-xl bg-amber-50 border border-amber-200 text-amber-600 flex items-center justify-center mx-auto">
          <AlertTriangle className="w-6 h-6" />
        </div>

        <div className="space-y-1">
          <h1 className="text-lg font-bold text-slate-900">System Recovery Mode</h1>
          <p className="text-xs text-slate-600 leading-relaxed">
            HealthLens AI includes built-in graceful recovery. If an API call drops momentarily, your progress is safely stored.
          </p>
        </div>

        <div className="bg-slate-50 p-3.5 rounded-xl border border-slate-200 text-left text-xs space-y-1">
          <div className="flex items-center justify-between font-bold text-slate-900">
            <span>Connection Status</span>
            <span className="text-emerald-700 flex items-center gap-1"><CheckCircle className="w-3.5 h-3.5" /> Ready</span>
          </div>
          <p className="text-slate-500 text-[11px]">All session data is stored safely.</p>
        </div>

        <div className="flex gap-2 pt-2">
          <button
            onClick={handleRetry}
            disabled={retrying}
            className="flex-1 py-2.5 rounded-xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-xs flex items-center justify-center gap-2"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${retrying ? 'animate-spin' : ''}`} />
            {retrying ? 'Retrying...' : 'Test Connection'}
          </button>

          <button
            onClick={() => navigate('/')}
            className="flex-1 py-2.5 rounded-xl font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 text-xs flex items-center justify-center gap-2"
          >
            <ArrowLeft className="w-3.5 h-3.5" /> Return Home
          </button>
        </div>
      </div>
    </div>
  );
};
