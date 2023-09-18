from .api import BooruFlavour
from .danbooru import DanbooruPost
from .gelbooru import GelbooruPost
from .threedbooru import ThreeDBooruPost
from .yandere import YanderePost


class DanbooruFlavour(BooruFlavour):
    post = DanbooruPost

    host = "danbooru.donmai.us"
    schema = "https"

    html_post = "posts/{}"
    html_artist = "posts?tags={}"

    api_post = "posts/{}.json"
    api_posts = "posts.json"


class SafebooruFlavour(DanbooruFlavour):
    host = "safebooru.org"


class GelbooruFlavour(BooruFlavour):
    post = GelbooruPost

    host = "gelbooru.com"
    schema = "https"

    html_post = "index.php?page=post&s=view&id={}"
    html_artist = "index.php?page=post&s=list&tags={}"

    api_post = "index.php?page=dapi&s=post&q=index&json=1&id={}"
    api_posts = "index.php?page=dapi&s=post&json=1&q=index"


class YandereFlavour(BooruFlavour):
    post = YanderePost

    host = "yande.re"
    schema = "https"

    html_post = "post/show/{}"
    html_artist = "post?tags={}"

    api_post = "post.json?tags=id:{}"
    api_posts = "post.json"


class KonachanFlavour(YandereFlavour):
    host = "konachan.com"


class ThreeDBooruFlavour(BooruFlavour):
    post = ThreeDBooruPost

    host = "behoimi.org"
    schema = "http"

    html_post = "post/show/{}"
    html_artist = "index?tags={}"

    api_post = "post/index.json?tags=id:{}"
    api_posts = "post/index.json"
