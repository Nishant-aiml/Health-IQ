/**
 * File: LandingPage.tsx
 * Purpose: Simple Light Theme Patient Marketing Homepage.
 * Module: Frontend / Pages
 * Route: /landing
 */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Upload, Sparkles, Activity, Heart,
  Brain, FileText, ChevronDown, Stethoscope, Bot
} from 'lucide-react';

const FEATURES = [
  { icon: <Brain className="w-5 h-5 text-teal-600" />, title: 'AI Medical Report Analysis', desc: 'Translates complex blood panels into clear, plain-language insights.' },
  { icon: <FileText className="w-5 h-5 text-indigo-600" />, title: 'Prescription Intelligence', desc: 'Extracts dosages, timing, active ingredients, and food interaction warnings.' },
  { icon: <Activity className="w-5 h-5 text-emerald-600" />, title: 'Longitudinal Health Journey', desc: 'Tracks biomarker changes across multiple report uploads over time.' },
  { icon: <Heart className="w-5 h-5 text-rose-600" />, title: 'Precision Nutrition', desc: 'Targeted food suggestions tied directly to your blood work markers.' },
  { icon: <Bot className="w-5 h-5 text-amber-600" />, title: 'Multilingual AI Chat Assistant', desc: 'Chat naturally in English, Hindi, Marathi, Tamil, Telugu, and 5+ Indian languages powered by Sarvam AI.' },
  { icon: <Stethoscope className="w-5 h-5 text-cyan-600" />, title: 'Doctor Collaboration Hub', desc: 'Assembles immutable clinical case packages for your physician.' }
];

const FAQS = [
  { q: 'What types of medical reports can I upload?', a: 'PDFs, scanned images (PNG, JPG), or document files (DOCX, TXT) containing blood panels, lipid profiles, or prescriptions.' },
  { q: 'Is my health data secure and private?', a: 'Yes. Data is processed using end-to-end security protocols with optional user authentication.' },
  { q: 'What languages are supported by the AI Chat Assistant?', a: 'English, Hindi, Marathi, Tamil, Telugu, Kannada, Gujarati, Punjabi, Bengali, and Malayalam.' }
];

export const LandingPage: React.FC = () => {
  const navigate = useNavigate();
  const [openFaq, setOpenFaq] = useState<number | null>(null);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      {/* Hero */}
      <section className="py-16 sm:py-24 max-w-5xl mx-auto px-4 text-center space-y-6">
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-teal-50 border border-teal-200 text-teal-700 text-xs font-bold">
          <Sparkles className="w-4 h-4 text-teal-600" /> AI-Powered Health Intelligence Platform
        </div>

        <h1 className="text-4xl sm:text-5xl font-black text-slate-900 tracking-tight max-w-3xl mx-auto leading-tight">
          See Beyond Your <span className="text-teal-600">Medical Reports</span>
        </h1>

        <p className="text-base sm:text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
          Upload any medical report. Receive instant AI-powered clinical explanations, precision nutrition guidance, longitudinal health tracking, and doctor-ready summaries.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
          <button
            onClick={() => navigate('/upload')}
            className="w-full sm:w-auto px-8 py-3.5 rounded-2xl font-bold bg-teal-600 hover:bg-teal-700 text-white text-sm flex items-center justify-center gap-2 shadow-md"
          >
            <Upload className="w-4 h-4" /> Upload Medical Report
          </button>
          <button
            onClick={() => navigate('/chat')}
            className="w-full sm:w-auto px-8 py-3.5 rounded-2xl font-bold bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 text-sm flex items-center justify-center gap-2"
          >
            <Bot className="w-4 h-4 text-teal-600" /> Try AI Chat Assistant
          </button>
        </div>
      </section>

      {/* Features */}
      <section className="py-12 bg-white border-y border-slate-200">
        <div className="max-w-5xl mx-auto px-4 space-y-8">
          <div className="text-center space-y-1">
            <h2 className="text-2xl font-bold text-slate-900">Complete Healthcare Intelligence Scope</h2>
            <p className="text-xs text-slate-500">Every feature designed for clinical clarity and patient empowerment.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {FEATURES.map((f, i) => (
              <div key={i} className="bg-slate-50 border border-slate-200 rounded-2xl p-5 space-y-2 hover:border-teal-500 transition-colors shadow-sm">
                <div className="w-10 h-10 rounded-xl bg-white border border-slate-200 flex items-center justify-center">
                  {f.icon}
                </div>
                <h3 className="text-sm font-bold text-slate-900">{f.title}</h3>
                <p className="text-xs text-slate-600 leading-relaxed">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQs */}
      <section className="py-16 max-w-3xl mx-auto px-4 space-y-6">
        <h2 className="text-2xl font-bold text-slate-900 text-center">Frequently Asked Questions</h2>
        <div className="space-y-3">
          {FAQS.map((faq, idx) => (
            <div key={idx} className="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm">
              <button
                onClick={() => setOpenFaq(openFaq === idx ? null : idx)}
                className="w-full p-4 text-left font-bold text-xs text-slate-900 flex items-center justify-between"
              >
                <span>{faq.q}</span>
                <ChevronDown className={`w-4 h-4 text-slate-400 transition-transform ${openFaq === idx ? 'rotate-180' : ''}`} />
              </button>
              {openFaq === idx && (
                <div className="p-4 border-t border-slate-100 bg-slate-50 text-xs text-slate-600 leading-relaxed">
                  {faq.a}
                </div>
              )}
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};
