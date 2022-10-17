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

project_dir = pathlib.Path(f"sample_project")

if not project_dir.exists():
    project_dir.mkdir(parents=True, exist_ok=True)


def generate_file(idx: int) -> None:
    template_file = pathlib.Path("hello_world-template.cpp")
    template_text = template_file.read_text()
    template_text = template_text.replace("$python_args$", str(idx))
    new_file = project_dir / pathlib.Path(f"hello_world_{idx}.cpp")

    if not new_file.exists():
        with open(new_file, "w") as f:
            f.write(template_text)

        cmake_filepath = project_dir / pathlib.Path(f"CMakeLists.txt")

        if not cmake_filepath.exists():
            cmake_template_filepath = pathlib.Path("CMakeLists-template.txt")
            template_text = cmake_template_filepath.read_text()
            with open(cmake_filepath, "w") as f:
                f.write(template_text)

        with open(project_dir / pathlib.Path(f"CMakeLists.txt"), "a") as f:
            f.write(f"add_executable(HelloWorld{idx} hello_world_{idx}.cpp)\n")


if __name__ == "__main__":
    for i in range(args.num_files):
        generate_file(i)

    print("Done")
