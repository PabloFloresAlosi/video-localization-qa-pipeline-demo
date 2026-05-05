"""
02_check_subtitle_reading_speed.py

Checks subtitle reading speed for the Video Localization QA Pipeline Demo.

Calculates:
- Duration
- Character count
- Characters per second (CPS)

Flags subtitles above the selected CPS threshold.
"""

from pathlib import Path
import srt


BASE_DIR = Path(__file__).resolve().parent.parent
SUBTITLES_DIR = BASE_DIR / "assets" / "subtitles"

SRT_FILES = [
    SUBTITLES_DIR / "video_qa_sample_en.srt",
    SUBTITLES_DIR / "video_qa_sample_es.srt",
]

CPS_THRESHOLD = 20


def calculate_cps(text, duration_seconds):
    clean_text = text.replace("\n", " ").strip()
    character_count = len(clean_text)

    if duration_seconds <= 0:
        return character_count, 0

    cps = character_count / duration_seconds
    return character_count, cps


def check_file(file_path):
    print(f"\nChecking reading speed: {file_path.name}")

    if not file_path.exists():
        print(f"ERROR: File not found: {file_path}")
        return

    content = file_path.read_text(encoding="utf-8")
    subtitles = list(srt.parse(content))

    issues_found = 0

    for subtitle in subtitles:
        duration = subtitle.end - subtitle.start
        duration_seconds = duration.total_seconds()

        character_count, cps = calculate_cps(
            subtitle.content,
            duration_seconds
        )

        print(
            f"Subtitle {subtitle.index}: "
            f"{duration_seconds:.2f}s, "
            f"{character_count} chars, "
            f"{cps:.2f} CPS"
        )

        if cps > CPS_THRESHOLD:
            print(
                f"  WARNING: Reading speed above threshold "
                f"({cps:.2f} CPS > {CPS_THRESHOLD} CPS)"
            )
            issues_found += 1

    if issues_found == 0:
        print("OK: No reading speed issues found.")
    else:
        print(f"Completed with {issues_found} reading speed issue(s).")


def main():
    print("Subtitle Reading Speed Check")
    print("============================")

    for srt_file in SRT_FILES:
        check_file(srt_file)


if __name__ == "__main__":
    main()