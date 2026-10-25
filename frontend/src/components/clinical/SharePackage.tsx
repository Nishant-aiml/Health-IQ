/**
 * File: SharePackage.tsx
 * Purpose: Share clinical case package with audit-safe role-based access control display.
 *          Shows who can access what (Viewer-only permissions matrix).
 * Module: Frontend / Components / Clinical
 * Used By: ClinicalSummaryPage
 */

import React, { useState } from 'react';
import { Share2, Users, Eye, EyeOff, Lock, Check, Copy } from 'lucide-react';

const CARE_ROLES = [
  { role: 'Primary Doctor', icon: '👨‍⚕️', permissions: ['full_summary', 'medications', 'lab_results', 'notes', 'fhir_export'], color: 'text-teal-300' },
  { role: 'Specialist', icon: '🔬', permissions: ['full_summary', 'lab_results', 'fhir_export'], color: 'text-indigo-300' },
  { role: 'Dietitian', icon: '🥗', permissions: ['nutrition_summary', 'lab_results'], color: 'text-emerald-300' },
  { role: 'Caregiver', icon: '🤝', permissions: ['patient_friendly_summary', 'medications'], color: 'text-amber-300' },
  { role: 'Family', icon: '👨‍👩‍👧', permissions: ['patient_friendly_summary'], color: 'text-purple-300' },
];

const ALL_PERMISSIONS = ['full_summary', 'medications', 'lab_results', 'nutrition_summary', 'notes', 'fhir_export', 'patient_friendly_summary'];

const PERMISSION_LABELS: Record<string, string> = {
  'full_summary': 'Full Clinical Summary',
  'medications': 'Medications',
  'lab_results': 'Lab Results',
  'nutrition_summary': 'Nutrition Summary',
  'notes': 'Clinical Notes',
  'fhir_export': 'FHIR Export',
  'patient_friendly_summary': 'Patient Summary',
};

interface SharePackageProps {
  packageId?: string;
  sha256Hash?: string;
}

export const SharePackage: React.FC<SharePackageProps> = ({ packageId, sha256Hash }) => {
  const [copied, setCopied] = useState(false);
  const [selectedRole, setSelectedRole] = useState<string | null>(null);

  const shareLink = `https://healthlens.ai/package/${packageId}`;

  const handleCopy = () => {
    navigator.clipboard.writeText(shareLink);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-5">
      <h3 className="text-base font-bold text-slate-100 flex items-center gap-2 border-b border-slate-800 pb-4">
        <Share2 className="w-5 h-5 text-purple-400" /> Share with Care Team
      </h3>

      {/* Share Link */}
      <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 flex items-center gap-2">
        <Lock className="w-3.5 h-3.5 text-slate-500 shrink-0" />
        <span className="text-xs text-slate-300 font-mono truncate flex-1">{shareLink}</span>
        <button
          onClick={handleCopy}
          className="text-xs bg-purple-600 hover:bg-purple-500 text-white px-3 py-1 rounded-lg flex items-center gap-1.5 font-bold shrink-0 transition-colors"
        >
          {copied ? <Check className="w-3 h-3" /> : <Copy className="w-3 h-3" />}
          {copied ? 'Copied!' : 'Copy'}
        </button>
      </div>

      {/* Role Selector */}
      <div>
        <p className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-2 flex items-center gap-1">
          <Users className="w-3 h-3" /> Care Team Roles & Permissions
        </p>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
          {CARE_ROLES.map(r => (
            <button
              key={r.role}
              onClick={() => setSelectedRole(selectedRole === r.role ? null : r.role)}
              className={`p-3 rounded-xl border text-left text-xs transition-all ${selectedRole === r.role ? 'border-purple-400/60 bg-purple-900/20' : 'border-slate-800 bg-slate-950/50 hover:border-slate-700'}`}
            >
              <span className="text-lg">{r.icon}</span>
              <p className={`font-bold mt-1 ${r.color}`}>{r.role}</p>
              <p className="text-[10px] text-slate-500">{r.permissions.length} permissions</p>
            </button>
          ))}
        </div>
      </div>

      {/* Permission Matrix */}
      {selectedRole && (() => {
        const role = CARE_ROLES.find(r => r.role === selectedRole);
        return (
          <div className="bg-slate-950/80 rounded-xl border border-slate-800 overflow-hidden">
            <div className="px-4 py-2.5 bg-purple-900/20 border-b border-slate-800">
              <p className="text-xs font-bold text-slate-200">{role?.icon} {selectedRole} — Permission Matrix</p>
            </div>
            <div className="divide-y divide-slate-800/50">
              {ALL_PERMISSIONS.map(perm => (
                <div key={perm} className="flex items-center justify-between px-4 py-2 text-xs">
                  <span className="text-slate-300">{PERMISSION_LABELS[perm]}</span>
                  {role?.permissions.includes(perm) ? (
                    <span className="flex items-center gap-1 text-emerald-400 font-bold"><Eye className="w-3 h-3" /> View</span>
                  ) : (
                    <span className="flex items-center gap-1 text-slate-600"><EyeOff className="w-3 h-3" /> Restricted</span>
                  )}
                </div>
              ))}
            </div>
          </div>
        );
      })()}

      {/* SHA-256 Integrity Notice */}
      {sha256Hash && (
        <div className="text-[10px] text-slate-500 bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 font-mono">
          Package integrity guaranteed · SHA-256: {sha256Hash.slice(0, 24)}...
        </div>
      )}
    </div>
  );
};
