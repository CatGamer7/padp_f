from .base_processor import Base_Processor


class Local_Processor(Base_Processor):

    def distribute(self, in_str: str) -> str:
        func = super().get_clean_str()
        return func(in_str)
