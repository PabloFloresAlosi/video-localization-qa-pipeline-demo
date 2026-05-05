# Subtitling Guidelines

This document defines the subtitle review rules used in the Video Localization QA Pipeline Demo.

## Subtitle Timing

Subtitles should appear close to the related spoken line or audio cue.

Recommended checks:

- Subtitle starts when the spoken line begins or slightly before.
- Subtitle does not appear noticeably late.
- Subtitle remains on screen long enough to be read.
- Subtitle does not stay on screen too long after the line ends.

## Reading Speed

Reading speed is measured in characters per second (CPS).

For this demo, subtitles above 20 CPS are flagged for review.

This does not automatically mean the subtitle is wrong, but it indicates that the text may be difficult to read comfortably.

## Subtitle Length

Subtitles should be concise and easy to read.

Recommended checks:

- Avoid unnecessary added words.
- Keep subtitles close to the spoken line.
- Avoid long subtitles that exceed the visible screen area.
- Split long subtitles where needed.

## Accuracy

Subtitles should accurately represent the spoken dialogue.

Check for:

- Added words that are not spoken.
- Missing important words.
- Incorrect meaning.
- Wrong language.
- Mismatch between audio and subtitle text.

## Formatting

Subtitle formatting should remain consistent across the video.

Check for:

- Consistent punctuation.
- Consistent ellipsis style.
- Final punctuation where appropriate.
- Clean line breaks.
- No unwanted extra spaces.

## Visibility

Subtitles must remain fully visible on screen.

Check for:

- Text overflow.
- Subtitle text cut off by screen edges.
- Poor contrast.
- Subtitle placement blocking important UI elements.

## Demo-Specific Examples

The sample video includes intentional subtitle issues such as:

- A subtitle mismatch: “Working on something very important.” instead of “Working on something important.”
- A punctuation inconsistency: “...” instead of “…”, plus missing final punctuation.
- A long Spanish subtitle that exceeds comfortable reading speed and overflows outside the screen.

These issues are documented in the QA report and checked through both manual review and Python-assisted validation.
