const QUOTES_SRC = 'https://cdn.jsdelivr.net/gh/etrusci-org/quotes@main/json/quotes.min.json'
const QUOTES_UPDATE_RATE = 30 * 1000
const TARGET_SELECTOR = '.quotes'
const TYPING_SPEED = 60




async function runRandomQuotesViewer()
{
    const quotes = await fetchJSON(QUOTES_SRC)

    const setRandomBG = () => {
        document.body.style.backgroundColor = `#${getRandomColorHex()}`
    }

    setRandomBG()

    RandomQuoteTyper.targetSelector = TARGET_SELECTOR
    RandomQuoteTyper.typingSpeed = TYPING_SPEED
    RandomQuoteTyper.init(quotes)
    RandomQuoteTyper.typeQuote()


    setInterval(() => {
        setRandomBG()
        RandomQuoteTyper.typeQuote()
    }, QUOTES_UPDATE_RATE)
}




window.addEventListener('load', () => {
    runRandomQuotesViewer()
}, false)
