/* --------------------------------------------------
 * File: ChatWindow.tsx
 * Purpose: Full Grounded Report Chat Window container component.
 * Module: Frontend Chat Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2D Grounded Chat
 * -------------------------------------------------- */

import React, { useState, useRef, useEffect } from 'react';
import { Card } from '../ui/Card';
import { MessageBubble, ChatMessage } from './MessageBubble';
import { SuggestedQuestions } from './SuggestedQuestions';
import { TypingIndicator } from './TypingIndicator';
import { Send, ShieldCheck, Sparkles } from 'lucide-react';

interface ChatWindowProps {
  reportId: number;
}

export const ChatWindow: React.FC<ChatWindowProps> = ({ reportId }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputQuery, setInputQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const chatEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const handleSendMessage = async (queryText?: string) => {
    const textToSend = queryText || inputQuery;
    if (!textToSend.trim() || loading) return;

    const userMsg: ChatMessage = {
      id: `msg_${Date.now()}`,
      sender: 'user',
      content: textToSend,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    setMessages((prev) => [...prev, userMsg]);
    if (!queryText) setInputQuery('');
    setLoading(true);

    try {
      const response = await fetch(`/api/v1/chat/${reportId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question: textToSend,
          conversation_id: conversationId,
        }),
      });

      if (!response.ok) throw new Error(`Chat API error (${response.status})`);
      const resJson = await response.json();

      if (resJson.data) {
        const data = resJson.data;
        if (data.conversation_id) setConversationId(data.conversation_id);

        const aiMsg: ChatMessage = {
          id: `msg_${Date.now() + 1}`,
          sender: 'assistant',
          content: data.answer,
          citations: data.citations,
          retrieved_chunks: data.retrieved_chunks,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        };

        setMessages((prev) => [...prev, aiMsg]);
      }
    } catch (err: any) {
      const errorMsg: ChatMessage = {
        id: `msg_err_${Date.now()}`,
        sender: 'assistant',
        content: "I'm sorry, I encountered an error while consulting medical guidelines. Please try asking again.",
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };
      setMessages((prev) => [...prev, errorMsg]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="flex flex-col h-[650px] p-0 overflow-hidden bg-slate-50/50 dark:bg-slate-900/50">
      {/* Header Banner */}
      <div className="p-4 bg-white dark:bg-slate-900 border-b border-slate-200/80 dark:border-slate-800 flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <Sparkles className="w-5 h-5 text-brand-600 dark:text-brand-400" />
          <div>
            <h3 className="text-sm font-bold text-slate-900 dark:text-slate-100">
              Grounded AI Report Assistant
            </h3>
            <p className="text-[11px] text-slate-400">
              Hybrid Medical Retrieval • WHO, CDC, NIH, ICMR Evidence Grounded
            </p>
          </div>
        </div>
        <div className="flex items-center space-x-1 text-xs font-semibold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/40 px-2.5 py-1 rounded-full border border-emerald-200/60 dark:border-emerald-900/40">
          <ShieldCheck className="w-3.5 h-3.5" />
          <span>Anti-Hallucination Safe</span>
        </div>
      </div>

      {/* Messages Scroll View */}
      <div className="flex-1 p-4 overflow-y-auto space-y-4">
        {messages.length === 0 && (
          <div className="py-8 space-y-6 animate-fade-in text-center max-w-lg mx-auto">
            <div className="p-4 bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/80 dark:border-slate-800 space-y-2 shadow-xs">
              <h4 className="text-sm font-bold text-slate-900 dark:text-slate-100">
                Ask Questions About Your Lab Results
              </h4>
              <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
                Every response is strictly grounded in your personal lab report analysis and official international medical guidelines.
              </p>
            </div>
            <SuggestedQuestions onSelectQuestion={(q) => handleSendMessage(q)} />
          </div>
        )}

        {messages.map((msg) => (
          <MessageBubble key={msg.id} message={msg} />
        ))}

        {loading && <TypingIndicator />}
        <div ref={chatEndRef} />
      </div>

      {/* Footer Input Bar */}
      <div className="p-3 bg-white dark:bg-slate-900 border-t border-slate-200/80 dark:border-slate-800 space-y-2">
        {messages.length > 0 && (
          <SuggestedQuestions onSelectQuestion={(q) => handleSendMessage(q)} />
        )}

        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSendMessage();
          }}
          className="flex items-center space-x-2"
        >
          <input
            type="text"
            value={inputQuery}
            onChange={(e) => setInputQuery(e.target.value)}
            placeholder="Ask a question about your lab results (e.g. Why is my Hb low?)..."
            disabled={loading}
            className="flex-1 px-4 py-3 bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl text-xs sm:text-sm text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-brand-500 min-h-[44px]"
          />
          <button
            type="submit"
            disabled={!inputQuery.trim() || loading}
            className="p-3 bg-brand-600 hover:bg-brand-700 disabled:opacity-50 text-white rounded-2xl transition-colors min-h-[44px] min-w-[44px] flex items-center justify-center shadow-xs"
          >
            <Send className="w-4 h-4" />
          </button>
        </form>
      </div>
    </Card>
  );
};
