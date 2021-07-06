# explainsh

`explainsh` is a command line interface for https://explainshell.com.

This tool is perfect for those who work most of the time with a terminal and have doubts about some commands. Instead of opening the browser, going to https://explainshell.com and pasting the command, `explainsh` does the same but from the terminal.

## Running `explainsh`

```console
$ git clone https://github.com/7Rocky/explainsh
$ cd explainsh/
$ chmod +x explainsh.py
```

Now, you can use either `python3 explainsh.py` or `./explainsh.py` to execute the tool.

Additionally, you can rename the script to simply `explainsh` and move it to a directory in your `PATH` environment variable, so that `explainsh` is available as a command at every working directory.

## Usage of `explainsh`

As easy as using https://explainshell.com:

```console
$ explainsh <command>
```

However, if the `<command>` contains special characters, it needs to be wrapped between single quotes.

And if the `<command>` contains single quotes, then each single quote must be escaped (`\'`) or duplicated (`''`).

To see some examples, type:

```console
$ explainsh

Usage: explainsh <command>

Wrap <command> between single quotes if it contains
special characters: ! " # $ & ' ( ) * ; < > ? [ \ ] ` { | } ~

Examples:

       explainsh ':(){ :|:& };:'
       explainsh 'for user in $(cut -f1 -d: /etc/passwd); do crontab -u $user -l 2>/dev/null; done'
       explainsh 'file=$(echo `basename "$file"`)'
       explainsh 'true && { echo success; } || { echo failed; }'
       explainsh 'cut -d '' '' -f 1 /var/log/apache2/access_logs | uniq -c | sort -n'
       explainsh 'tar zcf - some-dir | ssh some-server "cd /; tar xvzf -"'
       explainsh tar xzvf archive.tar.gz
       explainsh find . -type f -print0
       explainsh ssh -i keyfile -f -N -L 1234:www.google.com:80 host
       explainsh git log --graph --abbrev-commit --pretty=oneline origin..mybranch
```

## Using `explainsh` with Docker

There is an image in Docker Hub called `7rocky/explainsh` to execute `explainsh` from a Docker container:

```console
$ docker run --rm -it 7rocky/explainsh <command>
```

If you want to build and run the image locally:

```console
cd explainsh/
docker build -t explainsh .
docker run --rm -it explainsh <command>
```

And again, if the `<command>` contains special characters, wrap it between single quotes.

Hope it is useful! :smile:
