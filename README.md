# ⚡️Apply⚡️

## Usage

Apply to jobs on the PEY portal using the job id, the company name, and the position.

YOU NEED TO EDIT THE LATEX CONFIGURATION IN `work.py` 🙈

```shell
$ git clone https://github.com/anonymouspey/apply.git
$ cd apply
$ echo 'username = "YOUR USERNAME"' >> peyconfig.py
$ echo 'password = "YOUR PASSWORD"' >> peyconfig.py
$ echo 'name = "FIRSTNAME LASTNAME"' >> peyconfig.py
$ pip install -r requirements.txt
$ # make sure u have chromedriver installed/on your path
$ # `brew install chromedriver` if on mac
$ python apply.py JOB_ID "COMPANY_NAME" "POSITION" "TEAM"
```

The `TEAM` argument can be ommitted, and it defaults to "Engineering".

## Warning

* this has only been tested on macos.
* idk if this is legal.
  * If so, use it
  * If not, this was made purely because I was bored and i do not intend to use it.

## Requirements

* Python 2.7+ (only tested on 3, since 2 is deprecated 🖕).

* pdflatex

* the stuff in `requirements.txt` 

## Todo

- [ ] only apply using job id.
