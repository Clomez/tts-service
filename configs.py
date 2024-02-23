config = {
    "path_to_files" : "audio/",
    "path_to_input" : "tmp/input",
    "host" : "http://localhost:5000",
}


tts_config = {
    "speaker_wav" : "tts/fi_sample3.wav", # Custom wav voice
    "speaker" : "Abrahan Mack",
    "model_name" : "tts_models/multilingual/multi-dataset/xtts_v2",

    "split_sentancess" : True,
    "speed" : 1,

    "file_out_path" : "audio/", # Output wav path
    "char_limiter" : 20000,
}