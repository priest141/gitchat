from git import Repo
import base64

repo = Repo(".\\.git")

for commit in repo.iter_commits(max_count=50):
    msg = commit.message
    decoded_msg = base64.b64decode(msg)
    print(decoded_msg)