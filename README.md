# Lint configurations

Opinionated code-style and rules for various linters and formatters - can be combined with mega-linter.

This repository aims to provide a central source of all necessary configuration for various,
but mainly my own projects or projects that I contribute to.

To get started, either add a `pyproject.toml` or `.nitpick.toml` file to your repository:

```toml
[tool.nitpick]
style = ["github://MrP01/lint-me-now/nitpick-base-style.toml"]
```

And feel free to add more styles, such as

- `nitpick-python-style.toml`
- `nitpick-javascript-style.toml`
- `nitpick-c-cpp-style.toml`
- `nitpick-shell-style.toml`
- `nitpick-latex-style.toml`

To install the underlying tool, _nitpick_, simply

```bash
pipx install nitpick
```

Then, within your repository, execute
`nitpick check`
or `nitpick fix`
