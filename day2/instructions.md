# Day 2 hands-on exercise

When you logged into your laptop this morning, you found a new file,
`message.txt`, on your Desktop. You certainly did not create this file, and its
contents don't seem to make sense: just a bunch of numbers. It does indeed
look like a mysterious message... from your laptop?

After some contemplation, you think each number might be an
[ASCII](https://en.wikipedia.org/wiki/ASCII) code.
You asked a friend to write an R script to decode the message.
Your friend loves using `git`, so they put their code in a `git` repository and
shared it with you via an online `git`-based collaboration platform (GitHub).
Being in a hurry, your friend couldn't test the code and is currently without
internet access, unavailable to help you.
You see that there are three simple typos in the R script that need to be fixed,
so you decide to tackle this yourself.
Then you realize that your friend gave you read-only access to this repository,
so you cannot modify the content directly. That's okay, you say, because you can
still create your own copy of the repository and make edits that way.

Your tasks in this exercise are to:

1. [Create a GitHub account](https://github.com/) if you don't already have one.
1. Fork your friend's repository (we will pretend for the sake of this exercise
that it is this repository, `intro-to-git-2024-11.git`).
1. Clone your fork to your laptop.

   [Optional bonus step: create a new branch called `bugfix` and make your edits
   there rather than on the `main` branch]

1. Edit `decode_message.R` to fix the three typos.
1. Make a `git commit` with your edits.
1. `push` to your fork on GitHub.
1. Create a pull request to the upstream
repository (i.e., your friend's original repository) from your fork, so that
your friend's repository can also be updated with your fixes.
