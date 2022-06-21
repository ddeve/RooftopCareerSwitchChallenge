import sys
from typing import List
from riddle import Riddle, RiddleMock


def main(opts: List[str]):
    use_mock = False
    use_email = False
    is_verbose = False

    for opt in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit(0)
        elif opt == "--use-mock":
            use_mock = True
        elif "--email=" in opt:
            use_email = True
            email = opt.replace("--email=", "")
        elif opt == "-v":
            is_verbose = True
        else:
            print("Unknown option: '" + opt + "'.")
            print("Use '-h' or '--help' options for help.")
            sys.exit(2)

    if use_mock:
        Service = RiddleMock
    else:
        Service = Riddle

    if use_email:
        Service.email = email

    try:
        token = Service.getToken()

        unsortedBlocks = Service.getBlocks(token=token)
        if is_verbose:
            print("Original Blocks Riddle:")
            print_bloks(unsortedBlocks)

        orderedBlocks = Service.check(blocks=unsortedBlocks, token=token)
        if is_verbose:
            print("Solved Blocks Riddle:")
            print_bloks(orderedBlocks)

        result = Service.verify(blocks=orderedBlocks, token=token)

        if result:
            print("The Riddle is solved")
        else:
            print("Pleace try again")
    except Exception as e:
        print(e)


def print_bloks(blocks: List[str]) -> None:
    for block in blocks:
        print(block)


def print_help() -> None:
    print(
        """

        Usage:

            python main.py [-h --help] [--use-mock] [--email=nombre@empresa.com] [-v]

        Options:

            -h --help:  Show help information.
            --use-mock: Optional. The process is applied using mock data.
            --email: Optional. Set email used for ask the token to Rooftop API.
            -v: Optional. Show Riddle and solution blocks.

        Notes: 

            (*) Default behavior. The process is applied using Rooftop API.

        Examples: 

            python main.py                                (*)
            python main.py -h
            python main.py --help
            python main.py --use-mock
            python main.py --email=daniel.deve@rooftop.com
            python main.py -v

        """
    )


if __name__ == "__main__":
    main(sys.argv[1:])
