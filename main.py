from padp_proc import Local_Processor, Distributed_Processor


def main():
    proc = Local_Processor("mini_aug.txt", "out.txt")
    proc()

if __name__ == "__main__":
    main()