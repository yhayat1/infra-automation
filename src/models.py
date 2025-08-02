from pydantic import BaseModel, Field, field_validator
import re

class VMSpec(BaseModel):
    name: str = Field(..., min_length=1)
    os: str
    cpu: float
    ram: float

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9\-_]*$', value):
            raise ValueError("Invalid VM name format. VM name must start with a letter, allow letters, numbers, hyphens, and underscores.")
        return value

    @field_validator("os")
    @classmethod
    def validate_os(cls, value: str) -> str:
        if value.lower() not in ["ubuntu", "centos", "windows"]:
            raise ValueError("Unsupported OS.")
        return value.lower()

    @field_validator("cpu", "ram")
    @classmethod
    def validate_positive(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("CPU and RAM must be positive numbers.")
        return value