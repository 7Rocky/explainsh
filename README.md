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

For example:

```console
$ explainsh nmap -sC -sV -p22,80 10.10.10.10

Network exploration tool and security / port scanner

-sC .
    Performs a script scan using the default set of scripts. It is equivalent to --script=default. Some
    of the scripts in this category are considered intrusive and should not be run against a target
    network without permission.

-sV (Version detection) .
    Enables version detection, as discussed above. Alternatively, you can use -A, which enables version
    detection among other things.

-p port ranges (Only scan specified ports) .
    This option specifies which ports you want to scan and overrides the default. Individual port numbers
    are OK, as are ranges separated by a hyphen (e.g.  1-1023). The beginning and/or end values of a
    range may be omitted, causing Nmap to use 1 and 65535, respectively. So you can specify -p- to scan
    ports from 1 through 65535. Scanning port zero.  is allowed if you specify it explicitly. For IP
    protocol scanning (-sO), this option specifies the protocol numbers you wish to scan for (0–255).

    When scanning both TCP and UDP ports, you can specify a particular protocol by preceding the port
    numbers by T: or U:. The qualifier lasts until you specify another qualifier. For example, the
    argument -p U:53,111,137,T:21-25,80,139,8080 would scan UDP ports 53, 111,and 137, as well as the
    listed TCP ports. Note that to scan both UDP and TCP, you have to specify -sU and at least one TCP
    scan type (such as -sS, -sF, or -sT). If no protocol qualifier is given, the port numbers are added
    to all protocol lists.  Ports can also be specified by name according to what the port is referred to
    in the nmap-services. You can even use the wildcards * and ? with the names. For example, to scan FTP
    and all ports whose names begin with “http”, use -p ftp,http*. Be careful about shell expansions and
    quote the argument to -p if unsure.

    Ranges of ports can be surrounded by square brackets to indicate ports inside that range that appear
    in nmap-services. For example, the following will scan all ports in nmap-services equal to or below
    1024: -p [-1024]. Be careful with shell expansions and quote the argument to -p if unsure.

nmap [Scan Type...] [Options] {target specification}

http://manpages.ubuntu.com/manpages/precise/en/man1/nmap.html
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
$ cd explainsh/
$ docker build -t explainsh .
$ docker run --rm -it explainsh <command>
```

And again, if the `<command>` contains special characters, wrap it between single quotes.

Hope it is useful! :smile:
