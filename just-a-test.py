"""
AN ANONYMOUS (At least to normal network monitoring) COMMUNICATION APP USING GITHUB AS MESSAGE SYSTEM:

## VERSION 2.0
- ASSIGN A UUID4 TO THE USER
- CREATE (Deletes if it already exists) A FILE WITH THE USER ID AS NAME
- COMMITS THE FILE AND ENCODE (USERNAME: USER MESSAGE) AS B64 ON THE COMMIT MESSAGE
- PULL TO GET GIT HISTORY
- PUSH
- DECODE ALL COMMIT MESSAGES
- NEXT USER MESSAGE WILL BE JUST THE USER FILE DELETION
- CYCLE REPEATS

"""
import subprocess
import os
import uuid
import base64

from pathlib import Path

msg_board = Path(".\\MESSAGE-BOARD.md")

user = "ab65fe09-020e-4921-b8d7-33da7f821b96"
# user = uuid.uuid4()
upath = Path(f".\\{user}")

if not os.path.exists(upath):
    upath.touch(exist_ok=True)
else:
    os.remove(upath)

umsg = input("Write your message: ")
blob = f"{user}: {umsg}"
encoded_umsg = base64.b64encode(blob.encode("utf-8"))
b64_umsg = encoded_umsg.decode("utf-8")
print(b64_umsg)

subprocess.run(["git","add", upath])
subprocess.run(["git","commit","-m",f"{b64_umsg}"])

subprocess.run(["git","pull","origin","master"])
subprocess.run(["git","push","origin","master"])








