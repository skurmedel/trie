# trie

Implementations of a trie in various languages.

This project used to reside at [bitbucket](https://bitbucket.org/skurmedel/trie) but is now hosted here.

## Current status

Right now, there's just an implementation for Python. But it works quite well.

### Python

The Python implementation is very simple and quite speedy. If you find a way to make it quicker (without making a C-lib), please contribute to the project.

To use it, `import trie` and create a new Trie with `trie.Trie()`.

It supports the following actions, `insert`, `contains` and `find_by_prefix`.

The constructor may optionally take an iterable of strings, that will be `insert`:ed.

## License

See individual files for license, some files like the bundled dictionaries are not made by me and thus have other license requirements.

In general, the actual implementations themselves are under New BSD-style or MIT-licenses.