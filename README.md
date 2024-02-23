# TTS-Services
### TTS-API: Generate & Manage text-to-audio files and, other TTS py scripts using AI latest models
- API interface for generating audio files from text
- Storing, fetching and listing of all generated audio files.
- Simple database implimentation for extra information & meta info storage.
- XTTS-V2 model, and many others.
- Other related and example TTS scripts
    - Text file to audio file script
    - TTS using sockets
    - Example scripts

## Text-To-Audio API interface
provided by route_server.py:

| Desc.   |      Route      |  Method |
|----------|:-------------:|------:|
| request file |  /request | POST |
| get file |    /$id/get   |   GET |
| list files | /list |    GET |
    
### Starting API locally
1. venv is recommended
2. install needed packages using pip
3. init sqlite db
4. start server
```
> py -m venv /path/to/venv
> pip install tts ...
> py resources/scipts/db_init.py
> py route_server.py
```

### Endpoint: Request file
Posting to this endpoint will start a new process which translates text to audio.
endpoint will return link for eventual resource location, from which file can be obtained after the request is fully processed. 

Processing a file will take some time, depending on host machines hardware capabilities.

| Query args |          |                                          |
|------------|----------|------------------------------------------|
| Required   | user     | sender of file, also appears in filename |
| Optional   | theme    | audio theme, like history or finances    |
| Optional   | language | language used for tts reader             |
| Optional   | title    | title for audio recording                |

```
Post example using file with text and curl:

Input data is given with -d @file
> curl -X POST -d @text_to_read_file "localhost:5000/request?theme=Programming&user=clomez&language=en&title=License_grumbles_2"
```


### Endpoint: Get file
returns a file by id, for download.
ID is returned when requesting a new process, or alternatively all IDs are returned by /list endpoint

### Endpoint: Listing all files
List all files and fields stored in database
```
> curl "localhost:5000/list"
```

### System & TTS configs
Some configs are hidden under the hood.
They can be modified by changing the config.py file

### Logs
Route logs error and info into log/log.txt
Reader process fork logs into log/process_log.txt

To avoid conflicting with open files, each process should open their own log and write to that.
Route also has its own log, for readability. these are mostly HTTP and SQL errors and infos.

### Extra args
#### 1.1 Models
Select a model to use for recording voice.
**other args are heavyly related to selected model**
for multi-lingual xtts v2 use: "tts_models/multilingual/multi-dataset/xtts_v2"

List available models via cli:
```
> tts --list_models
```
Name format: type/language/dataset/model

Currently 1 Finnish model:
with model: 'Finnish: tts_models/fi/css10/vit'

#### 1.2 Speaker wav
Different from speaker, can be found from /tts
Short clip to be used for generating the voice.

#### 1.3 Speakers
Speaker voice.
- WILL clash with speaker_wav arg
- Only available with xtts-v2 model

xtts2 speakers:
'Claribel Dervla', 'Daisy Studious', 'Gracie Wise', 'Tammie Ema', 'Alison Dietlinde', 'Ana Florence', 'Annmarie Nele', 'Asya Anara', 'Brenda Stern', 'Gitta Nikolina', 'Henriette Usha', 'Sofia Hellen', 'Tammy Grit', 'Tanja Adelina', 'Vjollca Johnnie', 'Andrew Chipper', 'Badr Odhiambo', 'Dionisio Schuyler', 'Royston Min', 'Viktor Eka', 'Abrahan Mack', 'Adde Michal', 'Baldur Sanjin', 'Craig Gutsy', 'Damien Black', 'Gilberto Mathias', 'Ilkin Urbano', 'Kazuhiko Atallah', 'Ludvig Milivoj', 'Suad Qasim', 'Torcull Diarmuid', 'Viktor Menelaos', 'Zacharie Aimilios', 'Nova Hogarth', 'Maja Ruoho', 'Uta Obando', 'Lidiya Szekeres', 'Chandra MacFarland', 'Szofi Granger', 'Camilla Holmström', 'Lilya Stainthorpe', 'Zofija Kendrick', 'Narelle Moon', 'Barbora MacLean', 'Alexandra Hisakawa', 'Alma María', 'Rosemary Okafor', 'Ige Behringer', 'Filip Traverse', 'Damjan Chapman', 'Wulf Carlevaro', 'Aaron Dreschner', 'Kumar Dahl', 'Eugenio Mataracı', 'Ferran Simen', 'Xavier Hayasaka', 'Luis Moray', 'Marcos Rudaski'

#### 1.4 Language
Language to be used for the recording.
- Available in multi-lingual models.

xtts2 languages:
English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko) Hindi (hi).

#### Split sentances
used to split long text into smaller pieces for better performance.