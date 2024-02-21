# TTS-Service
Text to speak using AI models

## Installation
### PIP
pip install tts sounddevice

### XTTS-v2 (is this even needed?)
https://docs.coqui.ai/en/latest/
https://huggingface.co/coqui/XTTS-v2
Git clone https://huggingface.co/coqui/XTTS-v2

not bundled here, since repo is quite large in size.

### Venv (optional)
> python -m venv_name venv_loc

activate git bash:
> 'cd to Script folder inside venv_loc' (important)
> '. activate ## dont forget the space'

### Local setup
Run script init_workspace.bash/sh

## Local usage
### start flask API (flask / server)
Start local data API
> py route_server.py

routes:
route_server.py

### Send text to read (socket)
save text to file
> py client.py < [file]
file will be generated to audio/

### Special args
#### Title
add title to audio files like "Financial news" (TODO: Not yet implimented)

### Args
#### 1.1 Models
Select a model to use for recording voice.
**other args are heavyly related to selected model**
for multi-lingual xtts v2 use: "tts_models/multilingual/multi-dataset/xtts_v2"

> tts --list_models
Name format: type/language/dataset/model

Finnish:
with model: 'Finnish: tts_models/fi/css10/vit'

#### 1.2 Speaker wav
Different from speaker, can be found from /tts

#### 1.3 Speakers
Speaker voice.

- WILL clash with speaker_wav arg
- Very Model dependant

xtts2 speakers:
'Claribel Dervla', 'Daisy Studious', 'Gracie Wise', 'Tammie Ema', 'Alison Dietlinde', 'Ana Florence', 'Annmarie Nele', 'Asya Anara', 'Brenda Stern', 'Gitta Nikolina', 'Henriette Usha', 'Sofia Hellen', 'Tammy Grit', 'Tanja Adelina', 'Vjollca Johnnie', 'Andrew Chipper', 'Badr Odhiambo', 'Dionisio Schuyler', 'Royston Min', 'Viktor Eka', 'Abrahan Mack', 'Adde Michal', 'Baldur Sanjin', 'Craig Gutsy', 'Damien Black', 'Gilberto Mathias', 'Ilkin Urbano', 'Kazuhiko Atallah', 'Ludvig Milivoj', 'Suad Qasim', 'Torcull Diarmuid', 'Viktor Menelaos', 'Zacharie Aimilios', 'Nova Hogarth', 'Maja Ruoho', 'Uta Obando', 'Lidiya Szekeres', 'Chandra MacFarland', 'Szofi Granger', 'Camilla Holmström', 'Lilya Stainthorpe', 'Zofija Kendrick', 'Narelle Moon', 'Barbora MacLean', 'Alexandra Hisakawa', 'Alma María', 'Rosemary Okafor', 'Ige Behringer', 'Filip Traverse', 'Damjan Chapman', 'Wulf Carlevaro', 'Aaron Dreschner', 'Kumar Dahl', 'Eugenio Mataracı', 'Ferran Simen', 'Xavier Hayasaka', 'Luis Moray', 'Marcos Rudaski'

#### 1.4 Lang
Language to be used for the recording.
- Available in multi-lingual models.

xtts2 languages:
English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi).

#### Split sentances
used to split long text into smaller pieces for better performance.