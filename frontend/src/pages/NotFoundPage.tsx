/**
 * File: NotFoundPage.tsx
 * Purpose: Simple Light Theme 404 Page.
 * Module: Frontend / Pages
 */

import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Home } from 'lucide-react';

export const NotFoundPage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-4">
      <div className="bg-white border border-slate-200 rounded-2xl p-6 text-center space-y-4 max-w-sm shadow-sm">
        <div className="w-12 h-12 rounded-xl bg-teal-50 border border-teal-200 text-teal-700 font-black text-xl flex items-center justify-center mx-auto">
          404
        </div>
        <div className="space-y-1">
          <h1 className="text-base font-bold text-slate-900">Page Not Found</h1>
          <p className="text-xs text-slate-600">The requested page does not exist or has been moved.</p>
        </div>
        <button
          onClick={() => navigate('/')}
          className="w-full py-2.5 rounded-xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-xs flex items-center justify-center gap-2"
        >
          <Home className="w-4 h-4" /> Return to Overview
        </button>
      </div>
    </div>
  );
};
