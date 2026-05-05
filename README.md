# Video Localization QA Pipeline Demo

A small portfolio project demonstrating a video localization QA workflow for game and interactive media content.

This project focuses on identifying, documenting, and reporting localization issues in a short video demo, using subtitles, QA documentation, a glossary, Python validation scripts, and a structured QA report.

## Project Overview

The goal of this project is to simulate a practical localization QA pipeline for video/game content.

The demo includes:

* EN/ES subtitle files
* Localization QA checklist
* Subtitling guidelines
* Issue severity guide
* QA workflow documentation
* Sample QA report in CSV format
* Python scripts for subtitle validation and QA summary generation
* Screenshots for visual documentation

This project was created as part of my transition into localization QA, audio localization, and technical QA workflows for games.

## Screenshots

### Intro Panel in Unreal

!\[Intro panel in Unreal](images/01\_intro\_panel\_unreal.jpg)

### Unreal Demo Overview

!\[Project overview in Unreal](images/02\_project\_overview\_unreal.jpg)

### Title and Terminology Issues

!\[Title and terminology issues](images/03\_title\_and\_terminology\_issues.jpg)

### Language Switch Feedback Typo

!\[Language switch feedback typo](images/04\_language\_switch\_feedback\_typo.jpg)

### Basic Ambience UI Issues

!\[Basic ambience UI issues](images/05\_basic\_ambience\_issues.jpg)

### QA Report CSV

!\[QA report CSV](images/06\_qa\_report\_csv.png)

### Python QA Summary

!\[Python QA summary](images/07\_python\_qa\_summary.png)

### Project Structure

!\[Project structure](images/08\_project\_structure.png)

## Key Skills Demonstrated

* Localization QA
* Subtitle QA
* EN/ES linguistic review
* Bug reporting
* QA documentation
* Glossary usage
* Reading speed checks
* Python scripting for QA support
* Structured CSV reporting
* Video review workflow
* Attention to UI, subtitle, terminology, and consistency issues

## Project Structure

```text
video-localization-qa-pipeline-demo/
|
|-- assets/
|   |-- glossary/
|   |   |-- glossary\\\\\\\_en\\\\\\\_es.csv
|   |
|   |-- subtitles/
|   |   |-- video\\\\\\\_qa\\\\\\\_sample\\\\\\\_en.srt
|   |   |-- video\\\\\\\_qa\\\\\\\_sample\\\\\\\_es.srt
|   |
|   |-- video\\\\\\\_references/
|       |-- video\\\\\\\_links.md
|
|-- csv/
|   |-- qa\\\\\\\_report\\\\\\\_sample.csv
|
|-- docs/
|   |-- issue\\\\\\\_severity\\\\\\\_guide.md
|   |-- localization\\\\\\\_qa\\\\\\\_checklist.md
|   |-- qa\\\\\\\_workflow.md
|   |-- subtitling\\\\\\\_guidelines.md
|   |-- video\\\\\\\_qa\\\\\\\_plan.md
|   |-- video\\\\\\\_script\\\\\\\_and\\\\\\\_issues.md
|
|-- images/
|
|-- scripts/
|   |-- 01\\\\\\\_validate\\\\\\\_srt\\\\\\\_structure.py
|   |-- 02\\\\\\\_check\\\\\\\_subtitle\\\\\\\_reading\\\\\\\_speed.py
|   |-- 03\\\\\\\_generate\\\\\\\_qa\\\\\\\_summary.py
|
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## QA Scope

The QA review covers several types of localization and presentation issues:

* Spelling mistakes
* Typos
* Terminology inconsistencies
* Mixed language issues
* Subtitle/audio mismatch
* Text overflow
* UI display problems
* Reading speed issues
* Visual consistency issues
* Naming consistency issues

## Example Issues Covered

The sample QA report includes intentional issues such as:

* Incorrect spelling in UI text
* Mixed English and Spanish UI content
* Subtitle text overflowing the screen
* Subtitle/audio mismatch
* Incorrect terminology
* Inconsistent button naming
* Visual inconsistency in UI buttons
* Long subtitles affecting readability

## Python Scripts

The project includes small Python scripts to support the QA workflow.

### 01\_validate\_srt\_structure.py

Validates the basic structure of the subtitle files.

It checks:

* Subtitle index format
* Timecode structure
* Empty lines
* General SRT formatting

### 02\_check\_subtitle\_reading\_speed.py

Checks subtitle reading speed and helps identify lines that may be too long or difficult to read comfortably.

### 03\_generate\_qa\_summary.py

Generates a summary from the QA report CSV file.

This helps quickly review the number and type of issues found during the QA pass.

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Current dependencies:

```text
pandas
openpyxl
srt
```

## How to Run the Scripts

From the project root, run:

```bash
python scripts/01\\\\\\\_validate\\\\\\\_srt\\\\\\\_structure.py
python scripts/02\\\\\\\_check\\\\\\\_subtitle\\\\\\\_reading\\\\\\\_speed.py
python scripts/03\\\\\\\_generate\\\\\\\_qa\\\\\\\_summary.py
```

## QA Report

The main QA report is located at:

```text
csv/qa\\\\\\\_report\\\\\\\_sample.csv
```

It contains sample localization issues with fields such as:

* Timecode
* Category
* Issue type
* Severity
* Current text
* Expected result
* Notes

## Video Reference

The edited video file is not included in the repository because of file size and version-control best practices.

Video reference information can be found in:

```text
assets/video\\\\\\\_references/video\\\\\\\_links.md
```

## Notes

Large media files and editing project files are excluded from the repository through `.gitignore`.

This includes:

* Video files
* Audio files
* Filmora project files
* Render/export folders
* Temporary files

## About

Created by Pablo Flores Alosi.

Portfolio: https://pablofalosi.wixsite.com/home  
LinkedIn: https://www.linkedin.com/in/pablofloresalosi/  
GitHub: https://github.com/PabloFloresAlosi

