# Transcript Extraction Workflow

This workflow ensures high-accuracy extraction from long transcripts by bypassing context window limits and refining results through multiple stages.

## Stage 1: Segmented Extraction
Analyze each chunk individually. For each chunk, identify:
- **Direct Commitments:** Explicit promises, directives, or policy shifts.
- **Contextual Quotes:** The exact text surrounding the commitment.
- **Responsible Party:** The department, agency, or individual tasked with implementation.
- **Metadata:** Specific budget amounts, dates, or measurable targets.

## Stage 2: Aggregation & De-duplication
Consolidate findings from all chunks.
- Combine overlapping commitments found in different chunks.
- Resolve contradictions between segments (if any).
- Group related items to prevent redundancy.

## Stage 3: Schema Mapping & Validation
Transform the aggregated data into the final target schema.
- Map descriptions to a standard "Description" field.
- Normalize organization names.
- Validate that all mandatory fields (Description, Quote, Reasoning) are present.
- Export to the final format (JSON or CSV).
