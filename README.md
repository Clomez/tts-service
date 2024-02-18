# Install
## PIP
pip install tts sounddevice

## XTTS-v2
https://huggingface.co/coqui/XTTS-v2
Git clone https://huggingface.co/coqui/XTTS-v2

not bundled here, since repo is quite large in size.

## Venv (optional)
python -m venv_name venv_loc

activate git bash:
'cd to Script folder inside venv_loc' (important)
'. activate ## dont forget the space'

# Usage
## start backend localy
py [file.py]
py example_code.py
py text-to-file.py

## Send text to read
save text to file
> py client.py < [file]
file will be generated to audio/

## Special attributes
### Title
add title to audio files like "Financial news" (TODO: Not implimented)

## Args
### Lang
English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi).

### Speaker wav
Finnish: tts_models/fi/css10/vit
Different from speaker, can be found from /tts

### Speakers
'Claribel Dervla', 'Daisy Studious', 'Gracie Wise', 'Tammie Ema', 'Alison Dietlinde', 'Ana Florence', 'Annmarie Nele', 'Asya Anara', 'Brenda Stern', 'Gitta Nikolina', 'Henriette Usha', 'Sofia Hellen', 'Tammy Grit', 'Tanja Adelina', 'Vjollca Johnnie', 'Andrew Chipper', 'Badr Odhiambo', 'Dionisio Schuyler', 'Royston Min', 'Viktor Eka', 'Abrahan Mack', 'Adde Michal', 'Baldur Sanjin', 'Craig Gutsy', 'Damien Black', 'Gilberto Mathias', 'Ilkin Urbano', 'Kazuhiko Atallah', 'Ludvig Milivoj', 'Suad Qasim', 'Torcull Diarmuid', 'Viktor Menelaos', 'Zacharie Aimilios', 'Nova Hogarth', 'Maja Ruoho', 'Uta Obando', 'Lidiya Szekeres', 'Chandra MacFarland', 'Szofi Granger', 'Camilla Holmström', 'Lilya Stainthorpe', 'Zofija Kendrick', 'Narelle Moon', 'Barbora MacLean', 'Alexandra Hisakawa', 'Alma María', 'Rosemary Okafor', 'Ige Behringer', 'Filip Traverse', 'Damjan Chapman', 'Wulf Carlevaro', 'Aaron Dreschner', 'Kumar Dahl', 'Eugenio Mataracı', 'Ferran Simen', 'Xavier Hayasaka', 'Luis Moray', 'Marcos Rudaski'

### Split sentances
used to split long text into smaller pieces for better performance.