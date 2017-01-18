#!/usr/bin/python

from argparse import ArgumentParser
import os
import subprocess

REPOSITORY_DB_FILE = '/etc/apt-git.repo'

def parse_args():
    parser = ArgumentParser(
        description="Package manager for git cloned repos."
    )
    subparsers = parser.add_subparsers(title='commands',
        description="Commands to execute on script",
        dest='action')

    update_sp = subparsers.add_parser('update',
        help="Update (git pull) cached repositories"
    )

    install_sp = subparsers.add_parser('install',
        help="Install (git clone) the target repositories (format: autor/repo)"
    )
    install_sp.add_argument('add_repos', nargs='+', type=str)

    search_sp = subparsers.add_parser('search',
        help="Search on github, gitlab and bitbucket for the the input string"
    )
    search_sp.add_argument('search_query', nargs=1, type=str)

    remove_sp = subparsers.add_parser('remove',
        help="Remove the target repositories"
    )
    remove_sp.add_argument('remove_repos', nargs='+', type=str)

    return parser.parse_args()


def update():
    cwd = os.getcwd()
    with open(REPOSITORY_DB_FILE, 'r') as db:
        for line in db:
            line = line.strip()
            if line:
                print '[*] Updating %s...' % line
                os.chdir(os.path.join('/opt', line))
                proc = subprocess.Popen(['git','pull'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                print proc.stdout.read()
                print proc.stderr.read()

    os.chdir(cwd)
    print '[*] Update completed!'

def install(repos):
    pass

def search(query):
    pass

def remove(repos):
    pass

def main():
    args = parse_args()
    if args.action == 'update':
        update()
    elif args.action == 'install':
        install(args.add_repos)
    elif args.action == 'search':
        search(args.search_query)
    elif args.remove == 'remove':
        remove(args.remove_repos)

if __name__ == '__main__':
    main()
