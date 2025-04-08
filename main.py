import argparse
from padp_proc import Local_Processor, Distributed_Processor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input filename", required=True)
    parser.add_argument("-o", "--output", help="output filename", required=True)
    args = parser.parse_args()

    proc = Distributed_Processor(args.input, args.output)
    proc()

if __name__ == "__main__":
    main()
