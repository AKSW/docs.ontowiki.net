---
title: Using-the-repository
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Using-the-repository/
---
 **This page is deprecated (we switched from Mercurial to Git in August 2011). But most ideas still apply. But we use git-flow to automatically manage this. Never push to the master branch. :)**

The idea of this wiki page is to clarify OntoWiki development process and especially the naming rules for branching and tagging. For general information about branching and tagging in mercurial, have a look at the following pages:

- [http://stevelosh.com/blog/2009/08/a-guide-to-branching-in-mercurial/](http://stevelosh.com/blog/2009/08/a-guide-to-branching-in-mercurial/)
- [http://hgbook.red-bean.com/read/managing-releases-and-branchy-development.html#id386031](http://hgbook.red-bean.com/read/managing-releases-and-branchy-development.html#id386031)

# Named Branches and Clones

We use mercurials **named branches** feature in order to organise different stages of the software development process. Since mercurial always uses a named branch with the name `default`, we reuse this branch as our latest un-stable development branch. Thus, new developers do not need to handle different branches and tags until they are more involved. In addition to named branches, **personal clones** can always be used to test around try something out without being afraid of demolishing the repository.

One important note about named branches: Once pushed to the central code repository, they are always visible and can't be deleted. Of course they can be close with `hg commit --close-branch` but since they are always in the history, the google code repository browser will always display them BTW, the code browser selects the branch by default, which has the latest committed revision.

## Release Branches

**Release Branches** are created in order to start the bug-fixing process of a soon release. A release branch is named after the release version number, for example `OntoWiki-0.9.5`. After creating a release branch, only bug fixes are committed to this branch. These fixes should be immediately merged with the `default` branch in order to make sure that the bug is fixed in the development version too. Please have a look on the example session for branching, fixing and merging ...

Release branch names correspond to the milestone labels in the issue tracker (issue label `Milestone-OntoWiki-0.9.5` -> release branch name `OntoWiki-0.9.5`). The prefix OntoWiki is needed since we plan to release parts of OntoWiki as stand-alone versions (e.g. Erfurt and RDFauthor).

**Note: After producing a release file, the release branch must be closed in order to avoid accidentally commits/pushes to this branch.**

## Feature Branches

Feature branches are needed to separate crazy new stuff developed by more than one person which is highly unstable thus there is a need to protect the main development branch `default`. If you want to mess around and make crazy new stuff with known side effects and **you are the only one** who is developing this, **please create a clone**.

Feature branches have a prefix `Feature-` followed by a more or less free name in camel case. This name should describe the feature as much as possible.

Examples for feature branch names are `Feature-EnhancedListManagement` or `Feature-AdvancedQueryCache`.

**Please talk to the maintainer before you create a new feature branch.**

# Tags

Tags are additionally used to label specific revision across over all branches. There are different categories of tags:

- **Release candidates** are tagged with the branch name plus a RCx suffix, e.g. `OntoWiki-0.9.5-RC1`. The tag name corresponds to the released files `OntoWiki-0.9.5-RC1.zip` and `OntoWiki-0.9.5-RC1.tar.bz2`.
- **Snapshot releases** are tagged with the project name followed by a date identifier, e.g. `OntoWiki-20100324`. The tag name corresponds to the released snapshot file `OntoWiki-20100324.zip`.

Note: Releases are not tagged since they can be access via the branch name.

# Example Sessions

Here is an example mercurial session of branching, fixing, merging and tagging. The first part is important only for maintainer while the second part is important for every developer who fixes some bugs in front of a new release

## Create a Release Branch
```
# make sure you are up-to-date and in the default branch
# Warning: You loose all your local uncommitted changes with -C
hg pull
hg update -C default

# Create a new release branch
# Warning: The branch is now activated and commits go to this branch
hg branch OntoWiki-0.9.5

# Commit the branch to the central repo
hg commit -m "new release branch OntoWiki-0.9.5"

# Push it
hg push
```

## Fix some bugs for a release and merge it with the dev-branch
```
# make sure you are up-to-date and in the release branch
hg pull
hg update -C OntoWiki-0.9.5

# ... fix some bugs and commit them to the release branch ...

# Switch back to the development branch
# Warning: You loose all your local uncommitted changes with -C
hg update -C default

# Merge the release branch fixes into the default branch
# Warning: You should be able to use a 3-way merging tool like meld or kdiff3 for this step
hg merge OntoWiki-0.9.5

# Commit this merge revision
hg commit -m "merge fixes from release branch OntoWiki-0.9.5"

# Push it
hg push
```

## Update to a specific version
```
# make sure you are up-to-date
hg pull

# update to a release candidate (e.g. for testing a reported bug)
# Warning: You loose all your local uncommitted changes with -C
hg update -C OntoWiki-0.9.5-RC1

# update to the latest revision for a release
# Warning: You loose all your local uncommitted changes with -C
hg update -C OntoWiki-0.9.5

# update to the latest development version
# Warning: You loose all your local uncommitted changes with -C
hg update -C default
```
