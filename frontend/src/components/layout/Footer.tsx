import React from 'react';
import { Link } from 'react-router-dom';
import { Activity, Heart } from 'lucide-react';

export const Footer: React.FC = () => (
  <footer className="border-t border-slate-200 bg-white py-8 mt-auto text-xs text-slate-500">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div className="flex items-center gap-2.5">
        <div className="w-7 h-7 rounded-lg bg-teal-600 flex items-center justify-center text-white">
          <Activity className="w-4 h-4" />
        </div>
        <span className="font-bold text-slate-800">HealthLens AI</span>
      </div>

      <nav className="flex items-center gap-4 text-slate-600 font-medium">
        <Link to="/" className="hover:text-teal-600">Overview</Link>
        <Link to="/upload" className="hover:text-teal-600">Upload</Link>
        <Link to="/voice" className="hover:text-teal-600">AI Assistant</Link>
        <Link to="/clinical" className="hover:text-teal-600">Doctor Hub</Link>
      </nav>

      <p className="flex items-center gap-1 text-slate-500">
        Made with <Heart className="w-3.5 h-3.5 text-rose-500 fill-rose-500" /> for your health
      </p>
    </div>
  </footer>
);
