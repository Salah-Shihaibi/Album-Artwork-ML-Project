import configparser
import os

config = configparser.ConfigParser()
if not config.has_section("MASTER"):
    config.add_section("MASTER")
    config.set(
        "MASTER",
        "init-hook",
        f"'import sys; sys.path.append('{os.path.dirname(os.path.abspath('.pylintrc'))}')'",
    )
    config.set(
        "MASTER",
        "disable",
        """C0114,
    C0115,
    C0116,
    C0103,
    R0903""",
    )
    config.add_section("conftest.py")
    config.set("conftest.py", "disable", "W0621")

with open(".pylintrc", "w", encoding="ASCII") as cfg_file:

    config.write(cfg_file)
