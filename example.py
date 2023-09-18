import asyncio
from argparse import ArgumentParser

from aiohttp import ClientSession
from aiopath import AsyncPath

from aiobooru import BooruApi, DanbooruFlavour
from aiobooru.base import BooruPost


async def download_to_file(client: BooruApi, post: BooruPost, path: AsyncPath) -> None:
    file_path = path / f"{post.id}.{post.file_ext}"

    if post.file_url is None:
        return

    if await file_path.exists():
        print("Already downloaded post:", post.id)
        return

    data = await client.download_file(post.file_url)
    await file_path.write_bytes(data)

    print("Downloaded post:", post.id)


async def main(limit: int, page: int, tags: list[str], output: str) -> None:
    async with ClientSession() as session:
        client = BooruApi(session, DanbooruFlavour())

        latest_posts = await client.get_posts(params={"limit": limit, "page": page, "tags": " ".join(tags)})
        folder = AsyncPath(output)
        await folder.mkdir(exist_ok=True)

        for task in asyncio.as_completed([download_to_file(client, post, folder) for post in latest_posts]):
            await task


parser = ArgumentParser()
parser.add_argument("-l", "--limit", type=int, default=10)
parser.add_argument("-p", "--page", type=int, default=1)
parser.add_argument("-t", "--tags", type=str, default="", nargs="*")
parser.add_argument("-o", "--output", type=str, default="downloads")
args = parser.parse_args()
asyncio.run(main(limit=args.limit, page=args.page, tags=args.tags, output=args.output))
