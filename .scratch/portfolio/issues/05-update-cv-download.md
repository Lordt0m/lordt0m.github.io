# 05 Update CV download

**Status:** complete

## Outcome

Publish the revised one-page CV through the portfolio's existing Download CV action.

## Acceptance

- [x] Replace `assets/documents/ayotomiwa-ojo-cv.pdf` with the reviewed PDF exported from the updated editable CV.
- [x] Keep the existing homepage download path and verify the PDF's text, links, and one-page layout.
- [x] Run structural verification and unit tests.
- [x] Push the change to `main` and confirm the Cloudflare Pages download matches the committed PDF.

## Completion record

The revised PDF is one page with eight active link annotations. Its extracted text contains ShelfSum, Credence, the current Cloudflare portfolio URL, the 271-test ShelfSum release baseline, the 35-test Credence release baseline, and the verified education details. It contains none of the superseded project names or former GitHub Pages URL. The PDF hash is `7845608e966e6e68d25aa9c3eefa0b86594df4be0b64faa8302c8662db69f70d`.

`python scripts/verify_site.py` passed with zero errors; `python -m unittest discover tests` passed 30 tests; `git diff --check` passed. The PDF update was pushed as commit `afa880e9266db7e94feb61f0003a12fe9edafb97`. GitHub Actions verification run `35956228542` completed successfully. The Cloudflare Pages download returned HTTP 200 with `application/pdf` and matched the committed PDF's SHA-256 hash byte for byte. The homepage download path stayed unchanged, so no layout or interaction changes were required.
