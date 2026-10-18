import os, shutil, sys, zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
skills = root / "skills"
out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "zips"
shutil.rmtree(out, ignore_errors=True)
out.mkdir(parents=True)
for skill in sorted(p for p in skills.iterdir() if (p / "SKILL.md").is_file()):
    with zipfile.ZipFile(out / f"{skill.name}.zip", "w") as archive:
        for path in sorted(skill.rglob("*")):
            if path.is_file() and path.name != ".DS_Store":
                info = zipfile.ZipInfo(str(path.relative_to(skills)), (1980, 1, 1, 0, 0, 0))
                info.external_attr = (0o100755 if os.access(path, os.X_OK) else 0o100644) << 16
                archive.writestr(info, path.read_bytes())
