---
name: transcript-commitment-extractor
description: Extract structured data and government commitments from long transcripts. Use when Gemini CLI needs to process large text files (e.g., SONA, speeches, meeting minutes) to extract specific, measurable, and actionable commitments into a structured JSON or CSV format.
---

# Transcript Commitment Extractor

This skill provides a modular, multi-stage workflow for processing large transcripts that exceed standard context limits.

## Core Workflow

For a detailed walkthrough of the extraction stages, see [references/workflow.md](references/workflow.md).

### 1. Pre-processing & Chunking
Use the bundled Python script to divide the raw transcript into manageable segments.
- **Tool**: `scripts/chunker.py`
- **Action**: Run the script on the target text file. It will produce multiple text chunks (e.g., `chunk_1.txt`, `chunk_2.txt`).

### 2. Multi-Stage Extraction
Follow these iterative steps to ensure accuracy:
- **Analyze Segments**: Process each chunk individually using the guidelines in Stage 1 of the workflow.
- **Aggregate Results**: Merge all findings into a single raw dataset.
- **Refine & Validate**: Apply the final schema mapping and validate that every entry contains a supporting quote for traceability.

### 3. Final Export
Format the validated data into its target structure.
- **JSON**: For system-to-system integration.
- **CSV**: For manual analysis, spreadsheet tools, or reporting dashboards.

## Best Practices
- **Always Include Quotes**: Ensure every extracted commitment is backed by a direct excerpt from the transcript.
- **Identify Responsible Parties**: Explicitly link each commitment to an organization or individual.
- **Verify Measurability**: Prioritize items with specific dates, amounts, or measurable targets.
