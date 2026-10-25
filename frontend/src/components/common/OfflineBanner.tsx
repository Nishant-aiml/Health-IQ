/* --------------------------------------------------
 * File: OfflineBanner.tsx
 * Purpose: Offline status banner component notifying users when internet connection is lost.
 * Module: Frontend Common Components
 * Used By: App Layout / ReportDashboardPage
 * Future Phase: Phase 2E Graceful Fallback UI
 * -------------------------------------------------- */

import React, { useState, useEffect } from 'react';
import { WifiOff } from 'lucide-react';

export const OfflineBanner: React.FC = () => {
  const [isOffline, setIsOffline] = useState(!navigator.onLine);

  useEffect(() => {
    const handleOnline = () => setIsOffline(false);
    const handleOffline = () => setIsOffline(true);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  if (!isOffline) return null;

  return (
    <div className="p-3 bg-amber-600 text-white text-xs font-semibold flex items-center justify-center space-x-2 animate-fade-in">
      <WifiOff className="w-4 h-4 flex-shrink-0" />
      <span>You are currently offline. Local features and cached reports remain accessible.</span>
    </div>
  );
};
