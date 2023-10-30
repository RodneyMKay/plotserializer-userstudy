# Workflow

We follow the [basic GitHub flow](https://guides.github.com/introduction/flow/) to propose and review changes.

The basic steps are:

1. You propose a change.
2. You **can** (don't always have to) ask a reviewer (your supervisor) to check whether the changes are sound
4. You merge your change and document it.

## Proposing Changes

Each change should be self-contained and result in a valid ontology when being merged back into `main`.
Trying to keep changes as small as possible and splitting larger additions over several commits can help to keep everything clear and understandable.

1. Make sure you have the latest version of the upstream code:

```bash
# Got back to the main branch
git checkout main
# Get new commits from the repository
git pull
```

2. Create an issue that contains a description of the problem you are working on and create a local branch that you will use to resolve the issue. You can choose an arbitrary name - using a prefix that matches the issue name will relate the branch to the issue, such as `26-plotting` for an issue with the issue number `26`.

```bash
git checkout -b 26-plotting
```

3. Make necessary changes in your working repository. Use `git status` to check changed files and `git diff` to inspect changes.

4. With `git add <filename>`, you can select files to commit. Use `git commit -m "<Short description of your change>"` to actually commit the added files. Phrasing request-like statements to the repository usually leads to a good commit description, like: "Add a property for locations". It is also a good idea to start the commit comment with the part of the repository that has been changed, like "docs", "base", or "modules/something". So a commit comment could look like this: "base: Add location property".

5. Push the changes to your fork of the repository:

```bash
# Make sure to add the branch name from step 2:
git push origin 26-plotting
```

6. Create a merge request by selecting your branch as the _compare branch_ and the `main` branch as the _base branch_. After submitting the merge request, you can already select a suitable reviewer from the menu on the right side. If your merge request cannot be merged directly, it may be outdated w.r.t to the current `main` branch. In that case, you need to [rebase your feature branch](#rebase-your-feature-branch).

7. If you want to start working on a new issue, make sure to return to the current main branch before, sync it with the current status of the remote and then create a new branch:

```bash
git checkout main
git pull
# Now you can create your next working branch
git checkout -b 27-more-plotting
```

## Reviewing Changes

If you want, you can assign your supervisor as a Reviewer to take a look at your changes and give you feedback to your code. You can discuss the changes directly on GitLab using comments either directly in the merge request or in the issue.

## Merge merge request

Once the reviewer has given you positive feedback or you are sure you want to merge the changes as they are, you can complete your merge request in the GitLab web interface.

After merging, you can delete the branch (there should be a button on the MR page where the Merge button was before).
It is safe to delete your branch, since all changes are now part of the `main` branch.


## Troubleshooting

Some general tips & tricks in case of problems when working with git.

### Advanced: Rebase Your Feature Branch

If GitLab shows that your merge request cannot be merged into the `main` branch, you usually made your changes based on an outdated version of the `main` branch, meaning somebody else merged their changes between your `git pull` and `git push`.
In that case, you can _rebase_ your current branch on top of the current main branch:

```bash
# Get the current changes from the main branch
git fetch origin/main
# Checkout the branch to rebase (replace 28-test-branch by your working branch)
git checkout 28-test-branch
# Start rebase in interactive mode
git rebase -i origin/main
# Force-push your changes to the updated branch (again: replace 28-test-branch with the actual name)
git push --force origin 28-test-branch
```

Rebasing tries to apply your changes commit by commit on top of the new `main` branch.
Conflicts may be resolved automatically, but that is not always possible.
The basic steps to resolve conflicts are the following:

- When the rebasing process stops, you can run `git status` to determine which files have issues and fix them locally.
- After fixing the conflicts in a file `git add filename` them.
- When all files are dealt with, and `git status` shows no more conflicts, run `git rebase --continue`.
- If you want to start over, you can cancel the rebase process by running `git rebase --abort`.

> **Note:** If you run `git push --force` after the rebase, the commits on GitLab will be overridden. That means that **old review comments** may be lost during the process, if they are attached to changes in these commits (which is usually the case as all commits are modified during a rebase).

