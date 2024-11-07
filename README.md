# Version control for data science with git

## Class content

In this course, students will learn what version control is, why it is
important, and how it can be used in data science projects.
Each day will begin with a lecture, followed by hands-on practice.
The first day will focus on the git distributed version control system.
Students will create a new git project, track changes to code, and recover from
simple mistakes.
The second day will focus on collaborating with others via GitHub.
Students will contribute to an existing project via pull requests.

This repository contains lab materials (i.e., the hands-on exercises) for this
class.
See the links below for details on each exercise.

[Day 1 exercise](day1/instructions.md)

[Day 2 exercise](day2/instructions.md)

## Class requirements

You will need to have
[git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
installed on your laptop for this class.
You will also need a plain text editor; we recommend
[VS Code](https://code.visualstudio.com/Download).
You can install both `git` and VS Code as user, without requiring admin
privileges.

Familiarity with Unix will be helpful, but not strictly required.

### `git`

The recommended way to install `git` is as described in the
[documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git),
which will require admin privileges (please contact IT for assistance).

You can alternatively install `git` without requiring admin privileges as
follows:

1. Install conda as user: see
[anaconda installation](https://docs.anaconda.com/anaconda/install/).
2. Install `git` using conda inside a new conda environment. To do this,
in Terminal or Anaconda Prompt, execute:

    ```shell
    conda create -n mygitenv git
    ```

3. Activate this environment by executing in Terminal or Anaconda Prompt:

    ```shell
    conda activate mygitenv
    ```

4. Test that you have `git`:

    ```shell
    git --version
    ```

### VS Code

It is highly recommended to install VS Code as user, as this will allow you to
update VS Code and install extensions yourself. (If you install it with admin
privileges, then you'll need admin privileges each time you need to update it
or install an extension.)

To install VS Code as user on Windows, follow
[these instructions](https://code.visualstudio.com/docs/setup/windows).
On MacOS, you simply need to drag and drop the downloaded application to a
user directory where you have write permissions (rather than the
`/Applications/` directory).

## Additional resources

### Using `git` via a web browser

- [Exercise - Try out Git](https://learn.microsoft.com/en-us/training/modules/intro-to-git/2-exercise-configure-git):
You can use `git` via a web browser; sign in using SSO to gain access to
Azure Cloud Shell for 2 hours
- [GIT Web Terminal](https://git-terminal.js.org/): web browser-based terminal
where you can test out `git` commands; not all `git` commands are supported
(e.g., `git init`)

### Microsoft Training

- [Intro to version control with Git](https://learn.microsoft.com/en-us/training/paths/intro-to-vc-git/)
- [GitHub Foundations](https://learn.microsoft.com/en-us/training/paths/github-foundations/)

### GitHub Education

- [git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)

### Git Commit Message Format Information

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary)
- [cbeams "How to Write a Good Commit Message"](https://cbea.ms/git-commit/)
