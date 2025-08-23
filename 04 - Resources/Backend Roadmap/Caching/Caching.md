Caching is the process of storing copies of files in a cache, or temporary storage location, so that they can be accessed more quickly. Technically, a cache is any temporary storage location for copies of files or data, but the term is often used in reference to Internet technologies. Web browsers cache HTML files, JavaScript, and images in order to load websites more quickly, while [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) servers cache [DNS records](https://www.cloudflare.com/learning/dns/dns-records/) for faster lookups and [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) servers cache content to reduce [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/).

## What does a browser cache do?

Every time a user loads a webpage, their browser has to download quite a lot of data in order to display that webpage. To shorten page load times, browsers cache most of the content that appears on the webpage, saving a copy of the webpage's content on the device’s hard drive. This way, the next time the user loads the page, most of the content is already stored locally and the page will load much more quickly.

Browsers store these files until their [[time to live (TTL)]] expires or until the hard drive cache is full. (TTL is an indication of how long content should be cached.) Users can also clear their browser cache if desired.

## What does clearing a browser cache accomplish?

Once a browser cache is cleared, every webpage that loads will load as if it is the first time the user has visited the page. If something loaded incorrectly the first time and was cached, clearing the cache can allow it to load correctly. However, clearing one's browser cache can also temporarily slow page load times.
