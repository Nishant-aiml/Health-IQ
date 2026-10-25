/* --------------------------------------------------
 * File: LoadingSkeleton.tsx
 * Purpose: High-quality skeleton loading UI component for report dashboard views.
 * Module: Frontend Dashboard Components
 * Used By: ReportDashboardPage
 * Future Phase: Phase 2E Loading UX
 * -------------------------------------------------- */

import React from 'react';

export const LoadingSkeleton: React.FC = () => {
  return (
    <div className="space-y-6 animate-pulse">
      {/* Header Skeleton */}
      <div className="h-10 bg-slate-200 dark:bg-slate-800 rounded-2xl w-1/3" />

      {/* Hero Skeleton */}
      <div className="h-28 bg-slate-200 dark:bg-slate-800 rounded-3xl w-full" />

      {/* Tabs Skeleton */}
      <div className="h-12 bg-slate-200 dark:bg-slate-800 rounded-2xl w-full" />

      {/* Cards Skeleton Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div className="h-40 bg-slate-200 dark:bg-slate-800 rounded-3xl" />
        <div className="h-40 bg-slate-200 dark:bg-slate-800 rounded-3xl" />
      </div>
    </div>
  );
};
