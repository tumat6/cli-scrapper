# cli-scrapper

Small CLI scraping project in Python for extracting book data from `https://books.toscrape.com`.

## What it does

The project runs a simple pipeline:

1. Fetches HTML from a URL (`requests`)
2. Parses HTML into BeautifulSoup (`bs4`)
3. Extracts products from `article.product_pod`
4. Crawls pagination links until there is no next page (or max page limit)
5. Returns a list of dictionaries with:
   - `name`
   - `price`
   - `rating` (converted from words `One..Five` to numbers `1..5`)

## Project structure

- `main.py`: Entrypoint; configures logging and runs the pipeline
- `src/modules/logger.py`: Centralized logger setup (JSON format, console + file handlers)
- `src/modules/crawler.py`: Pagination crawl orchestration
- `src/modules/fetcher.py`: HTTP fetch logic
- `src/modules/parser.py`: BeautifulSoup parser helper
- `src/modules/extractor.py`: Product extraction logic
- `src/modules/cli.py`: CLI argument parser (`url` positional argument)

## Requirements

- Python `>=3.11`
- Dependencies are defined in `pyproject.toml`:
  - `requests`
  - `bs4`
  - `argparse`
  - `logging`
  - `python-json-logger`

## Install

Using `uv` (repo already includes `uv.lock`):

```bash
uv sync
```

Or with pip:

```bash
pip install -e .
```

## Run

Run with a target URL:

```bash
python main.py https://books.toscrape.com/
```

If using the project virtual environment on Windows:

```bash
.\.venv\Scripts\python.exe main.py https://books.toscrape.com/
```

## Logging

Logging is initialized in `main.py` and writes JSON logs to:

- Console (stdout/stderr)
- `logs_pipeline.json` (project root)

Logged events include:

- Pipeline start/completion
- Page-by-page crawl progress
- Extraction counts
- HTTP failures with stack traces

## Example output shape

Extracted items returned by the pipeline look like:

```python
{"name": "A Light in the Attic", "price": "GBP51.77", "rating": 3}
```
