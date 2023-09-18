from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import Field, model_validator

from .base import BooruPost


class ThreeDBooruPost(BooruPost):
    id: int

    created_at: datetime

    rating: str
    source: str | None = None
    score: int
    parent_id: int | None = None
    has_children: bool
    has_notes: bool
    has_comments: bool

    tag_string: str = Field(..., alias="tags")

    width: int
    height: int

    md5: str | None = None

    file_size: int
    file_url: str | None = None
    file_ext: str | None = None

    author: str
    change: int
    creator_id: int

    preview_url: str
    preview_height: int
    preview_width: int

    sample_height: int
    sample_url: str
    sample_width: int

    status: str

    @model_validator(mode="before")
    @classmethod
    def handle_values(cls, values: dict[str, Any]) -> dict[str, Any]:
        if "file_ext" not in values:
            values["file_ext"] = Path(values["file_url"]).suffix.lstrip(".")

        values["created_at"] = values["created_at"]["s"]

        return values

    @classmethod
    def de_json(cls, json: list[dict[str, Any]]) -> "ThreeDBooruPost | None":  # type: ignore[override]
        if json:
            return cls(**json[0])
        return None

    @classmethod
    def de_jsons(cls, json: list[dict[str, Any]]) -> list["ThreeDBooruPost"]:  # type: ignore[override]
        return [cls(**post) for post in json]
