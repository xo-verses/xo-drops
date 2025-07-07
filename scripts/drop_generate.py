"""Generate scaffold for a new XO drop variant."""
import pathlib, sys, datetime, uuid, shutil, textwrap, yaml

def main(slug: str):
    d = pathlib.Path("drops") / slug
    if d.exists():
        print(f"{slug} already exists")
        return
    (d / "assets").mkdir(parents=True)
    (d / "pod").mkdir()
    (d / "README.md").write_text(f"# {slug} drop")
    meta = {
        "uuid": str(uuid.uuid4()),
        "seal": slug,
        "created": str(datetime.date.today()),
        "signed": False,
    }
    (d / "coin.yml").write_text(yaml.safe_dump(meta))
    print(f"Scaffolded {slug}")

if __name__ == "__main__":
    main(sys.argv[1])
