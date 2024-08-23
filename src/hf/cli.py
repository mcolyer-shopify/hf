import fire
from huggingface_hub import HfApi

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

class HFCLI:
    def __init__(self):
        self.discussions = Discussions()

def main():
    fire.Fire(HFCLI())

if __name__ == "__main__":
    main()
