/**
 * File: NotesPanel.tsx
 * Purpose: Real-time clinical note creation and listing panel.
 *          Supports Note Types: Clinical Observation, Visit Summary, Patient Question, Doctor Comment.
 * Module: Frontend / Components / Clinical
 * Used By: ClinicalSummaryPage
 */

import React, { useState } from 'react';
import { MessageSquare, Plus, User, Clock } from 'lucide-react';

interface ClinicalNote {
  id?: number;
  note_id?: string;
  user_id: string | number;
  report_id?: number;
  note_type: string;
  title?: string;
  content: string;
  author_name: string;
  author_role: string;
  created_at: string;
}

interface NotesPanelProps {
  notes: ClinicalNote[];
  onAddNote: (note: Partial<ClinicalNote>) => void;
  userId: string;
}

const NOTE_TYPES = ['Clinical Observation', 'Visit Summary', 'Patient Question', 'Doctor Comment'];

const NOTE_COLORS: Record<string, string> = {
  'Clinical Observation': 'bg-teal-900/10 border-teal-400/30 text-teal-300',
  'Visit Summary': 'bg-indigo-900/10 border-indigo-400/30 text-indigo-300',
  'Patient Question': 'bg-amber-900/10 border-amber-400/30 text-amber-300',
  'Doctor Comment': 'bg-emerald-900/10 border-emerald-400/30 text-emerald-300',
};

export const NotesPanel: React.FC<NotesPanelProps> = ({ notes, onAddNote, userId }) => {
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    note_type: 'Clinical Observation',
    title: '',
    content: '',
    author_name: 'Patient',
    author_role: 'Patient',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.title.trim() || !formData.content.trim()) return;
    onAddNote({ ...formData, user_id: userId });
    setFormData({ note_type: 'Clinical Observation', title: '', content: '', author_name: 'Patient', author_role: 'Patient' });
    setShowForm(false);
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-5">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <h3 className="text-base font-bold text-slate-100 flex items-center gap-2">
          <MessageSquare className="w-5 h-5 text-amber-400" /> Clinical Notes ({notes.length})
        </h3>
        <button
          onClick={() => setShowForm(!showForm)}
          className="flex items-center gap-1.5 text-xs bg-amber-600 hover:bg-amber-500 text-white px-3 py-1.5 rounded-lg font-bold transition-colors"
        >
          <Plus className="w-3.5 h-3.5" /> Add Note
        </button>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="bg-slate-950/80 p-4 rounded-xl border border-slate-700 space-y-3">
          <div className="grid sm:grid-cols-2 gap-3">
            <div>
              <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">Note Type</label>
              <select
                value={formData.note_type}
                onChange={e => setFormData(f => ({ ...f, note_type: e.target.value }))}
                className="w-full bg-slate-900 text-slate-200 text-xs border border-slate-700 rounded-lg px-3 py-2 focus:outline-none focus:border-amber-400"
              >
                {NOTE_TYPES.map(t => <option key={t}>{t}</option>)}
              </select>
            </div>
            <div>
              <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">Author Name</label>
              <input
                value={formData.author_name}
                onChange={e => setFormData(f => ({ ...f, author_name: e.target.value }))}
                placeholder="e.g. Dr. Singh"
                className="w-full bg-slate-900 text-slate-200 text-xs border border-slate-700 rounded-lg px-3 py-2 focus:outline-none focus:border-amber-400"
              />
            </div>
          </div>
          <div>
            <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">Title</label>
            <input
              value={formData.title}
              onChange={e => setFormData(f => ({ ...f, title: e.target.value }))}
              placeholder="e.g. Cholesterol review visit"
              className="w-full bg-slate-900 text-slate-200 text-xs border border-slate-700 rounded-lg px-3 py-2 focus:outline-none focus:border-amber-400"
            />
          </div>
          <div>
            <label className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">Content</label>
            <textarea
              value={formData.content}
              onChange={e => setFormData(f => ({ ...f, content: e.target.value }))}
              rows={4}
              placeholder="Write clinical note..."
              className="w-full bg-slate-900 text-slate-200 text-xs border border-slate-700 rounded-lg px-3 py-2 focus:outline-none focus:border-amber-400 resize-none"
            />
          </div>
          <div className="flex gap-2 justify-end">
            <button type="button" onClick={() => setShowForm(false)} className="text-xs text-slate-400 hover:text-slate-200 px-3 py-1.5 rounded-lg border border-slate-700 font-bold">Cancel</button>
            <button type="submit" className="text-xs bg-amber-600 hover:bg-amber-500 text-white px-4 py-1.5 rounded-lg font-bold transition-colors">Save Note</button>
          </div>
        </form>
      )}

      <div className="space-y-3">
        {notes.length === 0 ? (
          <p className="text-center py-8 text-slate-500 text-sm">No notes yet. Add the first one.</p>
        ) : (
          notes.map((note, idx) => (
            <div key={note.note_id || note.id || idx} className={`p-4 rounded-xl border text-xs space-y-2 ${NOTE_COLORS[note.note_type] || 'bg-slate-950/50 border-slate-700'}`}>
              <div className="flex items-center justify-between flex-wrap gap-2">
                <span className="font-bold text-slate-100">{note.title || note.note_type}</span>
                <span className={`text-[10px] px-2 py-0.5 rounded-full font-bold border ${NOTE_COLORS[note.note_type]}`}>{note.note_type}</span>
              </div>
              <p className="text-slate-300 leading-relaxed">{note.content}</p>
              <div className="flex items-center gap-3 text-[10px] text-slate-500 flex-wrap">
                <span className="flex items-center gap-1"><User className="w-2.5 h-2.5" /> {note.author_name} · {note.author_role}</span>
                <span className="flex items-center gap-1"><Clock className="w-2.5 h-2.5" /> {new Date(note.created_at).toLocaleDateString()}</span>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
