import json
import pyaudio
from vosk import Model, KaldiRecognizer
from analyze.commands import Commands
from analyze.error import MatchError


class Listener:
    __slots__ = ('model', 'rec', 'audio', 'stream')

    def __init__(self):
        self.model = Model("./vosk-model-small-en-us-0.15")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=16000,
        )

    def start_listen(self):
        self.stream.start_stream()
        print('Speech!')
        while True:
            try:
                self.listen()
            except ValueError:
                self.start_listen()

    def listen(self):
        data = self.stream.read(8000)
        rec_data = self.rec.Result() if self.rec.AcceptWaveform(data) else self.rec.PartialResult()
        json_rec_data = json.loads(rec_data)
        if 'partial' in json_rec_data:
            self.partial_result(rec_data)
        if 'text' in json_rec_data:
            self.text_result(rec_data)

    @staticmethod
    def partial_result(rec_data):
        sub_res = json.loads(rec_data)['partial']
        if sub_res:
            print('Rec speech: ', sub_res)

    @staticmethod
    def text_result(rec_data):
        text_result = json.loads(rec_data)['text']
        if text_result:
            print('Rec speech res: ', text_result)
            try:
                name_command, res_com = Commands(text_result).found_command()
                print('Execute command name: ', name_command)
                print('Command result: ', res_com)
            except MatchError as e:
                print(e)