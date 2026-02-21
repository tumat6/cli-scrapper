# Changelog

All notable changes to this project are documented in this file.

## [0.1.1] - 2026-02-21

### Added
- Centralized logging module in `src/modules/logger.py`.
- JSON log formatter for structured logs without external logger runtime dependency.
- Dual log handlers:
  - Console output (stream handler)
  - File output to `logs_pipeline.json`
- Pipeline lifecycle logs in `main.py` (start/completion with item count).

### Changed
- `main.py` now initializes logging via `setup_logging()` and reads URL from CLI arguments.
- `crawler.py` now uses structured logger messages instead of `print()`.
- `fetcher.py` now logs request lifecycle and exceptions.
- `parser.py`, `extractor.py`, and `cli.py` now emit debug-level tracing logs.

### Fixed
- Crawler loop now terminates cleanly when there is no next page link.
- Network/request failures are now captured with stack traces through `logger.exception`.
