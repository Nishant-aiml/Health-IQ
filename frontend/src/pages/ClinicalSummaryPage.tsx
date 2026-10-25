/**
 * File: ClinicalSummaryPage.tsx
 * Purpose: Simple Light Theme Clinical Collaboration Hub.
 *          Doctor Package, Timeline, Notes, Evidence, Share, FHIR Export.
 * Module: Frontend / Pages
 * Routes: /clinical
 */

import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Stethoscope, Activity, MessageSquare, Share2, GitBranch, Database,
  RefreshCw, AlertTriangle, ChevronLeft
} from 'lucide-react';

import { DoctorPackage } from '../components/clinical/DoctorPackage';
import { TimelineViewer } from '../components/clinical/TimelineViewer';
import { NotesPanel } from '../components/clinical/NotesPanel';
import { SharePackage } from '../components/clinical/SharePackage';
import { EvidenceViewer } from '../components/clinical/EvidenceViewer';
import { FHIRPreview } from '../components/clinical/FHIRPreview';

const TABS = [
  { id: 'package', label: 'Case Package', icon: <Stethoscope className="w-4 h-4" /> },
  { id: 'timeline', label: 'Timeline', icon: <Activity className="w-4 h-4" /> },
  { id: 'notes', label: 'Notes', icon: <MessageSquare className="w-4 h-4" /> },
  { id: 'evidence', label: 'Evidence Graph', icon: <GitBranch className="w-4 h-4" /> },
  { id: 'share', label: 'Share Link', icon: <Share2 className="w-4 h-4" /> },
  { id: 'fhir', label: 'FHIR Export', icon: <Database className="w-4 h-4" /> },
];

export default function ClinicalSummaryPage() {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('package');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [packageData, setPackageData] = useState<any>(null);
  const [timelineEvents, setTimelineEvents] = useState<any[]>([]);
  const [notes, setNotes] = useState<any[]>([]);
  const [fhirBundle, setFhirBundle] = useState<any>(null);

  const loadLiveData = async () => {
    setLoading(true);
    setError(null);
    try {
      const storedUser = localStorage.getItem('hl_user');
      const user = storedUser ? JSON.parse(storedUser) : null;
      const userId = user?.id || 1;
      let reportId = 1;

      const hRes = await fetch(`/api/v1/history/${userId}`);
      if (hRes.ok) {
        const hJson = await hRes.json();
        if (hJson?.data?.reports?.length > 0) {
          reportId = hJson.data.reports[0].report_id;
        }
      }

      const [pkgRes, timelineRes, fhirRes, notesRes] = await Promise.allSettled([
        fetch(`/api/v1/clinical/package?user_id=${userId}&report_id=${reportId}&audience=doctor`),
        fetch(`/api/v1/clinical/timeline?user_id=${userId}&report_id=${reportId}`),
        fetch(`/api/v1/clinical/export?user_id=${userId}&report_id=${reportId}`),
        fetch(`/api/v1/notes?user_id=${userId}`),
      ]);

      if (pkgRes.status === 'fulfilled' && pkgRes.value.ok) {
        const json = await pkgRes.value.json();
        if (json?.data) setPackageData(json.data);
      }
      if (timelineRes.status === 'fulfilled' && timelineRes.value.ok) {
        const json = await timelineRes.value.json();
        if (json?.data?.events) setTimelineEvents(json.data.events);
      }
      if (fhirRes.status === 'fulfilled' && fhirRes.value.ok) {
        const json = await fhirRes.value.json();
        if (json?.data) setFhirBundle(json.data);
      }
      if (notesRes.status === 'fulfilled' && notesRes.value.ok) {
        const json = await notesRes.value.json();
        if (json?.data) setNotes(json.data);
      }
    } catch {
      setError('Connect backend for live clinical synchronization.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { loadLiveData(); }, []);

  const handleAddNote = async (noteData: any) => {
    try {
      const storedUser = localStorage.getItem('hl_user');
      const user = storedUser ? JSON.parse(storedUser) : null;
      const userId = user?.id || 1;
      const res = await fetch('/api/v1/notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: userId, ...noteData }),
      });
      if (res.ok) {
        const newNote = await res.json();
        setNotes(prev => [newNote.data || newNote, ...prev]);
      }
    } catch {
      // exception handled
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 py-6">
      {/* Top Header */}
      <div className="max-w-5xl mx-auto px-4 sm:px-6 space-y-4">
        <div className="flex items-center justify-between">
          <button onClick={() => navigate(-1)} className="flex items-center gap-1 text-xs font-bold text-slate-600 hover:text-slate-900">
            <ChevronLeft className="w-4 h-4" /> Back
          </button>
          <button
            onClick={loadLiveData}
            disabled={loading}
            className="flex items-center gap-1.5 text-xs bg-teal-600 hover:bg-teal-700 text-white px-3 py-1.5 rounded-lg font-bold"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
            {loading ? 'Refreshing...' : 'Sync Clinical Data'}
          </button>
        </div>

        <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-1">
          <h1 className="text-xl font-bold text-slate-900 flex items-center gap-2">
            <Stethoscope className="w-5 h-5 text-teal-600" /> Doctor Collaboration Hub
          </h1>
          <p className="text-xs text-slate-600">
            Assembled doctor case packages, clinical timeline, evidence graph, and FHIR export bundle.
          </p>
        </div>

        {/* Navigation Tabs */}
        <div className="flex gap-1 bg-white p-1 rounded-xl border border-slate-200 shadow-sm overflow-x-auto">
          {TABS.map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-xs font-bold whitespace-nowrap transition-all ${
                activeTab === tab.id ? 'bg-teal-600 text-white shadow-sm' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              {tab.icon} {tab.label}
            </button>
          ))}
        </div>

        {/* Tab Content */}
        <div className="space-y-4 pt-2">
          {error && (
            <div className="flex items-center gap-2 bg-amber-50 border border-amber-200 rounded-xl p-3 text-xs text-amber-800">
              <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" /> {error}
            </div>
          )}

          {activeTab === 'package' && <DoctorPackage packageData={packageData} />}
          {activeTab === 'timeline' && <TimelineViewer events={timelineEvents} />}
          {activeTab === 'notes' && <NotesPanel notes={notes} onAddNote={handleAddNote} userId="1" />}
          {activeTab === 'evidence' && <EvidenceViewer evidenceGraph={packageData?.evidence_graph || []} />}
          {activeTab === 'share' && (
            <SharePackage
              packageId={packageData?.package_id}
              sha256Hash={packageData?.sha256_integrity_hash}
            />
          )}
          {activeTab === 'fhir' && <FHIRPreview fhirBundle={fhirBundle} />}
        </div>
      </div>
    </div>
  );
}
