import os
import dispy
from .base_processor import Base_Processor


class Distributed_Processor(Base_Processor):

    def distribute(self, in_str: str) -> str:
        half_mark = len(in_str) // 2
        part_1, part_2 = in_str[:half_mark], in_str[half_mark:]

        func = super().get_clean_str()
        nodes = os.environ.get("DISPY_NODES").split()
        secret = os.environ.get("DISPY_SECRET")
        client_host = os.environ.get("DISPY_CLIENT_HOST")

        cluster = dispy.JobCluster(func, nodes=nodes, secret=secret, host=client_host)

        job_1 = cluster.submit(part_1)
        job_2 = cluster.submit(part_2)

        cluster.wait(timeout=60)

        r_1 = job_1()
        r_2 = job_2()

        return r_1 + r_2
