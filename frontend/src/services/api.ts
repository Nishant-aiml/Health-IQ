/* --------------------------------------------------
 * File: api.ts
 * Purpose: Frontend API HTTP integration client.
 * Module: Frontend Services
 * Used By: Navbar, HomePage, AboutPage, ErrorDemoPage
 * Future Phase: Phase 1 Foundation
 * -------------------------------------------------- */

export interface HealthData {
  status: string;
  database: string;
  environment: string;
  timestamp: string;
}

export interface VersionData {
  name: string;
  version: string;
  api_version: string;
  architecture_phase: string;
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  message?: string;
  error?: {
    code: string;
    message: string;
    request_id?: string;
  };
}

const API_BASE_URL = '/api/v1';

export async function fetchHealthStatus(): Promise<ApiResponse<HealthData>> {
  const response = await fetch(`${API_BASE_URL}/health`);
  if (!response.ok) {
    throw new Error(`HTTP Error: ${response.status}`);
  }
  return response.json();
}

export async function fetchVersionInfo(): Promise<ApiResponse<VersionData>> {
  const response = await fetch(`${API_BASE_URL}/version`);
  if (!response.ok) {
    throw new Error(`HTTP Error: ${response.status}`);
  }
  return response.json();
}
