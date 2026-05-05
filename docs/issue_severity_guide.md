# Issue Severity Guide

This guide defines the severity levels used in the Video Localization QA Pipeline Demo.

---

## Critical

A critical issue prevents the asset from being approved or creates a serious compliance, legal, platform, or user-facing problem.

Examples:

- Missing required legal or rating information
- Completely wrong language in a final localized asset
- Video cannot be reviewed or played correctly
- Severe text overflow blocking essential information

---

## Major

A major issue has a clear impact on quality, comprehension, localization accuracy, or user experience.

Examples:

- Visible spelling mistakes in important UI text
- Subtitle does not match the spoken dialogue
- Subtitle is too long to read comfortably
- Important UI text is truncated or overflowing
- Wrong terminology in a prominent location
- Mixed-language text in a localized UI panel

---

## Minor

A minor issue is visible but does not block understanding or approval on its own.

Examples:

- Small terminology inconsistency
- Slightly unclear UI wording
- Non-critical visual inconsistency
- Minor punctuation or formatting issue

---

## Suggestion

A suggestion is an improvement recommendation rather than a clear defect.

Examples:

- More natural phrasing
- Cleaner UI wording
- Better consistency with style preferences
- Optional readability improvements

---

## Severity Use in This Demo

The sample QA report uses mainly **Major** and **Minor** issues.

Critical issues are not included because this demo is designed as a controlled portfolio sample, not a failed release candidate.

Suggestions may be used when a change would improve clarity but is not strictly required.
