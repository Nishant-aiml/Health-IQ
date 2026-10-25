/**
 * File: ScheduleTimeline.tsx
 * Purpose: Data-driven visual timeline showing active daily dosage time slots (Morning, Afternoon, Evening, Night).
 * Module: Frontend / Components / Prescription
 * Used By: MedicineCard Component
 * Future Phase: Phase 3A Medicine Intelligence
 */

import React from 'react';
import { Sun, Sunset, Moon, Clock } from 'lucide-react';

export interface TimeSlot {
  slot_id: string;
  slot_name: string;
  target_time: string;
  is_active: boolean;
  instruction?: string;
}

export interface NormalizedSchedule {
  frequency_code: string;
  times_per_day: number;
  timing_slots: TimeSlot[];
  relation_to_food: string;
  food_instruction_en: string;
  human_description: string;
  duration: string;
}

interface ScheduleTimelineProps {
  schedule: NormalizedSchedule;
}

export const ScheduleTimeline: React.FC<ScheduleTimelineProps> = ({ schedule }) => {
  const getSlotIcon = (slotId: string) => {
    switch (slotId) {
      case 'morning':
        return <Sun className="w-4 h-4 text-amber-500" />;
      case 'afternoon':
        return <Sun className="w-4 h-4 text-orange-500" />;
      case 'evening':
        return <Sunset className="w-4 h-4 text-indigo-500" />;
      case 'night':
        return <Moon className="w-4 h-4 text-purple-400" />;
      default:
        return <Clock className="w-4 h-4 text-slate-400" />;
    }
  };

  return (
    <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 my-3">
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2">
          <span className="bg-teal-500/20 text-teal-300 font-semibold px-2.5 py-0.5 rounded-md text-xs border border-teal-500/30">
            {schedule.frequency_code}
          </span>
          <span className="text-slate-300 text-sm font-medium">{schedule.human_description}</span>
        </div>
        <span className="text-xs text-slate-400 bg-slate-800 px-2 py-1 rounded">
          Duration: {schedule.duration}
        </span>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-2.5">
        {schedule.timing_slots.map((slot) => (
          <div
            key={slot.slot_id}
            className={`p-3 rounded-lg border flex flex-col justify-between transition-all ${
              slot.is_active
                ? 'bg-teal-950/40 border-teal-500/40 shadow-sm shadow-teal-900/20'
                : 'bg-slate-950/40 border-slate-800/60 opacity-50'
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs text-slate-400 font-medium">{slot.slot_name}</span>
              {getSlotIcon(slot.slot_id)}
            </div>
            <div className="mt-2">
              <span className={`text-sm font-bold ${slot.is_active ? 'text-teal-300' : 'text-slate-500'}`}>
                {slot.is_active ? '1 Dose' : 'Skip'}
              </span>
              <p className="text-[11px] text-slate-400 mt-0.5">{slot.target_time}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
