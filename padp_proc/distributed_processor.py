import os
import dispy
from .base_processor import Base_Processor


class Distributed_Processor(Base_Processor):

    def distribute(self, in_str: str) -> str:
        half_mark = len(in_str) // 2
        part_1, part_2 = in_str[:half_mark], in_str[half_mark:]

        cluster = dispy.JobCluster(
            super().clean_string,
            secret=os.environ.get("DISPY_SECRET")
        )
        job_1 = cluster.submit(part_1)
        job_2 = cluster.submit(part_2)

        return job_1() + job_2()
