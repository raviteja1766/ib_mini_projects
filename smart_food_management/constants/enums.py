import enum

from ib_common.constants import BaseEnumClass


class MealType(BaseEnumClass, enum.Enum):
    PYTHON = "PYTHON"
    JAVA = "JAVA"
    C = "C"
    RUBY = "RUBY"
    CPP = "CPP"
    CS = "CS"
    JAVASCRIPT = "JAVASCRIPT"
    PHP = "PHP"


class MealSizeType(BaseEnumClass, enum.Enum):
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"
    LATEX = "LATEX"
    TEXT = "TEXT"