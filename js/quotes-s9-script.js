"use strict";
const quotes = [
    { author: `Aberjhani`, text: `Poetry, like jazz, is one of those dazzling diamonds of creative industry that help human beings make sense out of the comedies and tragedies that contextualize our lives.` },
    { author: `Adele`, text: `I make music for ears, not eyes.` },
    { author: `Albert Camus`, text: `Don't walk in front of me... I may not follow. Don't walk behind me... I may not lead. Walk beside me... just be my friend.` },
    { author: `Albert Einstein`, text: `The most beautiful experience we can have is the mysterious. It is the fundamental emotion that stands at the cradle of true art and true science.` },
    { author: `Aldous Huxley`, text: `After silence, that which comes nearest to expressing the inexpressible is music.` },
    { author: `Alejandro Jodorowsky`, text: `Birds born in a cage think flying is an illness.` },
    { author: `Alex Gaskarth`, text: `Life's greatest tragedy is not that it will someday end, but that most only live to follow directions and sometimes we end up totally lost.` },
    { author: `Alex Gaskarth`, text: `Music is the soundtrack to every good and bad time we will ever have.` },
    { author: `Amit Kalantri`, text: `Music shouldn't be just a tune, it should be a touch.` },
    { author: `Amit Kalantri`, text: `The job of feets is walking, but their hobby is dancing.` },
    { author: `Andre Gide`, text: `It is better to be hated for what you are than to be loved for what you are not.` },
    { author: `Ani Difranco`, text: `I don't like my language watered down, I don't like my edges rounded off.` },
    { author: `Anne Sexton`, text: `As it has been said: Love and a cough cannot be concealed. Even a small cough. Even a small love.` },
    { author: `Anthony Bourdain`, text: `Maybe that's enlightenment enough: to know that there is no final resting place of the mind; no moment of smug clarity. Perhaps wisdom…is realizing how small I am, and unwise, and how far I have yet to go.` },
    { author: `Aristotle`, text: `The aim of art is to represent not the outward appearance of things, but their inward significance.` },
    { author: `Arnold Bennett`, text: `Its language is a language which the soul alone understands, but which the soul can never translate.` },
    { author: `Arnold Schoenberg`, text: `If it is art, it is not for all, and if it is for all, it is not art.` },
    { author: `Banksy`, text: `Art should comfort the disturbed and disturb the comfortable.` },
    { author: `Benjamin Disraeli`, text: `Most people die with their music still locked up inside them.` },
    { author: `Bill Evans`, text: `When you play music you discover a part of yourself that you never knew existed.` },
    { author: `Bill Hicks`, text: `A man on acid realized that all matter is merely energy condensed to a slow vibration, that we are all one consciousness experiencing itself subjectively, there is no such thing as death, life is only a dream, and we are the imagination of ourselves.` },
    { author: `Bill Hicks`, text: `It's all about money, not freedom. You think you're free? Try going somewhere without money.` },
    { author: `Bill Hicks`, text: `It's just a ride.` },
    { author: `Bill Hicks`, text: `Life is only a dream and we are the imagination of ourselves.` },
    { author: `Bill Hicks`, text: `Listen, the next revolution is gonna be a revolution of ideas.` },
    { author: `Bob Dylan`, text: `Play it fuckin' loud!` },
    { author: `Bob Marley`, text: `None but ourselves can free our minds.` },
    { author: `Bono`, text: `Music can change the world because it can change people.` },
    { author: `Brian Tracy`, text: `It doesn't matter where you are coming from. All that matters is where you are going.` },
    { author: `Bryce W. Anderson`, text: `I've found that no matter what life throws at me, music softens the blow.` },
    { author: `C.G. Drews`, text: `Sharing music is personal because music speaks, it feels, it breathes. And it always says something about you.` },
    { author: `Captain Disillusion`, text: `Love with your heart; use your head for everything else.` },
    { author: `Charles Baudelaire`, text: `Music fathoms the sky.` },
    { author: `Charles Bukowski`, text: `I tell you such fine music waits in the shadows of hell.` },
    { author: `Charles Bukowski`, text: `Poetry is what happens when nothing else can.` },
    { author: `Charles Darwin`, text: `If I had my life to live over again, I would have made a rule to read some poetry and listen to some music at least once every week.` },
    { author: `Chuck Palahniuk`, text: `Losing all hope was freedom.` },
    { author: `Claude Monet`, text: `Everyone discusses my art and pretends to understand, as if it were necessary to understand, when it is simply necessary to love.` },
    { author: `Clive Barker`, text: `Any fool can be happy. It takes a man with real heart to make beauty out of the stuff that makes us weep.` },
    { author: `Confucius`, text: `Music produces a kind of pleasure which human nature cannot do without.` },
    { author: `Daniel Keyes`, text: `Thank God for books and music and things I can think about.` },
    { author: `Denzel Washington`, text: `Some people will never like you because your spirit irritates their demons.` },
    { author: `Dmitri Shostakovich`, text: `When a man is in despair, it means that he still believes in something.` },
    { author: `Donald Miller`, text: `I was outside the Bagdad Theater in Portland one night when I saw a man playing the saxophone. I stood there for fifteen minutes, and he never opened his eyes.` },
    { author: `Dr. Joyce Brothers`, text: `Music is stored in our long-term memory. When we learn something through music, we tend to remember it longer and believe it more deeply.` },
    { author: `Drake`, text: `We live in a generation of not being in love, and not being together. But we sure make it feel like we're together, because we're scared of seeing each other with somebody else.` },
    { author: `E. E. Cummings`, text: `To be nobody but yourself in a world which is doing its best day and night to make you like everybody else means to fight the hardest battle which any human being can fight and never stop fighting.` },
    { author: `Eddie Van Halen`, text: `The hell with the rules. If it sounds right, then it is.` },
    { author: `Edith Sitwell`, text: `My personal hobbies are reading, listening to music, and silence.` },
    { author: `Edward Bulwer Lytton`, text: `Music, once admitted to the soul, becomes a sort of spirit, and never dies.` },
    { author: `Elbert Hubbard`, text: `A friend is someone who knows all about you and still loves you.` },
    { author: `Elie Wiesel`, text: `Music does not replace words, it gives tone to the words.` },
    { author: `Emma Goldman`, text: `If I can't dance to it, it's not my revolution.` },
    { author: `Enigma`, text: `If you understand or if you don't. If you believe or if you doubt. There's a universal justice. And the eyes of truth, are always watching you.` },
    { author: `Erol Ozan`, text: `Dancing is creating a sculpture that is visible only for a moment.` },
    { author: `Flannery O'Connor`, text: `Art never responds to the wish to make it democratic; it is not for everybody; it is only for those who are willing to undergo the effort needed to understand it.` },
    { author: `Frank Ocean`, text: `When you're happy, you enjoy the music but when you're sad, you undestand the lyrics.` },
    { author: `Frank Zappa`, text: `Jazz isn't dead. It just smells funny.` },
    { author: `Frank Zappa`, text: `Without deviation from the norm, progress is not possible.` },
    { author: `Frederick Delius`, text: `Music is an outburst of the soul.` },
    { author: `Friedrich Nietzsche`, text: `And those who were seen dancing were thought to be insane by those who could not hear the music.` },
    { author: `Friedrich Nietzsche`, text: `We have art in order not to die of the truth.` },
    { author: `Friedrich Nietzsche`, text: `Without music, life would be a mistake.` },
    { author: `Friedrich Nietzsche`, text: `You must have chaos within you to give birth to a dancing star.` },
    { author: `G-Eazy`, text: `It all depends on what you value. Figure this out on your own, nobody shows you how to.` },
    { author: `George Bernard Shaw`, text: `Without art, the crudeness of reality would make the world unbearable.` },
    { author: `George Eliot`, text: `It is always fatal to have music or poetry interrupted.` },
    { author: `George Eliot`, text: `Life seems to go on without effort when I am filled with music.` },
    { author: `George Eliot`, text: `There is no feeling, except the extremes of fear and grief, that does not find relief in music.` },
    { author: `George Gershwin`, text: `Life is a lot like jazz - it's best when you improvise.` },
    { author: `Gerard Way`, text: `Would you destroy something perfect in order to make it beautiful?` },
    { author: `Hanif Abdurraqib`, text: `Home is where the heart begins, but not where the heart stays.` },
    { author: `Heinrich Heine`, text: `Where words leave off, music begins.` },
    { author: `Henri Matisse`, text: `Creativity takes courage.` },
    { author: `Henry Wadsworth Longfellow`, text: `Music is the universal language of mankind.` },
    { author: `Hoda Kotb`, text: `I love music. For me, music is morning coffee. It's mood medicine. It's pure magic. A good song is like a good meal-I just want to inhale it and then share a bite with someone else.` },
    { author: `Igor Stravinsky`, text: `I haven't understood a bar of music in my life, but I have felt it.` },
    { author: `Irena Huang`, text: `When words fail music speaks.` },
    { author: `J.K. Rowling`, text: `If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals.` },
    { author: `James Baldwin`, text: `You have to decide who you are and force the world to deal with you, not with its idea of you.` },
    { author: `Jane Austen`, text: `Without music, life would be a blank to me.` },
    { author: `Jean Paul Friedrich Richter`, text: `Music is the moonlight in the gloomy night of life.` },
    { author: `Jeff Zentner`, text: `Music was the only beautiful thing he owned.` },
    { author: `Jessica Carroll`, text: `Music defines us, for it shapes our souls and minds.` },
    { author: `Jim Morrison`, text: `This is the strangest life I have ever known.` },
    { author: `Jodi Picoult`, text: `For better or for worse, music is the language of memory. It is also the language of love.` },
    { author: `John Cage`, text: `The world is teeming; anything can happen.` },
    { author: `John Keats`, text: `There is nothing stable in the world; uproar's your only music.` },
    { author: `Jonathan Anthony Burkett`, text: `Faith is why I'm here today and faith is why I made it through.` },
    { author: `Joni Mitchell`, text: `You don't know what you got till it's gone.` },
    { author: `Joss Whedon`, text: `All worthy work is open to interpretations the author did not intend. Art isn't your pet - it's your kid. It grows up and talks back to you.` },
    { author: `Jules Combarieu`, text: `Music is the art of thinking with sounds.` },
    { author: `Kanye West`, text: `...my music isn't just music - its medicine.` },
    { author: `Karl Lagerfeld`, text: `Music gives color to the air of the moment.` },
    { author: `Ken Thompson`, text: `One of my most productive days was throwing away 1000 lines of code.` },
    { author: `Lady Gaga`, text: `Ignore all hatred and criticism. Live for what you create, and die protecting it.` },
    { author: `Lana Del Rey`, text: `Doing what you love is freedom. Loving what you do is happiness.` },
    { author: `Lao Tzu`, text: `Music in the soul can be heard by the universe.` },
    { author: `Leonard Bernstein`, text: `Music... can name the unnameable and communicate the unknowable.` },
    { author: `Leonard Bernstein`, text: `This will be our reply to violence: to make music more intensely, more beautifully, more devotedly than ever before.` },
    { author: `Leonardo da Vinci`, text: `The noblest pleasure is the joy of understanding.` },
    { author: `Leopold Stokowski`, text: `A painter paints pictures on canvas. But musicians paint their pictures on silence.` },
    { author: `Little Simz`, text: `Don't tell me I shouldn't just because you couldn't.` },
    { author: `Louis Armstrong`, text: `If you have to ask what jazz is, you'll never know.` },
    { author: `Mahatma Gandhi`, text: `Be the change that you wish to see in the world.` },
    { author: `Maria Cristina Mena`, text: `The pianokeys are black and white, but they sound like a million colors in your mind.` },
    { author: `Maria von Trapp`, text: `Music acts like a magic key, to which the most tightly closed heart opens.` },
    { author: `Marilyn Manson`, text: `Music is the strongest form of magic.` },
    { author: `Mark E. Smith`, text: `If you're going to play it out of tune, then play it out of tune properly.` },
    { author: `Mark Twain`, text: `If you tell the truth, you don't have to remember anything.` },
    { author: `Max Heindel`, text: `Music is the soul of language.` },
    { author: `Maya Angelou`, text: `Everything in the universe has a rhythm, everything dances.` },
    { author: `Michael Jackson`, text: `People ask me how I make music. I tell them I just step into it. It's like stepping into a river and joining the flow. Every moment in the river has its song.` },
    { author: `Miles Davis`, text: `It's not the note you play that's the wrong note - it's the note you play afterwards that makes it right or wrong.` },
    { author: `Mitch Albom`, text: `That is often why you come to music, isn't it? To feel that you are not alone?` },
    { author: `Morrissey`, text: `Tried living in the real world instead of a shell, but I was bored before I even began.` },
    { author: `Muse`, text: `Don't waste your time or time will waste you.` },
    { author: `Nick Cave`, text: `It's a beautiful life, if you can find it.` },
    { author: `Nina LaCour`, text: `It was the moment I realized what music can do to people, how it can make you hurt and feel so good all at once.` },
    { author: `Noah Levine`, text: `The inner revolution will not be televised or sold on the Internet. It must take place within one's own mind and heart.` },
    { author: `Oliver Wendell Holmes Senior`, text: `Every now and then a man's mind is stretched by a new idea or sensation, and never shrinks back to its former dimensions.` },
    { author: `Oscar Wilde`, text: `Be yourself; everyone else is already taken.` },
    { author: `Pablo Picasso`, text: `Art is the lie that enables us to realize the truth.` },
    { author: `Pablo Picasso`, text: `Art washes away from the soul the dust of everyday life.` },
    { author: `Pablo Picasso`, text: `Every child is an artist. The problem is how to remain an artist once he grows up.` },
    { author: `Pablo Picasso`, text: `Everything you can imagine is real.` },
    { author: `Pablo Picasso`, text: `Only put off until tomorrow what you are willing to die having left undone.` },
    { author: `Patrick Rothfuss`, text: `Music sounds different to the one who plays it. It is the musician's curse.` },
    { author: `Patrick Rothfuss`, text: `She didn't know any better. Nobody had ever told her she couldn't. Because of this, she moved through the city like some faerie creature. She walked roads no one else could see, and it made her music wild and strange and free.` },
    { author: `Patrick Rothfuss`, text: `Words cannot always do the work we need them to. Music is there for when words fail us.` },
    { author: `Paul Simon`, text: `Music is forever. Music should grow and mature with you, following you right on up until you die.` },
    { author: `Pete Billmann`, text: `We are not here to do what has already been done.` },
    { author: `Pete Wentz`, text: `You can live with me in this house I've built out of writers blocks.` },
    { author: `Plato`, text: `No wealth can ever make a bad man at peace with himself.` },
    { author: `Prince`, text: `Hard to say what's right when all I wanna do is wrong.` },
    { author: `Ransom Riggs`, text: `A song and a smile from someone I cared about could be enough to distract me from all that darkness, if only for a little while.` },
    { author: `Rick Riordan`, text: `You might as well ask an artist to explain his art, or ask a poet to explain his poem. It defeats the purpose. The meaning is only clear thorough the search.` },
    { author: `Rob Sheffield`, text: `There are all kinds of mix tapes. There is always a reason to make one.` },
    { author: `Rob Sheffield`, text: `When we die, we will turn into songs, and we will hear each other and remember each other.` },
    { author: `Rob Sheffield`, text: `When you stick a song on a tape, you set it free.` },
    { author: `Robert Frost`, text: `Forgive, O Lord, my little jokes on Thee. And I'll forgive Thy great big one on me.` },
    { author: `Robert Schumann`, text: `When you play, never mind who listens to you.` },
    { author: `Saliva`, text: `Am I the reason you breathe? Or am I the reason you cry?` },
    { author: `Sanober Khan`, text: `Because some things sometimes aren't ours to hold, but just beautiful to listen to.` },
    { author: `Sarah Dessen`, text: `Music is the great uniter. An incredible force. Something that people who differ on everything and anything else can have in common.` },
    { author: `Sarah Williams`, text: `Though my soul may set in darkness, it will rise in perfect light; I have loved the stars too fondly to be fearful of the night.` },
    { author: `Shannon L. Alder`, text: `Music is feelings in search of words.` },
    { author: `Shinichi Suzuki`, text: `If a musician wants to become a fine artist, he must first become a finer person.` },
    { author: `Sir James Barrie`, text: `If you cannot teach me to fly, teach me to sing.` },
    { author: `SPARTALIEN`, text: `Remember, that times and situations change, but your heart doesn't have to necessarily.` },
    { author: `Staind`, text: `The silence gets us nowhere, nowhere way to fast.` },
    { author: `Stella Adler`, text: `Life beats down and crushes the soul and art reminds you that you have one.` },
    { author: `Steven Tyler`, text: `Songwriting is a bitch. And then it has puppies.` },
    { author: `Sydney Smith`, text: `If I were to begin life again, I would devote it to music. It is the only cheap and unpunished rapture upon earth.` },
    { author: `T.S. Eliot`, text: `Music heard so deeply. That it is not heard at all, but you are the music. While the music lasts.` },
    { author: `Taylor Jenkins Reid`, text: `Art doesn't owe anything to anyone.` },
    { author: `The Narrator of The Stanley Parable`, text: `Perhaps his goal had not been to understand, but to let go.` },
    { author: `The Rolling Stones`, text: `Lose your dream, you lose your mind.` },
    { author: `Thomas Carlyle`, text: `Music is well said to be the speech of angels; in fact, nothing among the utterances allowed to man is felt to be so divine. It brings us near to the infinite.` },
    { author: `Thomas Fuller`, text: `Music is nothing else but wild sounds civilized into time and tune.` },
    { author: `Timothy Leary`, text: `...as a guide and protection. Trust your divinity, trust your brain.` },
    { author: `Timothy Leary`, text: `The goals of an intelligent life, according to Socrates, is to pursue the philosophic quest - to increase one's knowledge of self and world.` },
    { author: `Timothy Leary`, text: `The universe is an intelligence test.` },
    { author: `Timothy Leary`, text: `Think for yourself. Question authority.` },
    { author: `Tom Moon`, text: `The more you love music, the more music you love.` },
    { author: `Tom Petty`, text: `Excuse me if I have some place in my mind where I go time to time.` },
    { author: `Tom Waits`, text: `I like beautiful melodies telling me terrible things.` },
    { author: `Tupac Shakur`, text: `People tend to choke that which they do not understand.` },
    { author: `Tupac Shakur`, text: `Reality is wrong. Dreams are for the real.` },
    { author: `Unknown Author`, text: `Bees don't waste their time explaining to flies why honey is better than shit.` },
    { author: `Unknown Author`, text: `Saying no to someone is saying yes to yourself.` },
    { author: `Unknown Author`, text: `Whoever brings you the most peace should get the most time.` },
    { author: `Victor Hugo`, text: `Music expresses that which cannot be put into words and that which cannot remain silent.` },
    { author: `W.H. Auden`, text: `The most exciting rhythms seem unexpected and complex, the most beautiful melodies simple and inevitable.` },
    { author: `Walter Lippmann`, text: `It requires wisdom to understand wisdom: the music is nothing if the audience is deaf.` },
    { author: `Willem Dafoe`, text: `You have to lose yourself to find yourself.` },
    { author: `Wolfgang Amadeus Mozart`, text: `The music is not in the notes, but in the silence between.` },
];
