#!/usr/bin/env python3

import json
import pathlib
import shutil
import yaml




def bake_yaml(src_file: pathlib.Path, dst_dir: pathlib.Path) -> bool:
    try:
        dst_file: pathlib.Path = dst_dir / 'quotes.yml'
        shutil.copy(src=str(src_file), dst=str(dst_file))
    except:
        return False
    else:
        return True


def bake_json(src_data: dict[str, list[str]], dst_dir: pathlib.Path) -> bool:
    try:
        dst_file_expanded: pathlib.Path = dst_dir / 'quotes.json'
        dst_file_minified: pathlib.Path = dst_dir / 'quotes.min.json'
        dump_expanded = json.dumps(obj=src_data, indent=4, ensure_ascii=False)
        dump_minified = json.dumps(obj=src_data, indent=None, ensure_ascii=False)
        dst_file_expanded.write_text(dump_expanded)
        dst_file_minified.write_text(dump_minified)
    except:
        return False
    else:
        return True


def bake_markdown(src_data: dict[str, list[str]], dst_dir: pathlib.Path) -> bool:
    dump: list[str] = [
        "# Quotes",
        "",
    ]

    for author, quotes in src_data.items():
        dump.append(f"## {author}")
        dump.append("")
        for q in quotes:
            dump.append(f"- {q}")
        dump.append("")
        dump.append("")

    try:
        dst_file: pathlib.Path = dst_dir / 'quotes.md'
        dst_file.write_text("\n".join(dump))
    except:
        return False
    else:
        return True




if __name__ == '__main__':
    REPO_DIR: pathlib.Path = pathlib.Path(__file__).parent.resolve()
    JSON_DIR: pathlib.Path = REPO_DIR / 'json'
    YAML_DIR: pathlib.Path = REPO_DIR / 'yaml'
    MRKD_DIR: pathlib.Path = REPO_DIR / 'markdown'
    SRC_FILE: pathlib.Path = REPO_DIR / 'source.yml'
    SRC_DATA: dict[str, list[str]] = yaml.safe_load(stream=SRC_FILE.read_bytes())

    # bake_yaml(src_file=SRC_FILE, dst_dir=YAML_DIR)
    # bake_json(src_data=SRC_DATA, dst_dir=JSON_DIR)
    bake_markdown(src_data=SRC_DATA, dst_dir=MRKD_DIR)
