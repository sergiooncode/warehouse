# Contributing

When contributing to this repository, please discuss the change to be added with one of the owners
before making the change.

Please note we have some Guidelines to follow when contributing, please follow them.

# Guidelines

* [Pull Request Workflow](#pull-request-workflow)
  * [Step 1: Branch](#step-1-branch)
  * [Step 2: Tests](#step-2-tests)
  * [Step 3: Code](#step-3-code)
  * [Step 4: Commit](#step-4-commit)
  * [Step 5: More Tests](#step-5-more-tests)
  * [Step 6: Rebase and Squash](#step-6-rebase-and-squash)
  * [Step 7: Push](#step-7-push)
  * [Step 8: Open Pull Request](#step-8-open-pull-request)
  * [Step 9: Discuss and Update](#step-9-discuss-and-update)
  * [Step 10: Squash and Merge](#step-10-merge)
* [Style Guides](#style-guides)
  * [Py6thon Style Guide](#python-style-guide)
  * [Comment Guidelines](#comment-guidelines)
* [Code Review](#code-review)
  * [Purpose of Code Review](#purpose-of-code-review)
  * [Code Review Guidelines](#code-review-guidelines)
* [Testing](#testing)

## Pull Request Workflow

### Step 1: Branch

Work from local branches based on the latest master branch:

```bash
$ git checkout master
$ git fetch && git merge origin/master
$ git checkout -b WAREHOUSE-1234-fix-inventory-bug -t upstream/master
```

#### Branch Name Conventions

* Prefix all branches with a JIRA ticket identifier (e.g. `WAREHOUSE-xxxx`)
* Succinctly describe the branch's purpose (max 72 characters)
* Separate words with dashes (`add-feature` not `add_feature`)
* Use the present tense (`add-feature` not `added-feature`)
* Use the imperative mood (`add-feature` not `adds-feature`)

Good branch names:

* `WAREHOUSE--1234-fix-inventory-update-error`
* `WAREHOUSE--4567-add-validation-when-loading`
* `OPS-3679-use-graylog-as-production-logger`

Bad branch names:

* `1234-adding-new-product-page-feature`
* `bugfix`

### Step 2: Code

It's a good idea to run the test suite and the [linter](#using-linter) frequently. Also,
make sure you follow the relevant [style guides](#style-guides).

### Step 3: Commit

Ensure git is configured to use your name and email address

  This can be done per repository with these commands

  ```
  $ git config user.name "Sergio Perez"
  $ git config user.email "sperez4mba@gmail.com"
  ```

  You can configure this globally (for all repositories) by using the `--global` flag for `git config`.

#### Commit Message Guidelines

* Never use the `-m <msg>` or `--message=<msg>` flags for `git commit`

  This format encourages you to cram your commit message into your terminal input line. It is difficult to edit
  or format long commit messages within a single terminal line.

* Describe _what_ was changed and _why_ the change was necessary

  The purpose of git commit messages is for future engineers to review your changes and
  understand why they were made. Resist the urge to simply say "resolves WAREHOUSE-1234",
  which forces a developer to look up an old ticket (and hope the ticket has enough
  detail about the issue).

  If you cannot say why you're making a particular change, then you should not make that change.

* The first line of a commit should
  * contain a short description of the change
  * be 50 characters or less
  * begin with a capitalized, imperative word (e.g. "Add", "Fix")
  * not end with a period

* Keep the second line blank

  This is important for using `git log --oneline` and `git shortlog`.

* The third line should be a link to the ticket

  This _can_ be ignored if a change does not have a ticket. However, as a general rule,
  all changes should have an associated JIRA ticket.

  _Why is this useful? The branch name contains the ticket identifier!_

  It is very difficult to identify the branch a commit was written for. Including the
  ticket URL allows developers to simply click a link while exploring the `git blame`
  output for a file. This is very helpful for debugging.

* Wrap all other lines at 72 characters


Example adapted from [Tim Pope's excellent note](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
on commit messages:

```
Capitalized, short (50 chars or less) summary

https://warehouse.atlassian.net/browse/WAREHOUSE-xxxx

More detailed explanatory text, if necessary.  Wrap it to about 72
characters or so.  In some contexts, the first line is treated as the
subject of an email and the rest of the text as the body.  The blank
line separating the summary from the body is critical (unless you omit
the body entirely); tools like rebase can get confused if you run the
two together.

Write your commit message in the imperative: "Fix bug" and not "Fixed bug"
or "Fixes bug."  This convention matches up with commit messages generated
by commands like git merge and git revert.

Further paragraphs come after blank lines.

- Bullet points are okay, too

- Typically a hyphen or asterisk is used for the bullet, followed by a
  single space, with blank lines in between, but conventions vary here

- Use a hanging indent
```

Other helpful resources:

* [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
* [5 Useful Tips For A Better Commit Message](https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message)

### Step 5: More Tests

Once you're done writing code, ensure that you have sufficient unit test coverage.
Run your tests one last time to ensure your code is ready.

### Step 6: Rebase and Squash

As a best practice, once your changes are ready, you should use `git rebase`
(not `git merge`) to synchronize your work with the main repository. This ensures your
branch is up to date (and that we avoid merge conflicts) while the git history remains clean.

```bash
$ git fetch upstream
$ git rebase upstream master
```

### Step 7: Push

Once you are sure your commits ready to go, with passing tests and linting, begin
the process of opening Pull Request by pushing your working branch to GitHub.

```bash
$ git push origin my-branch
```

**Pro-tip** you can configure `git push` to push the current branch by default:

```bash
$ git config --global push.default "current"
```

### Step 8: Open Pull Request

Open a pull request from within GitHub. You will be presented with a template that should be filled out.

### Step 9: Discuss and Update

Once the pull request is ready, assign a code reviewer. You (the patch author) and the reviewer
should comply with the [code review guidelines](#code-review).

To make changes in response to feedback from your code reviewers, simply commit your changes
locally and push. Remember to keep your changes squashed to a single logical commit! The `--amend` flag
to `git commit` is useful for this purpose:

```bash
$ git add my/changed/files
$ git commit --amend
$ git push --force-with-lease origin my-branch
```

You should also frequently synchronize your changes with `master` by rebasing:

```bash
$ git checkout my-branch
$ git fetch --all
$ git rebase origin/master
$ git push --force-with-lease origin my-branch
```

Note that you should avoid the `--force` flag. The `--force-with-lease` is safer because it prevents you
from overwriting other people's changes to a branch.

### Step 10: Squash and Merge

Once your changes are approved by a reviewer, you're ready to merge! If you have merge conflicts,
**do not use GitHub's merge conflict resolution tool**. Instead, simply rebase your changes onto the
`master` branch. You can fix your merge conflicts during the rebase.

Once your branch is up to date, you should ensure that you squash your changes into logical commits.

During development, it's common to treat commits like savepoints that you can roll back. If you have to update
3 separate pages in order to add a new field, you might update each of those pages in a unique commit.

Your final branch history, however, should have as few logically independent commits as possible. This
keeps the history usable, since logical changes are grouped together.

See these guides to learn how to reorder and squash commits:

*  [Reorder Commits with Rebase](http://gitready.com/advanced/2009/03/20/reorder-commits-with-rebase.html)
*  [Squashing Commits with Rebase](http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html)


## Style Guides

### Python Style Guide

- WIP

- 

#### Using linter

Use the linter (we're using `flake8`) to check your Python changes.

To run the linter over the project:
```bash
$ flake8 --config=setup.cfg --max-complexity=12 <files_to_lint>
```

### Comment Guidelines
* Code should be self documenting.
* Comments summarizing what code does should be in function docstrings.
* Inline comments should only be used to tell you something the code cannot. The code itself
says _what_ and _how_. Comments say _why_.
* `TODO` comments are encouraged, but assign them to a person:

  ```python
  # TODO(personname): use quicksort instead of mergesort
  ```

## Code Review

All code must be reviewed and approved before it can be committed to master. This is enforced by
GitHub's protected branch feature, even for admins of the repository.

In fact, it is recommended that you read as many PRs as you can, even if you are not assigned as a
reviewer. This will help you stay on top of incoming changes to the codebase. If you find a bit of code difficult
to read/understand, say something! The only way we grow as developers and improve our codebase is by giving each
other this kind of feedback.

### Purpose of Code Review

#### Enabling the patch author to succeed

Code review is a guardrail that helps ensure the continuous improvement of the codebase. The reveiwer's
responsibility is to help the patch author succeed in improving the codebase.

#### Evaluating the design of code

Code review is an opportunity to ensure all code committed to the codebase follows best practices
regarding the design of programs. The code reviewer should ensure committed code is readable, maintainable,
extensible, and reusable.

#### Sharing knowledge

Code review is an opportunity for the reviewer to share their knowledge with the patch author. Did they
re-create a utility method that already exists elsewhere in the codebase? Could some code be simplified using
cool utilities from `collections` or `itertools`? Help the patch author learn!

Similarly, code review is an opportunity for the reviewer to learn what has changed recently in a codebase.
If a commit moves a package from one location to another, or deprecates a feature, they may avoid being
caught by surprise.

#### Finding defects

The primary frontline against defects is automated testing. In code review, finding defects is an important,
but secondary concern.

Some reviewers skip over unit tests. On the contrary, reviewing the unit tests to ensure they are thorough
(cover all use cases) and effective is the best way to ensure the rest of the code is free of defects.

### Code Review Guidelines

#### Keep patches small

Code review becomes ineffective after ~400 lines. Keep patches small and break large changes up into separate
tickets / pull requests.

#### Review immediately, but take your time

As a rule of thumb, 500 lines of code takes an hour to review. We're all busy people, but there's no point
in reviewing code if you rubber stamp it.

Don't keep the patch author waiting though. We all benefit from submitting small, frequent iterations to the
codebase. Please review any code assigned to you within 24 hours.

#### Review frequently, and in short bursts

Don't review code for more than 60 minutes at a time or you'll fatigue yourself. A fatigued reviewer misses
design issues and defects.

#### Follow the pull request template

The template exists to make the reviewer's job easier. Ensure all the required boxes are checked before
approving a change. Be conscientious of when exceptions should be made (e.g. docs changes don't need unit tests).

#### Take long discussions to Slack or a video chat

GitHub's PR comment system is decent, but not suitable to long discussions about style, design, etc. If you find
that a conversation is growing too long for GitHub's interface to be useful, or if you want to include more people,
then take the conversation to Slack or a video call where it is easier to engage each other's ideas.

#### Be aware of the person behind the code

Everyone has the right to submit code. Don't nitpick code over personal preferences. Request changes only when
code does not follow best practices or adhere to the style guidelines.

Also, be aware that _how_ you communicate requests and reviews in your feedback can have a significant impact
on the success of the pull request. We recommend giving feedback in the form of a question. For instance:

  > Should we replace these conditional statements with polymorphism?

Comes across as more amicable and suggestive than a command:

  > Replace these conditional statements with polymorphism.

Which is still better than an aggressive response:

  > This is a bad idea. Replace this conditional with polymorphism.

## Testing

All code needs to be tested. Automated testing is critical to validate code functions correctly, but
also to guard against regressions due to future changes.
