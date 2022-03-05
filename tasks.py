import invoke
import enum


class Tools(enum.Enum):
    BLACK = "black"


ACTIVATORS = {
    ("*.py",): ("black", "isort", "pylint"),
    ("*.c", "*.cpp", "*.h"): ("clang-format",),
    ("*.js", "*.mjs"): ("prettier", "eslint"),
    ("*.dart",): ("dart",),
}


@invoke.task
def lint_my_project(ctx):
    pass
