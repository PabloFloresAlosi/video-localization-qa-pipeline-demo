"""
01_validate_srt_structure.py

Validates basic SRT structure for the Video Localization QA Pipeline Demo.

Checks:
- File can be parsed as SRT
- Subtitle blocks are not empty
- Start time is before end time
- Subtitle indexes are sequential
"""

from pathlib import Path
import srt


BASE_DIR = Path(__file__).resolve().parent.parent
SUBTITLES_DIR = BASE_DIR / "assets" / "subtitles"

SRT_FILES = [
    SUBTITLES_DIR / "video_qa_sample_en.srt",
    SUBTITLES_DIR / "video_qa_sample_es.srt",
]


def validate_srt_file(file_path):
    print(f"\nChecking: {file_path.name}")

    if not file_path.exists():
        print(f"ERROR: File not found: {file_path}")
        return

    content = file_path.read_text(encoding="utf-8")
    subtitles = list(srt.parse(content))

    if not subtitles:
        print("ERROR: No subtitles found.")
        return

    issues_found = 0

    for expected_index, subtitle in enumerate(subtitles, start=1):
        if subtitle.index != expected_index:
            print(
                f"WARNING: Expected index {expected_index}, "
                f"found {subtitle.index}"
            )
            issues_found += 1

        if subtitle.start >= subtitle.end:
            print(
                f"ERROR: Subtitle {subtitle.index} has invalid timing: "
                f"{subtitle.start} --> {subtitle.end}"
            )
            issues_found += 1

        if not subtitle.content.strip():
            print(f"ERROR: Subtitle {subtitle.index} is empty.")
            issues_found += 1

    if issues_found == 0:
        print("OK: SRT structure looks valid.")
    else:
        print(f"Completed with {issues_found} structure issue(s).")


def main():
    print("SRT Structure Validation")
    print("========================")

    for srt_file in SRT_FILES:
        validate_srt_file(srt_file)


if __name__ == "__main__":
    main()