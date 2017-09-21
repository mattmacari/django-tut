# Omaha Python - Django Tutorial Part 1

_Data Given: 09/19/2017_

## Git Background

* Use `git init` to create an empty repo.
* Use `git clone` to clone a remote repo.
  * Reference: [git-clone](https://git-scm.com/docs/git-clone)
  * In parent directory, use `git clone https://github.com/mattmacari/django-tut.git`
  * Open repos don't require authentication or authorization
* To add a remote origin, use `git remote`.
  * (git-remote)[https://git-scm.com/docs/git-remote]
  * `git remote add origin https://github.com/mattmacari/hubot.git`

* First commit, let's modify the README.md.

## Virtual Environments

* Use cases for Virtual envs:
  * Ensure code dependencies don't change between apps
  * Create isolated environments that can be deployed on multiple machines.
  * Better practice than using the root python install.
* To create a virtualenv using `virtualenv` run `virtualenv ./{env_name}`
  * For example, `virtualenv ./django-tut`
* Using conda use, `conda create -n django-tut`

## Django Setup

* Run django setup (already did).
  * Use command `django-admin startproject mysite`
* Verify app works using `python manage.py runserver`
* Start an app 'chess'
* Refactor settings module
* talk about settings
* Create first model
* Create objects in database
* Wire up first view
* write tests
  * Write basic test for view
* setup admin site
* create some additional pieces
* create a list view

## Setup django-bootstrap
* http://django-bootstrap3.readthedocs.io/en/latest/installation.html

### References
* [GitHub](https://github.com/)
* [Git SCM Docs](https://git-scm.com/docs)
