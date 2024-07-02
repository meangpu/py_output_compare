from packaging import version


def update_version(update_type="patch"):
    with open("version.txt", "r") as file:
        current_version = file.read().strip()

    v = version.parse(current_version)

    if update_type == "major":
        new_version = f"{v.major + 1}.0.0"
    elif update_type == "minor":
        new_version = f"{v.major}.{v.minor + 1}.0"
    else:  # patch
        new_version = f"{v.major}.{v.minor}.{v.micro + 1}"

    with open("version.txt", "w") as file:
        file.write(new_version)

    print(f"Version updated from {current_version} to {new_version}")


if __name__ == "__main__":
    import sys

    update_type = sys.argv[1] if len(sys.argv) > 1 else "patch"
    update_version(update_type)
