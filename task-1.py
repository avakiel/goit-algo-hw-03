from pathlib import Path
import shutil
import argparse


def copy_tree(source: Path, destination: Path) -> None:
    try:
        if not source.exists():
            print(f"Error: Source directory '{source}' does not exist.")
            return
        
        if not source.is_dir():
            print(f"Error: '{source}' is not a directory.")
            return

        items = list(source.iterdir())
        
        if not items:
            return
        
        for item in items:
            try:
                if item.is_dir():
                    copy_tree(item, destination)
                elif item.is_file():
                    extension = item.suffix[1:] if item.suffix else "no_extension"
                    
                    extension_dir = destination / extension
                    extension_dir.mkdir(parents=True, exist_ok=True)
                    
                    dest_file = extension_dir / item.name
                    shutil.copy2(item, dest_file)
                    print(f"Copied {item} to {dest_file}")
            except (OSError, PermissionError) as e:
                print(f"Error accessing {item}: {e}")
    except (OSError, PermissionError) as e:
        print(f"Error accessing directory {source}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Recursively copy files from source directory to destination, "
                    "sorting them into subdirectories by file extension.",
        epilog="Example: python task-1.py ./root"
    )
    parser.add_argument(
        "source",
        type=str,
        help="Path to the source directory (e.g., ./root)"
    )
    parser.add_argument(
        "destination",
        type=str,
        nargs="?",
        default="dist",
        help="Path to the destination directory (default: dist)"
    )
    
    args = parser.parse_args()
    
    source_path = Path(args.source)
    destination_path = Path(args.destination)
    
    copy_tree(source_path, destination_path)


if __name__ == "__main__":
    main()
