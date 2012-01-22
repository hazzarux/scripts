#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
-- github_issues_checker.py --
Created on Sun Jan 22 18:44:04 2012

@licence: GNU GPL v3+
@author: Yigit Ozkan < yigitozkan2804@gmail.com >
"""

'''
looks up all OWN repositories of a certain user & returns the issues if they got any
'''

from github2.client import Github


USERNAME = "hazzarux"


def main():
  github = Github() #create the object
  all_repos = github.repos.list(USERNAME)
  for repo in all_repos:
    if repo.fork == False:
      issues = github.issues.list(USERNAME+"/"+repo.name, state="open")
      if len(issues)<>0:
        for issue in issues:
          print repo.name
          print "       #"+str(issue.number)+" | "+issue.title
  print "---------------------done---------------------"

if __name__ == '__main__':
  main()
