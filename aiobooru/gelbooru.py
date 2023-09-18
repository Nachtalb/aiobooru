from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import model_validator

from .base import BooruPost


class GelbooruPost(BooruPost):
    id: int

    created_at: datetime

    rating: str
    source: str | None
    score: int
    parent_id: int | None
    has_children: bool
    is_pending: bool = False

    tag_string: str

    width: int
    height: int

    md5: str | None

    file_size: int = 0
    file_url: str | None
    file_ext: str | None = None

    owner: str
    change: int
    creator_id: int

    directory: str

    has_comments: bool
    has_notes: bool
    post_locked: bool

    preview_url: str
    preview_height: int
    preview_width: int

    sample_height: int
    sample_url: str
    sample_width: int

    status: str
    title: str

    @model_validator(mode="before")
    @classmethod
    def handle_values(cls, values: dict[str, Any]) -> dict[str, Any]:
        if "file_ext" not in values:
            values["file_ext"] = Path(values["file_url"]).suffix.lstrip(".")

        values["created_at"] = datetime.strptime(values["created_at"], "%a %b %d %H:%M:%S %z %Y")
        return values

    @classmethod
    def de_json(cls, json: dict[str, Any]) -> "GelbooruPost | None":
        if json.get("post"):
            return cls(**json["post"][0])
        return None

    @classmethod
    def de_jsons(cls, json: dict[str, Any]) -> list["GelbooruPost"]:  # type: ignore[override]
        if "post" in json:
            return [cls(**post) for post in json["post"]]
        return []
