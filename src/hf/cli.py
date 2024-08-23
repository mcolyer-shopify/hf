import fire
from huggingface_hub import HfApi

class HFCLI:
    def discussions(self, repo: str, show_all: bool = False):
        api = HfApi()
        discussions = api.get_repo_discussions(repo_id=repo, discussion_status=None if show_all else "open")
        for discussion in discussions:
            print(f"#{discussion.num} Title: {discussion.title}, Created At: {discussion.created_at}")

def main():
    fire.Fire(HFCLI)

if __name__ == "__main__":
    main()
