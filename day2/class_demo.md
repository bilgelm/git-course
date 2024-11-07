# Notes on class demo

## Initial GitHub repository

### 1. Create a new public repository on GitHub with a README

:new:
[Instructions for creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

### 2. Edit `README.md` on GitHub and commit the change

:pencil:
[Instructions for editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)

### 3. Look at the commits on GitHub

:eyes:
[Instructions for navigating commits](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits)

### 4. Clone the repository to your laptop

We used `git clone <GitHub address for repo>` to copy the GitHub repository
to the local computer.

:arrow_down_small:
[Instructions for cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

[`clone` on Git Guides](https://github.com/git-guides/git-clone)

### 5. Inspect remotes

We used `git remote -v` to see the remote name and address.

:desert_island:
[`remote` on Git Guides](https://github.com/git-guides/git-remote)

### 6. Make a local change and push to GitHub

After making a change and committing it, we used `git push` to update the
repository on GitHub.

:arrow_up_small:
[`push` on Git Guides](https://github.com/git-guides/git-push)

## Create and resolve a *merge conflict*

User 1 made an edit to `README.md` online on GitHub.
User 2 made a different edit to `README.md` on their local copy.

User 2 then tried to `push` their edit, but got an error due to the conflicting content in `README.md`.

User 2 resolved this by `git pull --rebase`, manually fixing `README.md`,
followed by `git add README.md` and `git rebase --continue`,
which resulted in the creation of a new commit for the merge fix.

User 2 was then able to `git push`.

:crossed_swords:
[Instructions for resolving merge conflicts using the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)

## Ignoring files

There may be files in your project directory (such as data or large files) that
you don't want to track with git. You can tell git to ignore these files by
creating a `.gitignore` file in your project directory.
For example, if you want to ignore all files ending in `.gz` and the entire
subdirectory called `data`, your `.gitignore` file would look like:

```console
*.gz
data/

```

You should track the `.gitignore` file with git so that other users will also
make sure to exclude the content listed in `.gitignore`.

:no_good:
[Instructions for ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)

## Create a pull request

:technologist::earth_americas:
Read more about
[collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests).

### A. From a branch

This is what you would do if you have permissions to create new branches.

The `main` branch is intended to be a clean, working version of your code.
As you are working on developing new features or making changes to your code,
it is important to not break `main`. This is why you would create a new branch,
make your changes incrementally (i.e., small commits), then
finally bring those changes to `main` once everything is tested, stable, and
ready to be used by others.
(Some projects may have protections around the `main` branch,
preventing you from editing it directly.)

We created a new branch called `newfeature` in the local repository (on laptop),
made a commit, pushed to new branch on GitHub:

```shell
git checkout -b newfeature # this creates & switches to a new branch called newfeature
touch rocket.R # create an empty file called rocket.R
git add rocket.R
git commit -m "implement outerspace operations"
git push --set-upstream origin newfeature
```

Then, on GitHub, we created a pull request from the `newfeature` branch to
`main` using the button that appears in GitHub ("Compare & pull request" or
"Contribute"). Clicking this allowed us to enter a
message for our pull request. After creating the pull request, we went ahead and
approved it (normally, it would be someone else who approves the pull request,
after reviewing the changes).
After approving the merge, we got the suggestion to delete the `newfeature`
branch from GitHub, which we did by clicking the relevant button.

Next, returning to our local clone, we executed:

```shell
git checkout main # switch to main branch. You can also use "git switch main"
git pull # get the merged content from GitHub
git branch -d newfeature # delete newfeature branch now that it's been merged
```

Note that deleting a branch doesn't remove the content of the commits - it
simply removes the *pointer* (this is indeed the computer science/data
structures term) to the final commit in that branch.
The details are not needed to have a working knowledge of git branches, but if
you're interested, you can read more on
[git branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell).

### B. From a fork

If you don't have permissions to write to a GitHub repository, you'll need to
first create a fork (i.e., your own copy of the repository on GitHub).
Since this is now your own copy, you can edit it, and then create a pull request
to the upstream repository using the button that appears in your
fork on GitHub.

:fork_and_knife:
[Instructions for creating a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo?platform=mac&tool=webui)

:arrow_left:
[Instructions for creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

If you find any errors in this markdown file or would like to improve it,
please feel free to fork & create a pull request! :slightly_smiling_face:

## Miscellaneous

- [List of git graphical user interface (GUI) clients](https://git-scm.com/downloads/guis)
- [Using Git source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)
- Working with large files: git is intended for plain text files that are not
huge. Non-plain text files can still be tracked with git if they are not
expected to be updated (or will be only occasionally updated). If you want to do version control on non-plain text files or large files, you should check out
some git extensions such as [git-lfs](https://git-lfs.com/). For version control
on *datasets*, check out [datalad](https://www.datalad.org/).
