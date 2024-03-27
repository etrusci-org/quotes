# quotes

Curated [words](./markdown/quotes.md) from [people](./authors.txt). Mostly about art and life.

---

## Files

|Type                   | File                                           | URL                                                         |
|-----------------------|------------------------------------------------|-------------------------------------------------------------|
| Quotes JSON           | [json/quotes.json](./json/quotes.json)         | `https://etrusci-org.github.io/quotes/json/quotes.json`     |
| Quotes JSON minified  | [json/quotes.min.json](./json/quotes.min.json) | `https://etrusci-org.github.io/quotes/json/quotes.min.json` |
| Quotes Markdown       | [markdown/quotes.md](./markdown/quotes.md)     | `https://etrusci-org.github.io/quotes/markdown/quotes.md`   |
| Authors JSON          | [authors.json](./authors.json)                 | `https://etrusci-org.github.io/quotes/authors.json`         |
| Authors JSON minified | [authors.min.json](./authors.min.json)         | `https://etrusci-org.github.io/quotes/authors.min.json`     |
| Authors Plain Text    | [authors.txt](./authors.txt)                   | `https://etrusci-org.github.io/quotes/authors.txt`          |

---

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

---

## Maintain Quotes

In case you clone this repo and want to maintain your own quotes:

1. Edit [_src.json](./_src.json)
2. `$ python3 bake.py`
