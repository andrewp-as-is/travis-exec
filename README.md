[![](https://img.shields.io/pypi/v/travis-exec.svg?maxAge=3600)](https://pypi.org/project/travis-exec/)
[![](https://img.shields.io/npm/v/travis-exec.svg?maxAge=3600)](https://www.npmjs.com/package/travis-exec)
[![Travis](https://api.travis-ci.org/looking-for-a-job/travis-exec.svg?branch=master)](https://travis-ci.org/looking-for-a-job/travis-exec/)

<b>execute command for every travis repo</b>

#### Install
```bash
$ [sudo] npm i -g travis-exec
```
```bash
$ [sudo] pip install travis-exec
```

#### Features
+   `{}` replaced with repo name

#### CLI
```bash
usage: travis-exec args ...
```

#### Examples
```bash
$ travis-exec travis status -r {}
$ travis-exec python -m travis_cron.add {} master daily no
$ travis-exec python -m travis_env.set {} WEBHOOK_URL "$WEBHOOK_URL"
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>