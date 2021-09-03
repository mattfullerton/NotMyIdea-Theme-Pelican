## A pelican theme based on 'notmyidea'

This is a theme for the static site generator [pelican](https://github.com/getpelican/pelican).
It's based on the theme 'notmyidea' which is [included in pelican](https://github.com/getpelican/pelican/tree/master/pelican/themes/notmyidea).

The initial commit already has the social media icons removed since their copyright is not entirely sorted out: https://github.com/getpelican/pelican/issues/2179

### Using this theme
Download the folder `notmyidea`.
Run pelican with the argument `-t /path/to/notmyidea` or put the line `THEME = '/path/to/notmyidea'` into the `pelicanconf.py` file.
Take a look at the `pelicanconf.py` provided in this repo to configure theme-specific features.

Add the tag `ArticlePic: images/picture.png` to your article or page to show wide pictures at the top of the page between the navigation bar and the beginning of the article/page. 

### Features
- mobile friendly (but not highly optimized)
- logo and favicon possible
- easy to change colors
- comes with a dark theme (setting can optionally be saved to local storage)
- supports the plugin [`simple-footnotes`](https://github.com/pelican-plugins/simple-footnotes/)
- light bot protection for emails addresses (they can be encrypted so that bots which don't use javascript won't get the email address)
- Optionally show a picture above the article/page title (there can be a default and the picture can be overwritten/removed individually per page).