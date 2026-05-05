# Script Test Results

This document records the test results for the Python scripts included in the Video Localization QA Pipeline Demo.

---

## 01_validate_srt_structure.py

### Purpose

Validates the basic structure of the EN and ES subtitle files.

### Command

```bash
python scripts/01_validate_srt_structure.py
```

### Result

```text
SRT Structure Validation
========================

Checking: video_qa_sample_en.srt
OK: SRT structure looks valid.

Checking: video_qa_sample_es.srt
OK: SRT structure looks valid.
```

### Status

Passed.

---

## 02_check_subtitle_reading_speed.py

### Purpose

Checks subtitle reading speed using characters per second.

### Command

```bash
python scripts/02_check_subtitle_reading_speed.py
```

### Result

```text
Subtitle Reading Speed Check
============================

Checking reading speed: video_qa_sample_en.srt
Subtitle 1: 3.00s, 63 chars, 21.00 CPS
  WARNING: Reading speed above threshold (21.00 CPS > 20 CPS)
Subtitle 2: 3.00s, 45 chars, 15.00 CPS
Completed with 1 reading speed issue(s).

Checking reading speed: video_qa_sample_es.srt
Subtitle 1: 3.00s, 44 chars, 14.67 CPS
Subtitle 2: 3.00s, 101 chars, 33.67 CPS
  WARNING: Reading speed above threshold (33.67 CPS > 20 CPS)
Completed with 1 reading speed issue(s).
```

### Status

Passed with warnings.

### Notes

The warnings are expected because the demo intentionally includes subtitles with high reading speed.

---

## 03_generate_qa_summary.py

### Purpose

Generates a summary from the QA report CSV.

### Command

```bash
python scripts/03_generate_qa_summary.py
```

### Result

```text
QA Report Summary
=================

Total issues: 14

Issues by Severity
==================
Severity
Major    8
Minor    6

Issues by Category
==================
Category
Typo / Spelling                                    5
Terminology / Clarity                              2
Wrong Language / Mixed Language + Text Overflow    1
Terminology / UI Label Consistency                 1
Subtitle Mismatch / Accuracy                       1
Subtitle Formatting / Punctuation                  1
Reading Speed / Subtitle Length + Text Overflow    1
Display / Visual Consistency                       1
Naming Consistency / UI Label Consistency          1

Issues by Status
================
Status
Open    14

Summary generated successfully.
```

### Status

Passed.

---

## Summary

All scripts ran successfully.

The SRT structure validation passed.

The reading speed script detected expected subtitle readability warnings.

The QA summary script successfully generated a report overview from the CSV file.
