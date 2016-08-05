I'm currently testing scenarios, so the nitty gritty bits are mocked out. The
code in `check_maintainer_review` and the tests are all that's important.

The script will vote on it's own flag called Maintainer-Review (to be setup).
As long as the flag has +1 or greater, it is good to be merged.

## How it works
* Some paths can be defined as explicitly needing review from the respective
  maintainers.
* A top-level architect review is an explicit +2 and overrides everything
  else.
* If a change touches files that do not have explicit owners defined, it will
  get a vote of +1.
* If the maintainer(s) for the paths that need maintainer ack have given a vote
  of +1 or higher, the script will vote +2.
* If the maintainer(s) for the paths that need maintainer ack have vote of +1
  or less, the script will vote -1.

## TODO
* Permission inheritance.
