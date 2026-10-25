/* --------------------------------------------------
 * File: App.tsx
 * Purpose: Top-level React Router App component.
 * Module: Frontend Core
 * Used By: main.tsx
 * -------------------------------------------------- */

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { RootLayout } from './components/layout/RootLayout';
import { HomePage } from './pages/HomePage';
import { UploadPage } from './pages/UploadPage';
import { ReportDashboardPage } from './pages/ReportDashboardPage';
import { PrescriptionPage } from './pages/PrescriptionPage';
import { HistoryPage } from './pages/HistoryPage';
import { NutritionPage } from './pages/NutritionPage';
import { ChatAssistantPage } from './pages/ChatAssistantPage';
import { LandingPage } from './pages/LandingPage';
import { AboutPage } from './pages/AboutPage';
import { ErrorDemoPage } from './pages/ErrorDemoPage';
import { NotFoundPage } from './pages/NotFoundPage';
import ClinicalSummaryPage from './pages/ClinicalSummaryPage';

export const App: React.FC = () => {
  return (
    <Router>
      <RootLayout>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/upload" element={<UploadPage />} />
          <Route path="/chat" element={<ChatAssistantPage />} />
          <Route path="/voice" element={<Navigate to="/chat" replace />} />
          <Route path="/nutrition" element={<NutritionPage />} />
          <Route path="/history" element={<HistoryPage />} />
          <Route path="/prescriptions" element={<PrescriptionPage />} />
          <Route path="/reports/:reportId" element={<ReportDashboardPage />} />
          <Route path="/clinical" element={<ClinicalSummaryPage />} />
          <Route path="/landing" element={<LandingPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/error-demo" element={<ErrorDemoPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </RootLayout>
    </Router>
  );
};

export default App;
