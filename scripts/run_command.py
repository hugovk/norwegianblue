from __future__ import annotations

import os
import subprocess


def run(command: str, with_console: bool = True, line_limit: int | None = None) -> None:
    # Use a fixed terminal width for consistent output
    env = os.environ.copy()
    env["COLUMNS"] = "88"
    output = subprocess.run(
        command.split(), capture_output=True, text=True, env=env, check=True
    )
    print()
    if with_console:
        print("```console")
        print(f"$ {command}")

    output = output.stdout.strip()
    if line_limit:
        output = "".join(output.splitlines(keepends=True)[:line_limit]) + "..."
    print(output)

    if with_console:
        print("```")
    print()
