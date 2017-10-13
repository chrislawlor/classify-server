# Contributing

As an open source project, the Location Classifier Server welcomes
contributions of all kinds. Whether you are here looking to land your
first PR on github, or your a seasoned open source developer wanting to
get some experience with asyncio and aiohttp, or any other reason, be assured
that we can work together to make your contribution a success.

## Setting Up

Everything you need to set up your development environment is covered in 
the [Getting Started](https://github.com/chrislawlor/classify-server#getting-started) section of
the README.

## Code Standards

We mostly stick to [PEP-8](https://www.python.org/dev/peps/pep-0008/), but
with the maximum allowable line lenght increased to 99 characters.

For convenience, the developer requirements include Flake8, which you
can run with a quick `make check`.

## Pull Requests

For pull requests that have an existing issue in the tracker, please
reference the issue number in the pull request message.

If you're not familiar with the PR process, the basic steps are:

1. Fork the repository
1. Clone the fork to your machine
1. Create a new branch (`git checkout -b your-branch-name`)
1. Do some work, committing as you go.
1. Don't forget to add tests! We aim to always be increasing code coverage.
1. Run the test suite with `make test`
1. Optionally, but greatly preferred: When ready, squash to a single commit
   with `git rebase -i`
1. Push your branch to your fork with `git push -u origin your-branch-name`
1. Create a Pull Request using the Github user interface. The target branch
   should be `master`.



