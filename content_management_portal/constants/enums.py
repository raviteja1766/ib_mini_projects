import enum

from ib_common.constants import BaseEnumClass


class CodeLanguageType(BaseEnumClass, enum.Enum):
    PYTHON = "PYTHON"
    JAVA = "JAVA"
    C = "C"
    RUBY = "RUBY"
    CPP = "CPP"
    CS = "CS"
    JAVASCRIPT = "JAVASCRIPT"
    PHP = "PHP"


class DescriptionType(BaseEnumClass, enum.Enum):
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"
    LATEX = "LATEX"
    TEXT = "TEXT"
