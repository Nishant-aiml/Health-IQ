# --------------------------------------------------
# File: states.py
# Purpose: Defines state machine stages and status transitions for document ingestion jobs.
# Module: Ingestion Engine / Queue
# Used By: Worker Queue, Job Repository
# Future Phase: Phase 2A Ingestion Pipeline
# --------------------------------------------------

class JobStage:
    QUEUED = "queued"
    EXTRACTING = "extracting"
    PARSING = "parsing"
    ANALYZED = "analyzed"
    COMPLETED = "completed"
    FAILED = "failed"


class JobStatus:
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
