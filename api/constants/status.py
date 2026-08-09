from enum import Enum


class Status(Enum):
    ACTIVE = (1, "Active")
    INACTIVE = (2, "Inactive")
    REVOKED = (3, "Revoked")
    PENDING = (4, "Pending")

    def __init__(self, code: int, value: str):
        self.code = code
        self._value_ = value

    @classmethod
    def get_by_code(cls, code_name: str) -> 'Status':
        try:
            return cls[code_name.upper()]
        except KeyError:
            raise ValueError(f"'{code_name}' is not a valid Status code name")

    @classmethod
    def get_by_value(cls, code_val: int) -> 'Status':
        for status in cls:
            if status.code == code_val:
                return status
        raise ValueError(f"'{code_val}' is not a valid Status integer code")
