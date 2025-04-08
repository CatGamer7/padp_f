from .base_processor import Base_Processor


class Local_Processor(Base_Processor):

    def distribute(self, in_str: str) -> str:
        return super().clean_string(in_str)
