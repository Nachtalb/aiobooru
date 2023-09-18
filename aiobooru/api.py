from typing import Any, AsyncGenerator, Mapping

from aiohttp import BasicAuth, ClientSession
from yarl import URL

from .base import BooruPost


class BooruFlavour:
    __slots__ = ("post", "schema", "host", "html_post", "html_artist", "api_post", "api_posts")

    post: type[BooruPost]

    schema: str  # https
    host: str  # danbooru.donmai.us

    html_post: str  # posts/123456
    html_artist: str  # posts?tags=artist_name

    api_post: str  # posts/123456.json
    api_posts: str  # posts.json

    @property
    def base_url(self) -> URL:
        return URL(self.schema + "://" + self.host)


class BooruApi:
    def __init__(
        self,
        session: ClientSession,
        flavour: BooruFlavour,
        auth: BasicAuth | Mapping[str, str] | None = None,
        user_agent: str = "",
    ) -> None:
        self.session = session
        self.auth = auth if isinstance(auth, BasicAuth) else None
        self.headers: dict[str, str] = {}
        self.flavour = flavour

        if auth and not isinstance(auth, BasicAuth):
            self.headers.update(auth)

        if user_agent:
            self.headers["User-Agent"] = user_agent

    async def _request(self, url: str | URL, **kwargs: Any) -> Any:
        auth = kwargs.pop("auth", self.auth)
        headers = kwargs.pop("headers", self.headers)

        async with self.session.get(url, auth=auth, headers=headers, **kwargs) as r:
            return await r.json()

    async def get_post(self, post_id: int, **request_kwargs: Any) -> BooruPost | None:
        return self.flavour.post.de_json(
            await self._request(self.flavour.base_url / self.flavour.api_post.format(post_id), **request_kwargs)
        )

    async def get_posts(self, **request_kwargs: Any) -> list[BooruPost]:
        return self.flavour.post.de_jsons(
            await self._request(self.flavour.base_url / self.flavour.api_posts, **request_kwargs),
        )

    async def post_url(self, post_id: int) -> str:
        return str(self.flavour.base_url / self.flavour.html_post.format(post_id))

    async def user_url(self, user_id: int) -> str:
        return str(self.flavour.base_url / self.flavour.html_artist.format(user_id))

    async def download_file(self, url: str | URL, **request_kwargs: Any) -> bytes:
        out = b""
        async for chunk in self.download_file_iter(url, **request_kwargs):
            out += chunk
        return out

    async def download_file_iter(
        self, url: str | URL, chunk_size: int = 4096, **request_kwargs: Any
    ) -> AsyncGenerator[bytes, None]:
        auth = request_kwargs.pop("auth", self.auth)
        headers = request_kwargs.pop("headers", self.headers)

        async with self.session.get(url, auth=auth, headers=headers) as r:
            async for chunk in r.content.iter_chunked(chunk_size):
                yield chunk
