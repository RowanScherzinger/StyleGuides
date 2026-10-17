# CLAUDE.md

This repo is a collection of style guides, one per top-level folder. There is nothing to
build, run or test at the root. Each guide has its own `CLAUDE.md`: read it before working
in that guide.

## Public repo

This repository is public on GitHub. Never commit personal data:

- No absolute local paths (drive letters, user home directories), usernames or emails.
- No real hostnames, IP addresses, network shares or credentials. Use placeholders such as
  `node-01` in examples.
- Refer to consuming apps by name only, not by where they live on disk.

Scan staged changes before every commit, for example:
`git diff --cached | grep -niE "[a-z]:[\\\\/]|users[\\\\/]|192\.168|@gmail|password"`.

## Structure

New guides copy the layout described in `README.md` and get a row in its table.
