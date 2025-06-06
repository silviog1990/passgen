# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2024-06-10
### Added
- Cross-platform build scripts: `build.sh` (Linux/macOS) and `build.bat` (Windows).
- Cross-platform run scripts: `run.sh` (Linux/macOS) and `run.bat` (Windows).
- GitHub Actions workflow for automatic builds and artifact uploads on Windows, macOS, and Linux.
- Windows (`.ico`) and macOS (`.icns`) icon support for executables.
- Updated `README.md` with usage, build, and artifact download instructions.
- Project structure section in `README.md`.

### Changed
- Build and test logic moved into platform-specific scripts for easier maintenance.

### Fixed
- Icon selection in build process now works correctly for each OS.

---
Older changes are not tracked.
