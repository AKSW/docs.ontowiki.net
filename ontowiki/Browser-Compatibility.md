This document describes our browser policy.

### Google Chrome

Google Chrome is one of our development browsers.

### Firefox

Firefox is one of our development browsers. CSS and JavaScript is implemented for the current Firefox version first. Older versions of Firefox are not supported.

### Safari

Safari is one of our development browsers because some core developers are Mac users.

### Internet Explorer

Since nobody of the core developer is using Windows, this browser is not well supported. Though, we occasionally test Internet Explorer in a virtualisation environment, compatibility is not as far-fetches as with our development browsers.

However, we want full support of MSIE version >= 7 in both, funcionality and display. So eveyone is welcome to submit IE hacks.

The following list sums up component that are currently known to not work in Internet Explorer:

- MSIE does not support alpha layers in PNG images, so we have disabled PNG background images for MSIE.
- RDFauthor, our JavaScript-based editing component relies on W3C's RDFa parser which doesn't work in IE.
