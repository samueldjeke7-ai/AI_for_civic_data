# SONA 2026 Commitment Extraction Pipeline

## 1. Project Overview
**Objective:** To automate the extraction, structuring, and validation of government commitments from the 2026 State of the Nation Address (SONA).
**Input Source:** `2026_Sona_Transcript.docx` (Official presidential transcript).
**Output:** A structured dataset (`sona_commitments.csv`) for civic data analysis and tracking.

## 2. Data Preparation & Pre-processing
The large transcript was processed to ensure it could be analyzed by language models without context window limitations.

- **Transcript Extraction:** The raw text was extracted from the Word document into `full_transcript.txt`.
- **Text Chunking (`chunker.py`):** 
    - The script divides the 62KB `full_transcript.txt` into smaller, manageable segments.
    - Resulting files: `chunk_1.txt` through `chunk_6.txt`.
    - This allows for parallel processing and maintains high extraction accuracy for specific sections.

## 3. Analysis Workflow
The extraction followed a multi-stage refinement process to ensure no commitments were missed.

### Stage 1: Segmented Extraction
Each chunk was analyzed individually to identify:
- **Direct Commitments:** Specific promises or directives.
- **Contextual Quotes:** Supporting text for verification.
- **Organizations/Agencies:** Responsible parties for implementation.
- **Metadata:** Financial amounts (where specified) and implementation timelines.
- *Outputs: `analysis_1.json`, `analysis_2.json`, `analysis_3.json`*

### Stage 2: Aggregation & De-duplication
The segmented results were consolidated into a single raw dataset.
- *Output: `step2_raw_analysis.json`*

### Stage 3: Structuring & Schema Validation
The raw data was transformed into a strict JSON schema to ensure consistency across all entries.
- *Output: `step3_structured_commitments.json`*

## 4. Final Output Generation
The structured JSON data was exported to `sona_commitments.csv` for use in standard data analysis tools (Excel, Pandas, PowerBI).

### Data Fields:
- **Description:** Clear summary of the commitment.
- **Organization:** The government department or agency responsible.
- **Amount:** Specific budget or financial allocation (e.g., "R2.5 billion", "R500 million").
- **Timeline:** Implementation deadline (e.g., "this year", "by 2030").
- **Quotes:** The exact excerpt from the transcript for traceability.
- **Reasoning:** Technical justification for why the item was flagged as a commitment.

## 5. Technical Environment & Reproducibility
### Repository Structure:
- `/` : Root containing scripts and raw data.
- `/docs/` : Process documentation.

### Traceability:
All steps from raw text to the final CSV are version-controlled in Git. This ensures that any stakeholder can trace a specific CSV entry back to its original quote in the transcript.
