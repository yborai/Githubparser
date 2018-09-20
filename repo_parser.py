import requests
#import json
import sys

def main():
    user_name = input("Enter the Github user you would like to know about: ")
    repos = get_repos(user_name)

    for repo in repos:
        print('Repo: ' + repo + ' | Number of commits: ' + str(get_commit_count(user_name, repo)))

def get_repos(name):  #returns a list of all repos for a given user(defined by name)
    repo_request = requests.get("https://api.github.com/users/" + name + "/repos")
    raw_repos = repo_request.json()
    repos = []

    try:
        for repo in raw_repos:
            repos.append(repo['name'])
    except:
        print('Invalid username!')
        sys.exit(1)

    return repos

def get_commit_count(name, repo):   #returns the number of commits for a given repo
    commit_request = requests.get('https://api.github.com/repos/' + name + '/' + repo + '/commits')
    commits = commit_request.json()

    return(len(commits))

if __name__ == '__main__':
    main()
