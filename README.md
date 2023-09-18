# aiobooru

Asynchronous Python package to interact with various image boards like Danbooru,
Yandere, Gelbooru, and more. Built to be extendable through "Flavours" and
"Post" classes for different image board APIs.

## Installation

### Using Poetry

```bash
poetry add aiobooru
```

### From Source

```bash
git clone https://github.com/Nachtalb/aiobooru.git
cd aiobooru
poetry install
```

## Basic Usage

You can find a detailed example in the `example.py` file in the repository. To
run the example script:

```bash
python example.py --limit 10 --page 1 --tags "tag1 tag2" --output "./downloads"
```

## Extendability

- Create your own Flavour or Post class for other image boards.
- Example of a custom post class: `YanderePost`.

## Authentication

- Basic Auth or headers dictionary.
- Custom user-agent supported.

## API

### `BooruApi`

- `__init__(session, flavour, auth=None, user_agent="")`: Initializes the API
  client.
- `get_post(post_id, **kwargs)`: Get a single post.
- `get_posts(**kwargs)`: Get a list of posts.
- `post_url(post_id)`: Generate the URL for a post.
- `user_url(user_id)`: Generate the URL for a user.
- `download_file(url, **kwargs)`: Download a file as bytes.
- `download_file_iter(url, chunk_size=4096, **kwargs)`: Download a file in
  chunks.

## Contributing

Open for PRs and issues. Follow existing coding style.

## License

Licensed under LGPL 3.0.
