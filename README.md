# Multi-Agent Digest

A small, containerized pipeline that ingests plain-text files, summarizes them with OpenAI, prioritizes the most urgent items, and formats a clean daily digest in Markdown.

## How It Works

1. **Ingestor**: concatenates all files in `/data/input` into `/data/ingested.txt`.
2. **Summarizer**: uses the OpenAI API to generate bullet-point summaries in `/data/summary.txt`.
3. **Prioritizer**: scores each summary line by keyword priority and writes `/data/prioritized.txt`.
4. **Formatter**: outputs a nicely formatted digest to `/output/daily_digest.md`.

## Requirements

- Docker + Docker Compose
- An OpenAI API key

## Setup

1. Create a `.env` file in the repo root:

```env
OPENAI_API_KEY="your-key-here"
```

2. Add input files (plain text) under `data/input/`.

## Run

```bash
docker compose up --build
```

When the pipeline finishes, check:

- `output/daily_digest.md`

Intermediate artifacts are written to:

- `data/ingested.txt`
- `data/summary.txt`
- `data/prioritized.txt`

## Project Structure

- `agents/ingestor/` - merges input files into a single text stream
- `agents/summarizer/` - calls OpenAI to produce bullet-point summaries
- `agents/prioritizer/` - scores and sorts lines by urgency keywords
- `agents/formatter/` - writes the final Markdown digest
- `data/input/` - drop your source files here
- `output/` - digest output

## Notes

- The summarizer currently sends the first ~8,000 characters of the ingested text to the model.
- Priority scoring is keyword-based and easy to customize in `agents/prioritizer/app.py`.
- All services run once and exit (no long-running containers).