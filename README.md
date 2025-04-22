# Install
1. Go to [releses page](https://github.com/kotobot/puzzle/releases/tag/v1.2) and copy link to the wheel [file](https://github.com/kotobot/puzzle/releases/download/v1.2/puzzle-0.1.0-py3-none-any.whl).
2. Create new virtual environment and activate it, e.g.:
```bash
mkdir games
cd games
python -m venv .venv
source .venv/bin/activate
```
3. Install the wheel using copied link:
```bash
pip install https://github.com/kotobot/puzzle/releases/download/v1.2/puzzle-0.1.0-py3-none-any.whl
```
4. Run the game: `puzzle`.
5. Enjoy the puzzle!
# Development
## Setup your dev environment
1. Install python >= 3.12
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
3. Now you can run tests and build the project like that:
```bash
uv venv #only once
uv run pytest
uv build
```
## Release a new version
```bash
git tag v<major>.<minor>
git push origin --tags

```