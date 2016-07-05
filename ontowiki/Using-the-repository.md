---
title: Using-the-repository
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Using-the-repository/
---

# Branches

The `develop` branch is the core branch from where all features should be created. To ensure a clean and working develop branch all features need to be created in other branches/forks. **Never push onto develop**

So if you want to create your own extension or correct an error you need to pull the newest develop and then create a new branch/fork the branch which is either named `feature/MyCoolFeature` or `fix/FileorThingToFix`.

Afterwards you should (squash) and rebase your branch/fork back to the **actual** develop branch. Then you can make a pull request and the AKSW Team will look over your pull request. **Test your extension with phpunit and codesniffer before you rebase and create the pull request**

# Example 

## Pull develop and create new branch
```
# Clone/Pull OntoWiki
$ git clone https://www.github.com/AKSW/OntoWiki or $ git pull

# make changes and make a new commit
$ git add changed.file
$ git commit -m 'this is a feature branch to do something'

# push into new branch
$ git checkout -b feature/CoolFeature
$ git push origin feature/CoolFeature

```

## Rebasing
```
# while you are in your branch and are done with everything
$ git rebase [-i] develop

# or if you in a fork add https://www.github.com/AKSW/OntoWiki as upstream and then
$ git rebase [-i] upstreamname develop 

# then follow the instructions and squash the commits and rewrite the merge git commit 
# into a usefull explanation what your branch did.
```
