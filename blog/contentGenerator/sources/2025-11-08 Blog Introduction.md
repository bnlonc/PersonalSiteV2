---
title: "Notes on the new blog section"
description: "Introducing an overhaul to the site, including a new blog page!"
date: "2025-11-08"
tags: ["Tech"]
---
Hey! If you're reading this, you've found the new `Blog` page on my site. This is where I'll sporadically post long(ish)-form discussions when I want to put something out on a public page. I created this both for the purpose of having a blog as well as to experiment with building a content generation workflow from scratch. The first two posts are dated to the dates when I wrote them in their original form. Similarly to the blog page as a whole, these are here to serve as blog posts as well as testing posts for my Markdown-to-HTML conversion script. See the repo at `Projects -> Personal Site` for more details on that.

You may also have noticed that this site has moved from a single-page application architecture to a multi-page application. This was a lengthy refactoring effort that I had to undertake to accommodate the new blog page, as the janky JavaScript-dependent transitions I originally built just wouldn't support it. I also may or may not have discovered that my JavaScript-powered theme management was completely unnecessary and could be handled much more cleanly with CSS rules. Shout out to [Austin](https://www.austinatchley.xyz/), my mentor from my first internship, whose website I ruthlessly inspect-elemented for inspiration while cleaning up this site. 

I was wisely advised that it's not too late to switch to a higher-level framework like React.js or Hugo, but saving myself all that work would've made far too much sense. So, yeah, this page is still native HTML+CSS+JS. The CSS animation for switching between pages is gone, but I was getting sick of looking at it and it was a pain in the ass to maintain as I added to the site. I'm a lover of all things dumb and impractical, but I just don't have the time to keep that around. 

More posts about ham radio and possibly an RSS feed coming soon. 
