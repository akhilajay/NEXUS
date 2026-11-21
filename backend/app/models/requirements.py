from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class SourceReference(BaseModel):
    model_config = ConfigDict(extra="forbid")

    document: str = Field(min_length=1)
    chunk_id: str = Field(min_length=1)
    locations: list[str] = Field(default_factory=list)


class Requirement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    requirement_id: str | None
    kind: Literal["functional", "non_functional"]
    statement: str = Field(min_length=1)
    sources: list[SourceReference] = Field(min_length=1)


class OpenQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: str = Field(min_length=1)
    sources: list[SourceReference] = Field(min_length=1)


class RequirementsInventory(BaseModel):
    model_config = ConfigDict(extra="forbid")

    requirements: list[Requirement]
    open_questions: list[OpenQuestion]