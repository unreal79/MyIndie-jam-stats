import sys
import subprocess
import os
import re


def convert_notebook_to_html(notebook_path):
    if not os.path.exists(notebook_path):
        print(f"Error: File '{notebook_path}' not found.")
        return

    print(f"Converting '{notebook_path}' to HTML...")

    # Using jupyter-nbconvert
    command = [
        "jupyter-nbconvert",
        "--to", "html",
        "--template", "lab",
        "--HTMLExporter.exclude_input=True",
        "--theme", "dark",
        notebook_path
    ]

    try:
        subprocess.run(command, check=True)
        print("Conversion successful!")

        # Cleanup HTML file
        html_path = os.path.splitext(notebook_path)[0] + ".html"
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Robust regex to remove the block
            # Matches the div followed by the h1 with id starting with 0.
            # We use \s* to handle optional whitespace/newlines
            start_marker = r'<div [^>]*class="[^"]*jp-RenderedMarkdown[^"]*"[^>]*>\s*<h1 [^>]*id="0\.'
            end_marker = r'<h1 [^>]*id="3\.'

            # Using re.DOTALL to match across multiple lines
            full_pattern = f"{start_marker}.*?(?={end_marker})"

            new_content = re.sub(full_pattern, "", content, flags=re.DOTALL)

            if len(new_content) != len(content):
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Cleaned up '{html_path}'.")
            else:
                # Debugging: let's try a fallback if the first one fails
                # Maybe the div classes are slightly different in different versions
                print(f"Primary cleanup markers not found in '{html_path}'. Trying fallback...")
                fallback_start = r'<h1 [^>]*id="0\.'
                fallback_pattern = f"{fallback_start}.*?(?={end_marker})"
                new_content = re.sub(fallback_pattern, "", content, flags=re.DOTALL)
                if len(new_content) != len(content):
                    with open(html_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Cleaned up '{html_path}' using fallback (h1 only).")
                else:
                    print(f"Cleanup markers not found in '{html_path}'.")

    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("Error: 'jupyter-nbconvert' command not found. Make sure jupyter is installed and in your PATH.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        notebooks = [f for f in os.listdir('.') if f.endswith('.ipynb')]
        if not notebooks:
            print("Usage: python convert_to_html.py <notebook_file.ipynb>")
            sys.exit(1)

        print(f"No file specified. Found {len(notebooks)} notebooks. Converting all...")
        for nb in notebooks:
            convert_notebook_to_html(nb)
    else:
        for arg in sys.argv[1:]:
            convert_notebook_to_html(arg)
