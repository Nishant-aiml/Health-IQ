/* --------------------------------------------------
 * File: TypingIndicator.tsx
 * Purpose: Pulse animation typing indicator shown while AI generates grounded response.
 * Module: Frontend Chat Components
 * Used By: ChatWindow
 * Future Phase: Phase 2D Grounded Chat
 * -------------------------------------------------- */

import React from 'react';
import { Bot } from 'lucide-react';

export const TypingIndicator: React.FC = () => {
  return (
    <div className="flex items-center space-x-3 text-slate-400 animate-fade-in">
      <div className="w-8 h-8 rounded-full bg-teal-600 dark:bg-teal-500 flex items-center justify-center text-white flex-shrink-0">
        <Bot className="w-4 h-4" />
      </div>
      <div className="p-3 bg-white dark:bg-slate-900 border border-slate-200/80 dark:border-slate-800 rounded-2xl rounded-tl-none flex items-center space-x-1.5 shadow-xs">
        <span className="text-xs font-semibold text-slate-500 mr-1">Searching WHO/CDC/NIH guidelines</span>
        <div className="w-2 h-2 rounded-full bg-brand-600 animate-bounce" style={{ animationDelay: '0ms' }} />
        <div className="w-2 h-2 rounded-full bg-brand-600 animate-bounce" style={{ animationDelay: '150ms' }} />
        <div className="w-2 h-2 rounded-full bg-brand-600 animate-bounce" style={{ animationDelay: '300ms' }} />
      </div>
    </div>
  );
};
