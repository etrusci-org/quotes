# quotes

Curated [words](./markdown/quotes.md) from [people](./author/authors.txt). Mostly about art and life.




## Files

|Type                   | File                                                 | URL                                                            |
|-----------------------|------------------------------------------------------|----------------------------------------------------------------|
| Quotes JSON           | [json/quotes.json](./json/quotes.json)               | `https://etrusci-org.github.io/quotes/json/quotes.json`        |
| Quotes JSON minified  | [json/quotes.min.json](./json/quotes.min.json)       | `https://etrusci-org.github.io/quotes/json/quotes.min.json`    |
| Quotes Markdown       | [markdown/quotes.md](./markdown/quotes.md)           | `https://etrusci-org.github.io/quotes/markdown/quotes.md`      |
| Quotes Text           | [text/quotes.txt](./text/quotes.txt)                 | `https://etrusci-org.github.io/quotes/text/quotes.txt`         |
| Quotes Streamer.bot   | [streamerbot/quotes.dat](./streamerbot/quotes.dat)   | `https://etrusci-org.github.io/quotes/streamerbot/quotes.dat`  |
| Authors JSON          | [author/authors.json](./author/authors.json)         | `https://etrusci-org.github.io/quotes/author/authors.json`     |
| Authors JSON minified | [author/authors.min.json](./author/authors.min.json) | `https://etrusci-org.github.io/quotes/author/authors.min.json` |
| Authors Plain Text    | [author/authors.txt](./author/authors.txt)           | `https://etrusci-org.github.io/quotes/author/authors.txt`      |




## Viewer

Fullscreen random quotes viewer for your big screens.

Base URL: <https://etrusci.org/tool/quotes>

You can override some settings with URL request parameters:

| Parameter      | Default                   | Description                                                  |
|----------------|---------------------------|--------------------------------------------------------------|
| `update_rate`  | `60`                      | Interval between loading quotes in seconds                   |
| `typing_speed` | `80`                      | Speed of the typewriter effect in milliseconds, 1000 ms = 1s |
| `src`          | `../json/quotes.min.json` | Path or URL to your custom quotes file                       |

Keep [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in mind when using a remote URL for `src`. E.g. the CDN must support it.

Examples:

- `https://etrusci.org/tool/quotes?update_rate=10`
- `https://etrusci.org/tool/quotes?typing_speed=20`
- `https://etrusci.org/tool/quotes?src=https://etrusci-org.github.io/quotes/json/quotes.min.json`
- `https://etrusci.org/tool/quotes?update_rate=10&typing_speed=20&src=https://etrusci-org.github.io/quotes/json/quotes.min.json`




## Maintain Quotes

In case you clone this repo and want to maintain your own quotes:

1. Edit [source.json](./source.json)
2. Optionally adjust `STREAMERBOT_*` constants in [bake.py](./bake.py)
3. `$ python3 bake.py`




## License

[The Unlicense](./LICENSE.md)
