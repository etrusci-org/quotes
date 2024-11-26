#!/usr/bin/env python3

import json
import operator
import pathlib
import shutil
import yaml




def bake_autr(src_data: dict[str, list[str]], dst_dir: pathlib.Path) -> bool:
    dump_f1: list[str] = "\n".join([author for author in src_data.keys()])

    dst_file_f1: pathlib.Path = dst_dir / 'authors.txt'

    try:
        dst_file_f1.write_text(dump_f1)
    except Exception as e:
        print(e)
        return False

    return True


def bake_json(src_data: dict[str, list[str]], dst_dir: pathlib.Path) -> bool:
    dst_file_f1: pathlib.Path = dst_dir / 'quotes.json'
    dst_file_f2: pathlib.Path = dst_dir / 'quotes.min.json'

    try:
        dump_f1 = json.dumps(obj=src_data, indent=4, ensure_ascii=False)
        dump_f2 = json.dumps(obj=src_data, indent=None, ensure_ascii=False)
        dst_file_f1.write_text(dump_f1)
        dst_file_f2.write_text(dump_f2)
    except:
        return False

    return True


def bake_mrkd(src_data: dict[str, list[str]], dst_dir: pathlib.Path) -> bool:
    dump_f1: list[str] = []
    for author, quotes in src_data.items():
        dump_f1.append(f"**{author}**:  ")
        dump_f1.append("\n".join([f"- {q}" for q in quotes]))
        dump_f1.append("")

    dump_f2: list[str] = []
    for author, quotes in src_data.items():
        dump_f2.append("\n".join([f"- \"{q}\" - {author}" for q in quotes]))
    dump_f2.append("")

    dst_file_f1: pathlib.Path = dst_dir / 'quotes-f1.md'
    dst_file_f2: pathlib.Path = dst_dir / 'quotes-f2.md'

    try:
        dst_file_f1.write_text("\n".join(dump_f1))
        dst_file_f2.write_text("\n".join(dump_f2))
    except:
        return False

    return True


def bake_text(src_data: dict[str, list[str]], dst_dir: pathlib.Path) -> bool:
    dump_f1: list[str] = []
    for author, quotes in src_data.items():
        dump_f1.append(f"{author}:")
        dump_f1.append("\n".join([f"- {q}" for q in quotes]))
        dump_f1.append("")

    dump_f2: list[str] = []
    for author, quotes in src_data.items():
        dump_f2.append("\n".join([f"\"{q}\" - {author}" for q in quotes]))
    dump_f2.append("")

    dst_file_f1: pathlib.Path = dst_dir / 'quotes-f1.txt'
    dst_file_f2: pathlib.Path = dst_dir / 'quotes-f2.txt'

    try:
        dst_file_f1.write_text("\n".join(dump_f1))
        dst_file_f2.write_text("\n".join(dump_f2))
    except:
        return False

    return True


def bake_yaml(src_file: pathlib.Path, src_data: dict[str, list[str]], dst_dir: pathlib.Path) -> bool:
    dump_f2: list[str] = []
    for author, quotes in src_data.items():
        dump_f2.append("\n".join([f"- '\"{q}\" - {author}'" for q in quotes]))
    dump_f2.append("")

    dst_file_f1: pathlib.Path = dst_dir / 'quotes-f1.yml'
    dst_file_f2: pathlib.Path = dst_dir / 'quotes-f2.yml'

    try:
        shutil.copy(src=str(src_file), dst=str(dst_file_f1))
        dst_file_f2.write_text("\n".join(dump_f2))
    except:
        return False

    return True




if __name__ == '__main__':
    REPO_DIR: pathlib.Path = pathlib.Path(__file__).parent.resolve()
    AUTR_DIR: pathlib.Path = REPO_DIR / 'author'
    JSON_DIR: pathlib.Path = REPO_DIR / 'json'
    MRKD_DIR: pathlib.Path = REPO_DIR / 'markdown'
    TEXT_DIR: pathlib.Path = REPO_DIR / 'text'
    YAML_DIR: pathlib.Path = REPO_DIR / 'yaml'

    SRC_FILE: pathlib.Path = REPO_DIR / 'source.yml'
    SRC_DATA: dict[str, list[str]] = yaml.safe_load(stream=SRC_FILE.read_bytes())

    print(f"bake_autr {'OK' if bake_autr(src_data=SRC_DATA, dst_dir=AUTR_DIR) else 'BOO'}")
    print(f"bake_json {'OK' if bake_json(src_data=SRC_DATA, dst_dir=JSON_DIR) else 'BOO'}")
    print(f"bake_mrkd {'OK' if bake_mrkd(src_data=SRC_DATA, dst_dir=MRKD_DIR) else 'BOO'}")
    print(f"bake_text {'OK' if bake_text(src_data=SRC_DATA, dst_dir=TEXT_DIR) else 'BOO'}")
    print(f"bake_yaml {'OK' if bake_yaml(src_file=SRC_FILE, src_data=SRC_DATA, dst_dir=YAML_DIR) else 'BOO'}")
