import warnings
from huggingface_hub import HfApi

# Suppress the DeprecationWarning for 'pipes'  # noqa: E402
warnings.filterwarnings("ignore", category=DeprecationWarning, module="fire.core")

import fire  # noqa: E402


class Discussions:
    def list(self, repo: str, show_all: bool = False):
        api = HfApi()
        discussions = api.get_repo_discussions(repo_id=repo, discussion_status=None if show_all else "open")
        for discussion in discussions:
            print(f"#{discussion.num} Title: {discussion.title}, Created At: {discussion.created_at}")

    def close(self, repo: str, num: int):
        api = HfApi()
        api.change_discussion_status(repo_id=repo, discussion_num=num, new_status="closed")
        print(f"Discussion {num} has been closed.")

class Tags:
    def list(self, repo: str):
        api = HfApi()
        refs = api.list_repo_refs(repo_id=repo)
        for ref in refs.tags:
            if ref.type == "tag":
                print(f"Tag: {ref.ref}, Commit: {ref.commit}")

    def create(self, repo: str, tag_name: str, commit: str):
        api = HfApi()
        api.create_tag(repo_id=repo, tag_name=tag_name, commit=commit)
        print(f"Tag {tag_name} created at commit {commit}.")

    def delete(self, repo: str, tag_name: str):
        api = HfApi()
        api.delete_tag(repo_id=repo, tag_name=tag_name)
        print(f"Tag {tag_name} has been deleted.")

class HFCLI:
    def __init__(self):
        self.tags = Tags()
        self.discussions = Discussions()

def main():
    fire.Fire(HFCLI())

if __name__ == "__main__":
    main()
