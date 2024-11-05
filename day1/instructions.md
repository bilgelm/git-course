# Day 1 hands-on exercise

This exercise gives a brief introduction to frequently used `git` commands.

1. If you haven't yet configured your user name and email with `git`, do it
using:

    ```shell
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```

1. Create a new directory and initialize it with `git` using:

    ```shell
    git init
    ```

1. Download the three Python files (`node.py`, `graph.py`, `main.py`) from this
directory to your computer and place them into your `git` repository.

1. Check the status of your repository:

    ```shell
    git status
    ```

1. Stage `node.py` and `graph.py` using

    ```shell
    git add node.py graph.py
    ```

    and recheck the status.

1. Make a commit using

    ```shell
    git commit -m "add node and graph implementations"
    ```

    and recheck the status.

    **Note:** most of the time, you will want to (and should) write a multi-line
    commit message, in which case the inline commit message option with the `-m`
    flag can be quite inconvenient. You can instead use `git commit` (i.e.,
    without the `-m` flag and the following message). This will bring up your
    text editor so you can type your multi-line message. After doing so, save
    and exit to finalize your commit.

1. View the log using

    ```shell
    git log
    ```

1. Now stage `main.py`, make a commit, check the status, and view the log.

1. Rename `main.py` to `example.py` and stage the change using

    ```shell
    git mv main.py example.py
    ```

    Then make a commit.

1. Open `example.py` in a text editor and add the following line at the top of
the file: `# this is a simple python example`. Save and close the file.

1. Check the git status. Display what has been changed in `example.py` using

    ```shell
    git diff example.py
    ```

1. Stage your changes and make a commit.

1. Using `git log`, find the hash of the commit where you first included
`main.py`.

1. Go back in time to inspect the commit identified in the previous step using
`git checkout`.

1. Now go forward in time to your latest commit.

1. Let's pretend that your last commit broke your code.
Revert (i.e., undo) your latest commit using `git revert`. See the
[documentation for `git revert`](https://git-scm.com/docs/git-revert.html)
to learn how to do this.

1. For the day 2 exercise, you will need to have a GitHub account.
[Create a GitHub account](https://github.com/) if you don't already have one.
