#!/usr/bin/env python3
"""Validate the canonical Git companion and CCS packaging contract."""
import sys
import argparse
from ccs import validate, HOSTS, COMPANIONS


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--companion', default='git-companion', help='ID to validate, defaults to git-companion')
    parser.add_argument('--all', action='store_true', help='validate all canonical companions')
    args = parser.parse_args()
    names = sorted(folder.name for folder in COMPANIONS.iterdir() if folder.is_dir()) if args.all else [args.companion]
    for name in names:
        info = validate(name)
        print(f'PASS CCS {info["ccs_version"]} | {info["id"]} {info["version"]}')
    print(f'PASS Agent Skills metadata, runtime references, manifests, behaviour coverage and {len(HOSTS)} host adapters')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
