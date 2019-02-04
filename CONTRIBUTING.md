# Contributing Guidelines

Hello! If this is your first time contributing to Ralsei Bot, welcome! 
Thanks for considering to help the project!

If you're a returning contributor, welcome back! you're work is much appreciated.

***

Following these guidelines will enable the main developers to quickly integrate your new additions,
as they won't need to go through and add on to, edit, and fix code that isn't up to standard.

In return for this service you provide to them, they will return the favor by addressing your issue, 
considering your pull request, and helping you finalize your feature.

***
#### Contributions

Ralsei, as an open source Discord Bot, could use almost any contribution: New features, updated integrations, 
expanded documentation (Wiki and Site), as well as nearly anything else, such as tutorials or simple fixes like 
spelling mistakes

However, there are some restrictions. Firstly, if you are making an issue, check to make sure there are no any other 
issues addressing your problem. Secondly, please do not make an issue asking a support question. 
Instead ask support questions in #support of the [Ralsei Bot Discord](https://discord.gg/urSqehS)

***

#### Responsibilities

* Keep changes to be cross-platform without the need of end-user modification
* Ensure changes remain dynamic with the bot. Only modify the core bot files if you are adding core functionality.
* Use classes when needed, when they make sense, or to group underlying functionality pieces together.
    * If making a cog, keep the needed classes as subclasses within the cog class.
* Core functionality should be added within the main_ralsei.py file or as a module in the `core` directory.
    * When adding this kind of functionality, ensure that the main_ralsei file is updated to add the functionality.
    * Also note that core functionality will be extensively reviewed by the main developers
* Be welcoming to newcomers and encourage diverse new contributors from all backgrounds. 
See the [Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/) 
and the [Ralsei Code of Conduct](https://github.com/Infinidoge/Ralsei-Rewrite/blob/master/CODE_OF_CONDUCT.md) 
(adapted from the Contributor Covenant)

***

#### Your First Contribution

Unsure where to begin contributing? You can start by looking through the beginner and help-wanted issues
* [beginner (Good First Issue label)](https://github.com/Infinidoge/Ralsei-Rewrite/labels/good%20first%20issue)
  - Small changes, typically to already made cogs or utilities. Few lines, simple. Examples:
    - Adding a new stat generation method to the dnd cog
    - Improving upon a game in the games cog
    - Updating documentation within cogs
    - Adding a function to misc utils
* [help-wanted](https://github.com/Infinidoge/Ralsei-Rewrite/labels/help%20wanted)
  - Move involved than the beginner issues, typically more along the lines of adding commands to already made cogs
    - Adding a command to the random cog
    - Making a new game for the games cog
 
Working on your first Pull Request? You can learn how from this *free* series, 
[How to Contribute to an Open Source Project on GitHub.](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)
 
Some other good resources include http://makeapullrequest.com/ and http://www.firsttimersonly.com/
 
At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first 😸

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

***

#### Getting Started For Contributing

For something that is bigger than a one or two line fix:

1. Create your own fork of the code
2. Do the changes or add the features in your fork
3. If you like the change and think the project could use it, send a pull request with the changes.



Small contributions such as fixing spelling errors, can be submitted by a contributor as a patch, without a pull request

As a rule of thumb, changes are obvious fixes if they do not introduce any new functionality or creative thinking. As long as the change does not affect functionality, some likely examples include the following:

* Spelling / grammar fixes
* Typo correction, white space and formatting changes
* Comment clean up
* Bug fixes that change default return values or error codes stored in constants
* Adding logging messages or debugging output
* Changes to ‘metadata’ files like .gitignore, build scripts, etc.
* Moving source files from one directory or package to another

***

#### Code Style Guide

The code for Ralsei Bot has a pseudo-specific style.

As with most Python projects, all code must follow the style guide outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/)

Additionally, as you can see within all code files within the repository, all files and objects must have docstrings whenever possible/practical.
Such docstrings are formatted in a few different ways
* File docstrings for for files such as utils and cogs are formatted like this:
```python
"""
------------------------------
Ralsei [folder]/[file]
Written by Infinidoge
------------------------------
Description:
    [Description here]
------------------------------
Contributors:
    - [contributors here]
------------------------------
Misc Notes:
  - [Any notes go here]
"""
```
* Functions are formatted as per normal Python docstring format
* Cog classes are formatted like this:
```python
"""
Ralsei [folder]/[file]
------------------------------
Description:
    [Description]
------------------------------
Events:
  - [List of events]
------------------------------
Classes:
  - [Any classes within the cog class
"""
```

As a rule of thumb, follow the style of the other code files in the repository.

***

#### Reporting a Bug

###### Note: If you find a security vulnerability, do NOT open an issue. Email [security@doge-inc.net](mailto:security.doge-inc.net) instead.

When filing an issue, follow the respective template whenever possible, and provide as much information as possible.

Doing so will help maintainers get to your issue as quickly as possible, as well as ease the process of implementing or fixing the issue.

If there is not a template for what you wish to do, submit an issue without the use of a template and label it appropriately. 
Maintainers will get to your issue as soon as they can.

*** 

#### Requesting a Feature

When using this bot, it may strike you that some kind of functionality would be great if added.
You are probably, not alone in wanting a new feature.

Before requesting a feature, search through all enhancement issues to make sure it was not already requested. 
If it wasn't already requested, you may request the feature.

To request a feature, open an issue and follow the `enhancement` template, filling in as necessary.
This way it will be automatically tagged and put in the list for requested enhancements.

***

#### Labeling Issues

Every issue that is submitted should have some kind of label, unless a relevant label does not exist

Suggestions are labeled with `enhancement`, bug reports are labeled with `bug`, etc.

***

#### Code Review Process

The maintainers of the repository, mainly @Infinidoge, look at pull requests whenever possible, at least weekly.
After reviewing the repository, it will either be integrated, postponed, or closed.


A pull request will be postponed if a maintainer has a question, or needs something done with the PR before integration.


Additionally, a pull request will be closed with a response message if the functionality is already present, doesnt fit with the bot, or for any reason explained in the closing message.

***

#### Community

You can chat with the maintainers and other contributors over Discord.

The Ralsei Bot discord can be found [here](https://discord.gg/7UaaAze) (https://discord.gg/7UaaAze)

You can also send @Infinidoge a message using his discord tag: `Infinidoge#1337`