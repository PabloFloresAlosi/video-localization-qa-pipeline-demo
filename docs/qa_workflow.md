# QA Workflow

This document describes the workflow used in the Video Localization QA Pipeline Demo.

---

## 1. Prepare the Video Asset

A short Unreal Engine in-game capture is edited into a localized video QA sample.

The video includes intentional QA issues related to UI text, subtitles, terminology, display bugs, and visual consistency.

The final video is hosted externally to keep the GitHub repository lightweight.

---

## 2. Review the Video

The video is reviewed from start to finish, focusing on:

- In-game UI text
- Static screens
- Subtitle timing
- Subtitle readability
- Language consistency
- Visual consistency
- Terminology and glossary use

---

## 3. Log Issues

Each issue is logged in the QA report with:

- Issue ID
- Asset type
- Asset name
- Language
- Timecode
- Category
- Severity
- Original text
- Localized text
- Issue description
- Expected result
- Actual result
- Status
- Notes

---

## 4. Validate Subtitle Files

Subtitle files are stored separately in the repository as SRT samples.

The structure validation script checks whether the SRT files can be parsed correctly and whether subtitle entries have valid timing and content.

Script:

```text
scripts/01_validate_srt_structure.py
```

---

## 5. Check Reading Speed

The reading speed script calculates:

- Subtitle duration
- Character count
- Characters per second

The demo uses a 20 CPS threshold to flag subtitles that may be too fast to read comfortably.

Script:

```text
scripts/02_check_subtitle_reading_speed.py
```

---

## 6. Generate QA Summary

The QA summary script reads the issue report and prints:

- Total number of issues
- Issues by severity
- Issues by category
- Issues by status

Script:

```text
scripts/03_generate_qa_summary.py
```

---

## 7. Document Results

Script outputs are documented in:

```text
docs/script_test_results.md
```

This makes the QA process easier to review and shows how manual QA reporting can be supported by lightweight automation.
