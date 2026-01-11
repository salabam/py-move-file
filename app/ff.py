import os


def move_file(command: str) -> None:
    check_command(command)
    check_source_path(command)
    make_directories(command)
    write_content_to_new_file(command)
    remove_source(command)


def check_command(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "mv":
        raise ValueError("Invalid command format.")

def check_source_path(command: str) -> None:
    source_path = command.split()[1]
    if not os.path.exists(source_path):
        raise FileNotFoundError("Source file does not exist")
    if not os.path.isfile(source_path):
        raise ValueError(f"Source is not a file")


def make_directories(command: str) -> None:
    source_path, destination_path = command.split()[1:]

    if destination_path.endswith("/"):
        source_filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_path, source_filename)

    destination_dir = os.path.dirname(destination_path)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    ######
    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dst_dir = os.path.dirname(dst)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)

def write_content_to_new_file(command: str) -> None:
    source_path, destination_path = command.split()[1:]
    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(destination_path, "w") as destination_file:
        destination_file.write(content)


def remove_source(command: str) -> None:
    os.remove(command.split()[1])