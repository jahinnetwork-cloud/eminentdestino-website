ASSETS FOLDER
=============
Put these files here and the website will use them automatically:

  logo.png      Your main logo (PNG with transparent or white background, about 400px wide).
  hero.mp4      Homepage video (H.264 + AAC, ideally under 15 MB).
  hero.webm     Optional. Same video as WebM (smaller in Chrome/Firefox/Android).

If these files are missing, the site falls back to:
  logo   ->  https://storage.jahinmusic.com/2026-09-18%2023.58.40.jpg
  video  ->  https://storage.jahinmusic.com/0717.mp4  then  0717.mov
and finally to a clean EDO wordmark and an animated orange background.

CONVERT YOUR .MOV TO A WEB-FRIENDLY MP4 (works on iPhone, Android, Mac, Windows):

  ffmpeg -i 0717.mov -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 26 -preset slow \
         -vf "scale='min(1280,iw)':-2" -movflags +faststart -c:a aac -b:a 128k hero.mp4

Optional WebM:

  ffmpeg -i 0717.mov -c:v libvpx-vp9 -crf 34 -b:v 0 -vf "scale='min(1280,iw)':-2" -c:a libopus hero.webm
