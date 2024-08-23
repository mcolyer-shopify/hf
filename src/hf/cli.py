import fire
from huggingface_hub import HfApi

class HFCLI:
    def discussions(self, repo: str):
        api = HfApi()
        discussions = api.list_discussions(repo_id=repo)
        for discussion in discussions:
            print(f"Title: {discussion.title}, Created At: {discussion.created_at}")

def main():
    fire.Fire(HFCLI)

if __name__ == "__main__":
    main()
