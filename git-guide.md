git commands:

status:
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
- git status

clone:
  - Clone a repository into a new directory
  - git clone git@github.com:WSU-kduncan/ceg3120-pattonsgirl.git

add:
  - add file contents to the index (add file to those to be committed in git commit)
  - git add filename.txt
  - git add * (add all, potentially dangerous)

rm:
  - Remove files from the working tree and from the index (Easier to remember as roughly being reverse git add)
  - git remove filename.txt

commit:
  - Create a new commit containing the current contents of the index and the given logmessage describing the changes. In other words, commit the added changes for the branch.
  - git commit -m "commit message"  (my preferred way to commit)

push:
  - Update remote refs along with associated objects. Simply put, push local branch changes to the remote branch.
  - git push

fetch:
  - Download objects and refs from another repository. In other words, fetch the contents of remote to the local repository (not working directory). Fetch but do not merge.
  - git fetch

merge:
  - Join two or more development histories together. AKA merge two or more branches' contents.
  - git merge other-branch

pull:
  - Fetch from AND INTEGRATE with another repository or a local branch. Fetch and merge the remote repository locally.
  - git pull

branch:
  - list (with no flags), create (by specifying a new branch name), or delete branches
  - git branch (for listing branches)

checkout:
  - Switch branches or restores working tree files
  - git switch other-branch



.git folder:
  - A folder in git repositories that holds files and folders for branches, config, etc.

.gitignore:
  - A file that holds the names of all the files to be ignored by the git additions and commits. git add and commit will ignore any files with their names in .gitignore.



Pull requests:
  - Pull requests are submissions of a branch to a GitHub repository. They can be set up so the changes need to be reviewed by someone else before being merged with the main branch.

SSH authentication to repositories:
  - A SSH public key can be uploaded to a GitHub account which allows the corresponding private key to be used to establish a connection between the remote repository and the local one. The local device can then pull repositories off of GitHub and alter them and submit changes to the remote repositories.
