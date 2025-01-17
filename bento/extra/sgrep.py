import json
import os
import re
from typing import Iterable, List, Pattern, Type

from semantic_version import Version

from bento.base_context import BaseContext
from bento.parser import Parser
from bento.tool import StrTool
from bento.violation import Violation


class SGrepParser(Parser):
    def parse(self, results: str) -> List[Violation]:
        violations: List[Violation] = []
        checks = json.loads(results).get("results", [])
        for check in checks:
            path = self.trim_base(check["path"])
            start_line = check["start"]["line"]
            start_col = check["start"]["col"]
            # Custom way to get check_name for sgrep-lint:0.1.10
            message = check.get("extra", {}).get("message")
            check_name, message = message.split(":")
            violation = Violation(
                tool_id=SGrepTool.tool_id(),
                check_id=check_name,
                path=path,
                line=start_line,
                column=start_col,
                message=message,
                severity=2,
                syntactic_context=check.get("extra", {}).get("line"),
            )

            violations.append(violation)
        return violations


class SGrepTool(StrTool):
    ANALYZER_NAME = "r2c/sgrep-lint"
    ANALYZER_VERSION = Version("0.1.12")
    FILE_NAME_FILTER = re.compile(r".*")

    @property
    def file_name_filter(self) -> Pattern:
        return self.FILE_NAME_FILTER

    @property
    def project_name(self) -> str:
        return "Python/JS"

    @classmethod
    def tool_id(cls) -> str:
        return "r2c.sgrep"

    @classmethod
    def tool_desc(cls) -> str:
        return "Matches user-provided AST patterns (experimental; requires Docker)"

    def setup(self) -> None:
        # import inside def for performance
        from bento.extra.r2c_analyzer import prepull_analyzers

        prepull_analyzers(self.ANALYZER_NAME, self.ANALYZER_VERSION)

    def run(self, files: Iterable[str]) -> str:
        # import inside def for performance
        from bento.extra.r2c_analyzer import run_analyzer_on_local_code

        targets = [os.path.realpath(p) for p in files]

        ignore_files = {
            e.path for e in self.context.file_ignores.entries() if not e.survives
        }
        return run_analyzer_on_local_code(
            self.ANALYZER_NAME,
            self.ANALYZER_VERSION,
            self.base_path,
            ignore_files,
            targets,
        )

    @classmethod
    def matches_project(cls, context: BaseContext) -> bool:
        return True

    @property
    def parser_type(self) -> Type[Parser]:
        return SGrepParser
