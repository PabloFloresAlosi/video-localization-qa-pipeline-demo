# Script Test Results

## 01\_validate\_srt\_structure.py

Result:

```text
SRT Structure Validation
========================

Checking: video\\\\\\\\\\\\\\\_qa\\\\\\\\\\\\\\\_sample\\\\\\\\\\\\\\\_en.srt
OK: SRT structure looks valid.

Checking: video\\\\\\\\\\\\\\\_qa\\\\\\\\\\\\\\\_sample\\\\\\\\\\\\\\\_es.srt
OK: SRT structure looks valid.
```

## 02\_check\_subtitle\_reading\_speed.py

Result:

```text
Subtitle Reading Speed Check
============================

Checking reading speed: video\\\\\\\\\\\\\\\_qa\\\\\\\\\\\\\\\_sample\\\\\\\\\\\\\\\_en.srt
Subtitle 1: 3.00s, 63 chars, 21.00 CPS
WARNING: Reading speed above threshold (21.00 CPS > 20 CPS)
Subtitle 2: 3.00s, 45 chars, 15.00 CPS
Completed with 1 reading speed issue(s).

Checking reading speed: video\\\\\\\\\\\\\\\_qa\\\\\\\\\\\\\\\_sample\\\\\\\\\\\\\\\_es.srt
Subtitle 1: 3.00s, 44 chars, 14.67 CPS
Subtitle 2: 3.00s, 101 chars, 33.67 CPS
WARNING: Reading speed above threshold (33.67 CPS > 20 CPS)
Completed with 1 reading speed issue(s).
```

## 03\_generate\_qa\_summary.py

Result:

```text
QA Report Summary
=================

Total issues: 14

Issues by Severity
==================
Major    8
Minor    6

Issues by Status
================
Open    14
```

## Notes

The SRT validation script confirms that both subtitle files are structurally valid.

The reading speed script flags two subtitle entries above the selected 20 CPS threshold, including the intentionally long Spanish subtitle.

The QA summary script confirms that the sample issue report contains 14 open issues across multiple QA categories.

