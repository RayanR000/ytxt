# ytxt Implementation Guide

## Problem

The repository overview describes a fully local YouTube transcript CLI, but the implementation work is not yet present in the repo. The goal is to turn that product overview into a step-by-step build guide that can be followed to deliver the CLI, caching, formatting, and optional API surface in a predictable order.

## Proposed approach

Build the project in small layers:

1. Establish the project scaffold and CLI entrypoint.
2. Implement YouTube audio extraction locally with `yt-dlp`.
3. Add transcription with `faster-whisper`.
4. Format output for terminal, text, Markdown, SRT, and JSON.
5. Add transcript caching by video ID.
6. Add file output and storage defaults.
7. Wire in optional API/server support if still in scope.
8. Document usage and validate the end-to-end flow.

## Step-by-step implementation guide

1. Inspect the repo structure and choose the runtime/tooling baseline.
   - Confirm package manager, language, and project layout.
   - Create the minimum files needed for a runnable CLI.

2. Scaffold the CLI surface.
   - Define the `ytxt <youtube_url>` command.
   - Add flags for `--output`, `--format`, `--model`, `--timestamps`, and `--no-cache`.
   - Make argument parsing the first stable boundary for the rest of the work.

3. Implement local media download.
   - Use `yt-dlp` to resolve and extract audio.
   - Keep the download path local and temporary.
   - Fail clearly when the URL is invalid or media cannot be fetched.

4. Implement transcription.
   - Load `faster-whisper` with a sensible default model.
   - Support CPU/GPU selection based on availability.
   - Return a structured transcript representation that downstream formatters can reuse.

5. Add transcript formatting.
   - Render plain text for terminal output.
   - Render Markdown, SRT, and JSON from the same structured transcript data.
   - Preserve timestamps when requested.

6. Add caching.
   - Cache transcripts by video ID.
   - Check cache before downloading or transcribing.
   - Make cache usage controllable with `--no-cache`.

7. Add file output and storage defaults.
   - Write to a user-specified output path when provided.
   - Fall back to `./transcripts/` when a file output is requested but no path is given.
   - Keep terminal output as the default when no file is requested.

8. Add optional local API/server support.
   - Keep this separate from the core CLI path.
   - Expose transcript retrieval in a way that can serve browser extensions or other tools.

9. Document behavior.
   - Update README usage examples.
   - Document defaults, cache behavior, and output formats.
   - Add any implementation notes that future maintainers will need.

10. Validate the full flow.
    - Test a successful transcript run.
    - Test repeated runs to confirm cache hits.
    - Test each output format and file-writing path.

## Todos

- Define the CLI interface and supported flags.
- Build the local download pipeline.
- Build transcription and transcript data modeling.
- Add formatting for terminal, text, Markdown, SRT, and JSON.
- Add cache lookup and writeback by video ID.
- Add output-path handling and transcript directory fallback.
- Decide whether the optional API/server is part of the first implementation pass.
- Update docs after the implementation is stable.

## Notes

- The overview emphasizes local-only processing, so the implementation should avoid external APIs.
- Caching and streaming are core product traits, not afterthoughts.
- The optional API/server should stay decoupled so the CLI remains the primary path.
