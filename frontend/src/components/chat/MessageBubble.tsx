/* --------------------------------------------------
 * File: MessageBubble.tsx
 * Purpose: Chat message bubble component displaying user/assistant messages with citations and evidence drawer.
 * Module: Frontend Chat Components
 * Used By: ChatWindow
 * Future Phase: Phase 2D Grounded Chat
 * -------------------------------------------------- */

import React from 'react';
import { User, Bot, Sparkles } from 'lucide-react';
import { CitationCard, CitationItem } from './CitationCard';
import { RetrievedSources, RetrievedChunkItem } from './RetrievedSources';

export interface ChatMessage {
  id: string;
  sender: 'user' | 'assistant';
  content: string;
  citations?: CitationItem[];
  retrieved_chunks?: RetrievedChunkItem[];
  timestamp: string;
}

interface MessageBubbleProps {
  message: ChatMessage;
}

export const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const isUser = message.sender === 'user';

  return (
    <div className={`flex items-start space-x-3 ${isUser ? 'flex-row-reverse space-x-reverse' : ''} animate-fade-in`}>
      <div className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 text-white shadow-xs ${
        isUser ? 'bg-brand-600 dark:bg-brand-500' : 'bg-teal-600 dark:bg-teal-500'
      }`}>
        {isUser ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
      </div>

      <div className={`max-w-[85%] sm:max-w-[75%] space-y-2 ${isUser ? 'items-end' : 'items-start'}`}>
        <div className={`p-4 rounded-2xl text-sm leading-relaxed ${
          isUser
            ? 'bg-brand-600 text-white rounded-tr-none'
            : 'bg-white dark:bg-slate-900 border border-slate-200/80 dark:border-slate-800 text-slate-800 dark:text-slate-100 shadow-xs rounded-tl-none'
        }`}>
          {!isUser && (
            <div className="flex items-center space-x-1 text-xs font-bold text-teal-600 dark:text-teal-400 mb-2">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Grounded Medical Intelligence</span>
            </div>
          )}
          <p className="whitespace-pre-wrap">{message.content}</p>
        </div>

        {/* Citations List */}
        {!isUser && message.citations && message.citations.length > 0 && (
          <div className="space-y-1.5 pt-1">
            <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Citations & References</span>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {message.citations.map((cite, idx) => (
                <CitationCard key={idx} citation={cite} />
              ))}
            </div>
          </div>
        )}

        {/* Evidence Drawer */}
        {!isUser && message.retrieved_chunks && message.retrieved_chunks.length > 0 && (
          <RetrievedSources sources={message.retrieved_chunks} />
        )}

        <span className="text-[10px] text-slate-400 font-medium block px-1">
          {message.timestamp}
        </span>
      </div>
    </div>
  );
};
