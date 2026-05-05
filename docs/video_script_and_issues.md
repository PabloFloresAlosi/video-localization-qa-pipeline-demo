# Video Script and Intentional QA Issues

## Project

Video Localization QA Pipeline Demo

## Purpose

This document maps the final video timeline, subtitles, on-screen text, and intentional QA issues used for the demo.

The goal is to document the intentional localization QA issues included in the video and connect each issue to a clear timecode, expected result, and QA category.

---

## Video Source

Source material:

- Existing Unreal + Wwise Localization Audio Pipeline Demo capture
- EN/ES dialogue and UI/audio interaction demo
- Additional subtitle overlays and intentional QA issues added during editing

---

## Timeline Review

### 00:07–00:08 — Intro / Title Card

**What appears on screen**

- "Localized VO changes globally through Wwise audio culture"
- "Unrel"

**Intended QA issue**

- Terminology / clarity issue
- Typo / spelling issue

**Expected result**

- Use clearer terminology such as "Wwise language settings".
- Correct "Unrel" to "Unreal".

**Notes**

The phrase "Wwise audio culture" is unclear in a localization QA context. The typo "Unrel" is visible in a prominent title area.

---

### 00:10–00:12 — Language Switching Area

**What appears on screen**

- "Language Swiching"

**Intended QA issue**

- Typo / spelling issue

**Expected result**

- "Language Switching"

**Notes**

Visible typo in a main section heading.

---

### 00:13–00:16 — Start Here Panel

**What appears on screen**

- "Start Here"
- "Tutorial & Overview"
- "Explora cada estación"
- "Listen to localized audio"
- "Cambiar idioma"
- "Test UI & ambience sounds"

**Intended QA issue**

- Wrong language / mixed language issue
- Text overflow / display issue

**Expected result**

All text should be consistently localized for the selected language and remain fully visible within the UI panel.

**Notes**

The panel mixes English and Spanish text. The final line also overflows outside the visible panel area.

---

### 00:20–00:22 — Dialogue Category Label

**What appears on screen**

- "Complain"

**Intended QA issue**

- Terminology / UI label consistency issue

**Expected result**

- "Complaint"

**Notes**

Other category labels use nouns such as "Greeting", "Work", "Reaction", and "Idle". "Complain" is a verb and breaks naming consistency.

---

### 00:20–00:23 — Dialogue Subtitle

**Audio / dialogue**

- Spoken line: "Working on something important."
- Subtitle: "Working on something very important."

**Intended QA issue**

- Subtitle mismatch / accuracy issue

**Expected result**

The subtitle should match the spoken dialogue:

- "Working on something important."

**Notes**

The subtitle adds the word "very", which is not present in the spoken line.

---

### 00:25–00:28 — Subtitle Punctuation

**Subtitle text**

- "You seem distracted.. / Just thinking out loud"

**Intended QA issue**

- Subtitle formatting / punctuation issue

**Expected result**

- "You seem distracted... / Just thinking out loud."

**Notes**

The ellipsis style is inconsistent and final punctuation is missing.

---

### 00:37–00:40 — Long Spanish Subtitle

**Audio / dialogue**

- Spoken line: "Creo que se ha roto otra vez."
- Subtitle: "Creo que se ha roto otra vez, no sé qué pasa con este sistema ahora mismo."

**Intended QA issue**

- Reading speed / subtitle length issue
- Subtitle mismatch / accuracy issue
- Text overflow / display issue

**Expected result**

The subtitle should match the spoken line:

- "Creo que se ha roto otra vez."

**Notes**

The subtitle is significantly longer than the spoken line, exceeds comfortable reading speed, and overflows outside the visible screen area.

---

### 00:44–00:47 — Language Switch Feedback Area

**What appears on screen**

- "LANGUAGE SWICH FEEDBACK"
- "Select the feedback sound used when switching languaje"

**Intended QA issue**

- Typo / spelling issue
- Terminology / clarity issue

**Expected result**

- "LANGUAGE SWITCH FEEDBACK"
- "Select the confirmation sound used when switching language."

**Notes**

"Swich" and "languaje" are spelling mistakes. "Feedback sound" is less clear in this context than "confirmation sound".

---

### 00:48–00:50 — Basic Ambience Area

**What appears on screen**

- "Switch bitween simple background ambience beds"

**Intended QA issue**

- Typo / spelling issue

**Expected result**

- "Switch between simple background ambience beds."

**Notes**

Visible typo in the Basic Ambience description.

---

### 00:58–01:01 — Ambience Button Visual Style

**What appears on screen**

- "Street AMB" button appears yellow while the other ambience buttons use a different style.

**Intended QA issue**

- Display / visual consistency issue

**Expected result**

All ambience buttons should keep the same visual style unless the color indicates a clear documented state.

**Notes**

The yellow button creates visual inconsistency across related UI controls.

---

### 01:02–01:09 — Ambience Button Naming

**What appears on screen**

- "Stop ambience"

**Intended QA issue**

- Naming consistency / UI label consistency issue

**Expected result**

Use one of the following:

- "Stop AMB"
- Or a standardized naming convention across all ambience buttons.

**Notes**

The other buttons use the "AMB" abbreviation: "Forest AMB", "Room AMB", and "Street AMB". "Stop ambience" breaks the naming pattern.

---

## Final Issue Summary

The video includes intentional localization QA issues across:

- UI spelling
- Terminology clarity
- Mixed language text
- Subtitle mismatch
- Reading speed
- Text overflow
- Visual consistency
- Naming consistency

These issues are documented in the QA report located at:

```text
csv/qa_report_sample.csv
```
