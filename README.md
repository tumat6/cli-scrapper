# cli-scrapper

Small CLI scraping project in Python for extracting book data from `https://books.toscrape.com`.

## What it does

The project runs a simple pipeline:

1. Fetches HTML from a URL (`requests`)
2. Parses HTML into BeautifulSoup (`bs4`)
3. Extracts products from `article.product_pod`
4. Returns a list of dictionaries with:
- `name`
- `price`
- `rating` (converted from words `One..Five` to numbers `1..5`)

## Project structure

- `main.py`: Runs the pipeline and prints extracted products
- `src/modules/fetcher.py`: HTTP fetch logic
- `src/modules/parser.py`: BeautifulSoup parser helper
- `src/modules/extractor.py`: Product extraction logic
- `src/modules/cli.py`: CLI argument parser (`--url`)

## Requirements

- Python `>=3.11`
- Dependencies are defined in `pyproject.toml`:
- `requests`
- `bs4`
- `argparse`
- `logging`

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

Current entrypoint:

```bash
python main.py
```

This currently uses a hardcoded URL in `main.py`:

- `https://books.toscrape.com`

## Example output shape

Printed items look like:

```python
{"name": "A Light in the Attic", "price": "GBP51.77", "rating": 3}
```

## Known limitation

`src/modules/cli.py` defines `--url`, but `main.py` does not currently call `parse_arguments()`, so URL input from CLI is not wired into runtime yet.
