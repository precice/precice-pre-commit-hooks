# pre-commit hooks for preCICE

This repo contains [pre-commit](https://github.com/pre-commit/pre-commit) hooks for [preCICE](https://github.com/precice/precice).

## Versioning of this repo

Hooks cover a major version of preCICE.
The version is `vX.Y`, where `X` is the major version of preCICE and `Y` is the release of the hook.

Thus, if you plan to use these hooks with preCICE version `2.3.1`, then only the `2` is important for the hook version.

## Using the hooks

Add this to your `.pre-commit-config.yaml` in the root of your project:

```yaml
-   repo: https://github.com/precice/precice-pre-commit-hooks
    rev: ''  # Use the tag you want to use
    hooks:
    -   id: format-precice-config
        exclude: '^thridparty' # optionally exclude directories here
```

**Note:**
The hook will treat every `.xml` file as a preCICE configuration file.
You may need to exclude directories using `exclude`.

## Hooks

### format-precice-config

Formats given preCICE configuration files.
Returns 0 on success, 1 on error, and 2 if a file was modified.
