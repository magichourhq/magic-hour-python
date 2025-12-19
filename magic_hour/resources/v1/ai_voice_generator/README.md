# v1.ai_voice_generator

## Module Functions



<!-- CUSTOM DOCS START -->

### Ai Talking Photo Generate Workflow <a name="generate"></a>

The workflow performs the following action

1. upload local assets to Magic Hour storage. So you can pass in a local path instead of having to upload files yourself
2. trigger a generation
3. poll for a completion status. This is configurable
4. if success, download the output to local directory

> [!TIP]
> This is the recommended way to use the SDK unless you have specific needs where it is necessary to split up the actions.

#### Parameters

In Additional to the parameters listed in the `.create` section below, `.generate` introduces 3 new parameters:

- `wait_for_completion` (bool, default True): Whether to wait for the project to complete.
- `download_outputs` (bool, default True): Whether to download the generated files
- `download_directory` (str, optional): Directory to save downloaded files (defaults to current directory)

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_voice_generator.generate(
    style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
    name="Voice Generator audio",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_voice_generator.generate(
    style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
    name="Voice Generator audio",
    wait_for_completion=True,
    download_outputs=True,
    download_directory="outputs"
)
```

<!-- CUSTOM DOCS END -->
### AI Voice Generator <a name="create"></a>

Generate speech from text. Each character costs 0.05 credits. The cost is rounded up to the nearest whole number.

**API Endpoint**: `POST /v1/ai-voice-generator`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `style` | ✓ | The content used to generate speech. | `{"prompt": "Hello, how are you?", "voice_name": "Elon Musk"}` |
| `└─ prompt` | ✓ | Text used to generate speech. Starter tier users can use up to 1000 characters, while Creator, Pro, or Business users can use up to 1000. | `"Hello, how are you?"` |
| `└─ voice_name` | ✓ | The voice to use for the speech. Available voices: Elon Musk, Mark Zuckerberg, Joe Rogan, Barack Obama, Morgan Freeman, Kanye West, Donald Trump, Joe Biden, Kim Kardashian, Taylor Swift, James Earl Jones, Samuel L. Jackson, Jeff Goldblum, David Attenborough, Sean Connery, Cillian Murphy, Anne Hathaway, Julia Roberts, Natalie Portman, Steve Carell, Amy Poehler, Stephen Colbert, Jimmy Fallon, David Letterman, Alex Trebek, Katy Perry, Prince, Kevin Bacon, Tom Hiddleston, Adam Driver, Alan Rickman, Alexz Johnson, Ana Gasteyer, Andrew Rannells, Arden Cho, Bear Grylls, Ben McKenzie, Ben Stiller, Ben Whishaw, Billie Joe Armstrong, Bingbing Li, Bob Barker, Booboo Stewart, Bradley Steven Perry, Bruno Mars, Caity Lotz, Cameron Boyce, Candice Accola, Carrie Underwood, Casey Affleck, Caterina Scorsone, Cedric the Entertainer, Chace Crawford, Chadwick Boseman, Charlie Day, Chris Hemsworth, Chris Martin, Christopher Mintz-Plasse, Dan Fogler, Dan Stevens, Daniel Dae Kim, Danielle Panabaker, Dave Bautista, David Schwimmer, Denis Leary, Derek Mears, Diego Luna, Donald Glover, Donnie Yen, Doutzen Kroes, Dove Cameron, Dr. Dre, Drake Bell, Elle Fanning, Ernie Hudson, Fergie, Forest Whitaker, Francia Raisa, Freddie Highmore, Gillian Jacobs, Gina Carano, Ginnifer Goodwin, Gordon Ramsay, Guy Pearce, Gwendoline Christie, Hailee Steinfeld, Howie Mandel, Hugh Jackman, Hugh Laurie, J. K. Simmons, Jack Black, Jared Leto, Jennifer Carpenter, Kesha, Kris Jenner, Kristen Bell, Lorde, Matt Smith, Marilyn Monroe, Charlie Chaplin, Albert Einstein, Abraham Lincoln, John F. Kennedy, Lucille Ball, A.R. Rahman, Aamir Khan, Ajay Devgn, Akshay Kumar, Alain Delon, Alan Alda, Alan Cumming, Amitabh Bachchan, Ang Lee, Ansel Elgort, Anthony Anderson, Anthony Mackie, Armie Hammer, Asa Butterfield, B.J. Novak, Barbara Eden, Betty White, Bill Nighy, Bill Pullman, Blake Shelton, Bonnie Wright, Brad Paisley, Brendan Gleeson, Brian Cox, Bruno Ganz, Burt Reynolds, Carrie Fisher, Charles Dance, Chiwetel Ejiofor, Chris Pine, Christina Hendricks, Christina Ricci, Cyndi Lauper, Dakota Fanning, Damian Lewis, Dan Aykroyd, Daniel Craig, David Oyelowo, David Tennant, Diane Keaton, Diane Kruger, Dick Van Dyke, Domhnall Gleeson, Dominic Cooper, Donald Sutherland, Drew Carey, Eartha Kitt, Eddie Izzard, Edward Asner, Eli Roth, Elisabeth Moss, Ellen Burstyn, Emile Hirsch, Ezra Miller, Felicity Jones, Fiona Shaw, Florence Henderson, Freida Pinto, Geena Davis, Gemma Arterton, Geri Halliwell, Glenn Close, Gloria Steinem, Greta Gerwig, Gugu Mbatha-Raw, Hans Zimmer, Harry Connick Jr., Harvey Keitel, Helena Bonham Carter, Henry Cavill, Hilary Swank, Hugh Bonneville, Idina Menzel, Imelda Staunton, Ingrid Bergman, Irrfan Khan, Isla Fisher, Iwan Rheon, Jack Lemmon, Janet Jackson, Jason Bateman, Jason Segel, Jennifer Coolidge, Johnny Galecki, Jon Favreau, Joseph Gordon-Levitt, Josh Brolin, Josh Gad, Josh Groban, Julia Louis-Dreyfus, Kristen Stewart, Kristen Wiig, Rooney Mara, Caitriona Balfe, J.J. Abrams, Zoe Saldana | `"Elon Musk"` |
| `name` | ✗ | The name of audio. This value is mainly used for your own identification of the audio. | `"Voice Generator audio"` |

#### Synchronous Client

```python
from magic_hour import Client
from os import getenv

client = Client(token=getenv("API_TOKEN"))
res = client.v1.ai_voice_generator.create(
    style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
    name="Voice Generator audio",
)

```

#### Asynchronous Client

```python
from magic_hour import AsyncClient
from os import getenv

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.v1.ai_voice_generator.create(
    style={"prompt": "Hello, how are you?", "voice_name": "Elon Musk"},
    name="Voice Generator audio",
)

```

#### Response

##### Type
[V1AiVoiceGeneratorCreateResponse](/magic_hour/types/models/v1_ai_voice_generator_create_response.py)

##### Example
`{"credits_charged": 1, "id": "cuid-example"}`

