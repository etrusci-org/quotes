# quotes

Curated [words](./markdown/quotes.md) from [people](./authors.txt). Mostly about art and life.

---

## CDN

| File                  | URL                                                                        |
|-----------------------|----------------------------------------------------------------------------|
| Quotes JSON           | `https://cdn.jsdelivr.net/gh/etrusci-org/quotes@main/json/quotes.json`     |
| Quotes JSON minified  | `https://cdn.jsdelivr.net/gh/etrusci-org/quotes@main/json/quotes.min.json` |
| Quotes Markdown       | `https://cdn.jsdelivr.net/gh/etrusci-org/quotes@main/markdown/quotes.md`   |
| Authors JSON          | `https://cdn.jsdelivr.net/gh/etrusci-org/quotes@main/authors.json`         |
| Authors JSON minified | `https://cdn.jsdelivr.net/gh/etrusci-org/quotes@main/authors.min.json`     |
| Authors TXT           | `https://cdn.jsdelivr.net/gh/etrusci-org/quotes@main/authors.txt`          |

---

## Viewer

Fullscreen random quotes viewer. Work in progress.

Base URL: <https://etrusci-org.github.io/quotes/viewer/>

You can override some settings with URL request parameters:

| Parameter | Default | Description |
|----------------|---------------------------|------------------------------------------------------------|
| `update_rate`  | `42`                      | seconds, interval between loading quotes                   |
| `typing_speed` | `80`                      | milliseconds, speed of the typewriter effect, 1000 ms = 1s |
| `src`          | `../json/quotes.min.json` | path to your custom quotes file                            |

Example:

`https://etrusci-org.github.io/quotes/viewer/?update_rate=10&typing_speed=20&src=https://cdn.jsdelivr.net/gh/etrusci-org/quotes@main/json/quotes.min.json`

---

## Maintain Quotes

In case you clone this repo and want to maintain your own quotes:

1. Edit **[_src.json](./_src.json)**
2. `$ python3 bake.py`
