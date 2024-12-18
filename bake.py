#!/usr/bin/env python3

import json
import pathlib
import yaml




def bake_json(src_data: dict[str, list[str]], dst_dir: pathlib.Path) -> bool:
    dst_file_expanded: pathlib.Path = dst_dir / 'quotes.json'
    dst_file_minified: pathlib.Path = dst_dir / 'quotes.min.json'

    dump: list[dict[str, str]] = []

    for author, quotes in src_data.items():
        for text in quotes:
            dump.append({'author': author, 'text': text})

    output_expanded: str = json.dumps(obj=dump, ensure_ascii=False, indent=4)
    output_minified: str = json.dumps(obj=dump, ensure_ascii=False, indent=None)

    dst_file_expanded.write_text(output_expanded)
    dst_file_minified.write_text(output_minified)




if __name__ == '__main__':
    REPO_DIR: pathlib.Path = pathlib.Path(__file__).parent.resolve()
    JSON_DIR: pathlib.Path = REPO_DIR / 'json'
    SRC_FILE: pathlib.Path = REPO_DIR / 'source.yaml'
    SRC_DATA: dict[str, list[str]] = yaml.safe_load(stream=SRC_FILE.read_bytes())
    bake_json(src_data=SRC_DATA, dst_dir=JSON_DIR)
