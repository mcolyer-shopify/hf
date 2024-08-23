# hf

A CLI tool to list discussions on a Hugging Face repo.

Today it only supports listing and closing discussions, maybe one day it will
do more.

## Usage

```bash
HF_TOKEN=your_token_here
uv run hf discussions list org/repo
uv run hf discussions close org/repo #123
```
