# --------------------------------------------------
# File: templates.py
# Purpose: Templates for executive clinical summaries and safety-focused trend notes.
# Module: Longitudinal Summary Generator / Templates
# Used By: Summary Generator
# Future Phase: Phase 3B Longitudinal Health Intelligence
# --------------------------------------------------

LONGITUDINAL_DISCLAIMER = (
    "This longitudinal summary is educational and does not provide a clinical diagnosis or disease prediction. "
    "All parameter trends and historical shifts should be reviewed with your prescribing healthcare provider."
)

LONGITUDINAL_SUMMARY_TEMPLATE = """
Longitudinal Health Journey Summary ({report_count} Reports Tracked):

Overall Health Score Trajectory:
- Initial Baseline: {initial_score} / 100
- Latest Report: {latest_score} / 100 (Delta: {score_delta})

Key Biomarker Trajectories:
{trends_summary}

Clinical Change Highlights:
- Improved Parameters: {improved_count}
- Stable Parameters: {stable_count}
- Parameters Needing Attention: {attention_count}
"""
