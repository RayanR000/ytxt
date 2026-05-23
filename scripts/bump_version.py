#!/usr/bin/env python3
import re
import sys
import subprocess
from pathlib import Path

def bump_version(part):
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    
    # Find current version
    match = re.search(r'version = "(.*?)"', content)
    if not match:
        print("Error: Could not find version in pyproject.toml")
        sys.exit(1)
    
    current_version = match.group(1)
    major, minor, patch = map(int, current_version.split("."))
    
    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        print("Usage: python bump_version.py [major|minor|patch]")
        sys.exit(1)
        
    new_version = f"{major}.{minor}.{patch}"
    print(f"Bumping version: {current_version} -> {new_version}")
    
    # Update pyproject.toml
    new_content = re.sub(r'version = ".*?"', f'version = "{new_version}"', content)
    pyproject_path.write_text(new_content)
    
    # Git operations
    try:
        subprocess.run(["git", "add", "pyproject.toml"], check=True)
        subprocess.run(["git", "commit", "-m", f"chore: bump version to {new_version}"], check=True)
        subprocess.run(["git", "tag", "-a", f"v{new_version}", "-m", f"Release v{new_version}"], check=True)
        print(f"\nSuccessfully bumped to v{new_version}!")
        print(f"Run 'git push origin main --tags' to trigger the automated release.")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py [major|minor|patch]")
    else:
        bump_version(sys.argv[1])
