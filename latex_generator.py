"""
Python script for generating images of LaTeX equations.
"""

import argparse
from sympy import preview

parser = argparse.ArgumentParser(
    prog="latex-generator.py", description="Generates image of LaTeX equation."
)

parser.add_argument(
    "-f",
    "--file",
    help="""path to file with equation
    (NOTE: this is evaluated second;
    if `--equation` is provided, will NOT be evaluated)"""
)

parser.add_argument(
    "-e", "--equation", help="equation to generate (NOTE: this is evaluated first)"
)

parser.add_argument(
    "-o", "--out", help="path to save image", default="output/image.png"
)

parser.add_argument("--eulerFont", help="use Euler font", default=True, type=bool)

parser.add_argument("--dpi", help="dpi of output image", default=1200, type=int)

args = parser.parse_args()


def main() -> None:
    """
    Runs LaTeX image generator.
    """

    if args.equation is not None:
        preview(
            r"$$" + args.equation + "$$",
            viewer="file",
            filename=args.out,
            euler=args.eulerFont,
            dvioptions=["-D", str(args.dpi)],
        )
        print("image successfully typeset")
    elif args.file is not None:
        raise NotImplementedError("not yet implemented!")


if __name__ == "__main__":
    if args.file is None and args.equation is None:
        print("doing nothing...")
    else:
        main()
