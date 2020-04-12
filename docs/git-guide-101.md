# Git Guide 101
***
## Commit
The "commit" command is used to save your changes to the local repository.
***

### Initialized a repository

```commandline
git init
```

### Add a file to the staging area

```commandline
git add --all

```

### Commiting files
```commandline
git commit -m "message"
git commit -am "message with adding file to the staging area "
```
### Repository log
```commandline
git log
```
### Repository status
```commandline
git status 
```

### Unstaging files
``` sh
git reset --hard


git diff <1stVer commit hash> <LastVer commit hash> ::	difference btw changes made 

```
## Branch
In Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes. This makes it harder for unstable code to get merged into the main code base, and it gives you the chance to clean up your future's history before merging it into the main branch.
***



### Create a branch
```commandline
git branch <branch-name>
git checkout -b <branch-name>
```
### Merging a branch
```commandline
git merge <source-branch-name>
```
### Listing branches 
```commandline
git branch 
git brach --list
```
### Removing a branch

##### Remotly
```commandline
git push origin --delete <branch-name>
```

##### Locally
```commandline
git branch -d <branch-name>
```


### Create a tag
```commandline
git tag <tag-name>
```
### Replace a tag
```commandline
git tag -f <new-tag-name>
```
### Listing tags
```commandline
git tag -l
git tag
```
### Removing a tag
```commandline
git tag -d <tag-name>
```

## Fixing Common issues
***

### 
```commandline
git log --oneline
```

### Ammend wiht previous commits
```commandline

git status
git add --all
git commit ammend
git log --oneline
```
!!! warning "Be carefull!"
    When you `ammend` a commit, this will remove the tag from the commit if it has already

### Add tag to the latest ammend
```commandline
git tag
git log --online
git tag -f <update-tag>
```


### Show all changes
```commandline
git reflog

```
### Checkout differert state in the repository
```commandline
git reset HEAD@{5}
```
`Changes sitting there`

#### older version of this file
```commandline
git reset --hard


or

git reset HEAD@{3} --hard
```

### Reset Back to previous commits. 
```commandline
git log --oneline
git reset HEAD~2 --hard

```

### Last Commit gone but changes sitting there
```commandline
git reset HEAD~ --soft
```
### Stash -- file no need to put into stage
```commandline
git stash
```
### Taking stash file to the staging folder
```commandline
git stash pop
git add --all
git commit -m "<message>"
```




### Switch between branches A/B B/A 
```commandline
git checkout <branch-name> 

``` 


## Adding and Pushing an existing repository
***
```
git remote add origin <link-to-github-repo>
```

```commandline
git remote add origin https://github.com/mohsinmdl/GTIN-Prediction-System.git
git push -u origin master

```


## List your existing remotes

```
$ git remote -v
```


## Change a remote Git repository

```
git remote set-url origin git@your.git.repo.example.com:user/repository2.git
```


```
You can check the configs of your repository by :

git config -l
which contains your remote repository url.

Also, you can use the following command :

git remote -v

```

## Adding submodule to git repo
```
git submodule add https://github.com/mohsinmdl/mohsinmdl.github.io.git site
```

## Update Git submodule to latest commit on origin
```
git submodule update --remote --merge
```

## Remving git from directory
```
rm -rf .git
```

## Error
Git refusing to merge unrelated histories 

!!! failure
    git  pull origin master
    From https://github.com/mohsinmdl/mdl-portfolio
    * branch            master     -> FETCH_HEAD
    fatal: refusing to merge unrelated histories

!!! failure
    There is no tracking information for the current branch.
    Please specify which branch you want to merge with.
    See git-pull(1) for details.

### solution

```
git pull origin branchname --allow-unrelated-histories
```

```
git --work-tree="." pull --allow-unrelated-histories
```

```
git branch --set-upstream-to=origin/master

```


## Save VSCODE Git Credentials
If you wanna save your git password in VSCode, below is the command for that purpose --
```
git config --global credential.helper store

```


!!! failure
    git submodule add https://github.com/mohsinmdl/blogs-deploy public
    'public' already exists in the index


```
git ls-files
```

```
git rm --cached <DIR>
```

```
git rm -f --cached <DIR>
```

Error
!!! failure
    fatal: Please stage your changes to .gitmodules or stash them to proceed

```
git rm --cached .gitmodules
```


### Remove module from .git folder

ls -a
cd .git
cd modules/
rm -rf mdl-docs/

***

### Git Pull with Submodule
For a repo with submodules, we can pull all submodules using
git submodule update --init --recursive

for the first time. All submodules will be pulled down locally.
To update submodules, we can use
```
git submodule update --recursive --remote
```

or simply
```
git pull --recurse-submodules
```
***

## Pushing all submodules recursively

git1.7.11 ([ANNOUNCE] Git 1.7.11.rc1) mentions:
>"git push --recurse-submodules" learned to optionally look into the histories of submodules >bound to the superproject and push them out.
So you can use:

```
git push --recurse-submodules=on-demand
```
