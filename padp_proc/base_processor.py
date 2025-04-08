from abc import ABC, abstractmethod
import time


class Base_Processor(ABC):

    in_filename: str
    out_filename: str

    def __init__(self, in_filename: str, out_filename: str):
        self.in_filename = in_filename
        self.out_filename = out_filename

    @staticmethod
    def clean_string(in_str: str) -> str:
        PUNCT_MAKS = (".", ",", "!", "?", ":", ";", "'", "\"")
        string_list = []

        for char in in_str:
            if (char in PUNCT_MAKS) or char.isdigit():
                continue

            string_list.append(char)

        return "".join(string_list)
    
    @abstractmethod
    def distribute(self, in_str: str) -> str:
        pass

    def __call__(self, *args, **kwds):
        with open(self.in_filename, "r", encoding="UTF-8") as f:
            data_str = f.read()

            start = time.monotonic()
            out_str = self.distribute(data_str)
            elapsed = time.monotonic() - start

            print(f"{round(elapsed, 3)}s, elapsed")
            
            out_f = open(self.out_filename, "w", encoding="UTF-8")
            out_f.write(out_str)
            out_f.close()
