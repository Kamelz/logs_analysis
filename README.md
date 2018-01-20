# Logs Analysis
A python script that analys a database log.

## Setup & Running
 - Install [python](https://www.python.org/downloads/) version 3.6.2.
 - Download and install [Git bash](https://git-scm.com/downloads) if you don't have a command line interface.
 - Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
 - Download and install [Vagrant](https://www.vagrantup.com/).
 - Clone or download [Fullstack Nanodegree VM](https://github.com/udacity/fullstack-nanodegree-vm) repository.
 - [Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
 - Extract it and you'll find an sql file `newsdata.sql` put this file inside vagrant directory alongside the `connection.py` and `log.py`, which is shared with your virtual machine.
 - Go to vagrant directory and open a terminal then type: `vagrant up`
 - After that you'll get your shell back then type: `vagrant ssh` to log in.
 - Make sure you have `newsdata.sql` sql file type `ls` to view the files in your directory.
 - Then type `psql -d news -f newsdata.sql`
 - Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
 - Run the `python log.py` to run the script, it'll print the result in the shell and also it'll export the result in `output.txt`.

