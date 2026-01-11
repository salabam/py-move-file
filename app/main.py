import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format.")

    source_path = parts[1]
    if not os.path.exists(source_path):
        raise FileNotFoundError("Source file does not exist")
    if not os.path.isfile(source_path):
        raise ValueError("Source is not a file")

    destination_path = parts[2]
    if destination_path.endswith("/"):
        destination_path = os.path.join(destination_path,
                                        os.path.basename(source_path))

    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    open(destination_path, "w").write(open(source_path).read())
    os.remove(source_path)
