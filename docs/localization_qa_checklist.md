# Localization QA Checklist

This checklist is used to review the localized video sample in the Video Localization QA Pipeline Demo.

---

## Video Asset Review

- Confirm that the video plays correctly from start to finish.
- Check that the correct language version is being reviewed.
- Verify that all visible UI text is readable.
- Confirm that important text does not overflow outside the screen or UI panels.
- Check that visual style remains consistent across related UI elements.

---

## Subtitle Review

- Confirm that subtitles match the spoken dialogue.
- Check subtitle timing against the audio.
- Check subtitle reading speed.
- Confirm that punctuation and formatting are consistent.
- Verify that subtitles remain fully visible on screen.
- Check that line breaks do not reduce readability.

---

## Linguistic Review

- Check for spelling mistakes.
- Check for grammar issues.
- Verify that terminology follows the glossary.
- Confirm that translated text sounds natural in context.
- Check for mixed-language issues in localized sections.

---

## UI and Static Material Review

- Check title cards, menu panels, labels, buttons, and instruction screens.
- Confirm that labels use consistent naming conventions.
- Verify that buttons and related UI elements use consistent visual styles.
- Check that important information remains on screen long enough to be read.

---

## Compliance-Style Review

This demo does not perform official legal, rating, or platform compliance certification.

However, it includes compliance-style checks such as:

- Text legibility
- Display duration
- Safe visible area
- Clear warning/review text
- No critical information cut off or hidden

---

## Reporting Checklist

For every issue found, log:

- Issue ID
- Asset type
- Asset name
- Language
- Timecode in
- Timecode out
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

## Final Review

Before closing the QA pass, confirm that:

- All issues have clear timecodes.
- Each issue has a category and severity.
- Expected results are specific and actionable.
- The QA report is consistent with the severity guide.
- The Python script results are documented.
- Screenshots support the most visible issues.
