# AA236
Associated Files for AA236A CubeSat Design Project

## Setting up Git
You can download the latest version of Git for Mac or Linux [here](https://git-scm.com/downloads)
Windows CMD can be annoying to use if you are used to command line Linux. If you are using Windows, download Git from [here](https://gitforwindows.org/)
This comes with Git Bash, a terminal that I use, and recommend that you use too!
Now you need to tell Git which user you are.
`git config --global user.email "you@example.com"`
`git config --global user.name "Your Name"`

## Cloning the repository
Navigate to the directory on your local machine that you would like to store the documents.
For Mac and Linux, open a terminal here. For Windows, right click and select 'Git Bash here'
Clone the repository by
`sudo git clone https://github.com/Group3-SDR-cubesat/AA236.git`

## Housekeeping
When collaborating on projects, issues with merge conflicts can occur. This happens when one team member attempts to push an update from their local machine to the repository without having their local repository being previously up-to-date with the on-line repo.
To reduce the likelihood of this occurring, before working on your local repo, always pull the latest updates from the repo.
`sudo git pull`

## Pushing an update
Before updating your local repository, make sure you have pulled the latest updates.
To push your updates to the online repo, first stage them for commit.
`sudo git add --all`
Then commit the files, with a brief message as to what changes have been made.
`sudo git commit -m "This is my description of update"`
Finally, push the update
`sudo git push`

## Helpful commands
### Status
To view the status of the repository (what files have been added, staged for commit etc)
`git status`
### Branching
This will be more useful as we begin to develop software for the project.
Git repositories can have multiple branches. The master branch is best kept as the latest working version, while developments and bug-testing is best carried out on a separate branch
To create a new branch
`sudo git checkout -b my-branch master`
This creates a new branch called my-branch, based on the master branch. This only needs to be done once.
To switch between working branches use
`sudo git checkout next-branch`
Notice we dropped the -b flag and only specified the name of the branch we chose to switch to.
To merge branches (eg when we are happy with improvements in development branch and what to push them to the master branch)
Make sure you are in the master branch
`sudo git checkout master`
`sudo git merge dev`
This merges the changes made in the "dev" branch to the master branch