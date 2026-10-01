# gone like summer — project notes

## Standing rules

- **videos.html must always exclude the YouTube short "i miss your love (Malvern Hills)" (video ID `yv69CuKjTPE`).**
  The page (`videos.html`) pulls videos live from the YouTube channel's uploads
  playlist via the YouTube Data API — there's no static list of videos in the
  code, so this video can't be "deleted" from the site; it has to be filtered
  out client-side. The `EXCLUDED_IDS` array near the top of the `<script>`
  block in `videos.html` does this:

  ```js
  const EXCLUDED_IDS = ["yv69CuKjTPE"];
  ```

  Whenever `videos.html` is rewritten, regenerated, or restructured for any
  reason, carry this array (and the `.filter(item => !EXCLUDED_IDS.includes(...))`
  step in `loadYouTubeVideos`) forward. Do not drop it just because the rest
  of the page's structure changes. If the user asks to hide additional
  videos in the future, add their IDs to this same array rather than
  building a new mechanism.
