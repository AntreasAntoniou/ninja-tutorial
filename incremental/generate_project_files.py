import argparse
import os
import pathlib
import sys
import shutil

parser = argparse.ArgumentParser(
    description="Generate project files for a given project"
)
parser.add_argument(
    "--num_files", help="Number of files to generate", type=int, default=10000
)

args = parser.parse_args()


def generate_file(idx: int) -> None:
    template_file = pathlib.Path("hello_world_template.cpp")
    template_text = template_file.read_text()
    template_text = template_text.replace("$python_args$", str(idx))
    new_file = pathlib.Path(f"hello_world_{idx}.cpp")

    with open(new_file, "w") as f:
        f.write(template_text)

    with open(pathlib.Path(f"CMakeLists-{args.num_files}-file-project.txt"), "a") as f:
        f.write(f"add_executable(HelloWorld hello_world_{idx}.cpp\n")


if __name__ == "__main__":
    for i in range(args.num_files):
        generate_file(i)

    print("Done")
