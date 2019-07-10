# Catalog Analysis

The program you write in this project will run from the command line. 
It won't take any input from the user. 
Instead, it will connect to a database, use SQL queries to analyze the log data, and print out the answers to some questions.

The printout will be in the console where the script is called.

## Getting Started

These instructions will get you a copy of he project up and running on your local machine.

### Prerequisites

To run the VM, you must have the following:
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/)

For more information on the base setup that this project is running off of, visit the [Udacity VM Setup](https://github.com/udacity/fullstack-nanodegree-vm)

To have the project run, you need to download the import data:
* [Import Data](https://drive.google.com/file/d/1iy8bCofa7JJRINPeFdDQoY7SkEKBnKNx/view?usp=sharing)

### Running the VM

To run the VM you must do the following:
1. Obtain a copy of the repository from: [Repo Zip](https://github.com/udacity/fullstack-nanodegree-vm/archive/master.zip)
2. Unzip the master.zip file to a directory
3. Open a command prompt/PowerShell/terminal window
4. Navigate to the project folder in the directory that you chose in step 2
5. Copy the [Import Data](https://drive.google.com/file/d/1iy8bCofa7JJRINPeFdDQoY7SkEKBnKNx/view?usp=sharing) file into the project folder
**NOTE**: Be sure to note the name of the file and keep the sql extension. In step 8, replace **newdata.sql** with this file name.
6. Run the following commands
```
vagrant init
vagrant up
vagrant ssh
```

### Setting up the data

Once you establish a connection to your VM, do the following:
1. Navigate to the loganalysis folder
```
cd /vagrant/loganalysis
```
2. Import the database data
```
psql -d news -f newdata.sql
```

### Printing the log analysis data

Now that the data has been imported, run the project file:
```
python3 ./loganalysis.py
```

### Example of Project's output
You should now be able to review the analysis results that the database has found.

Review the [Example.txt](https://github.com/Justin-Tadlock/Log-Analysis/blob/master/example.txt) file for an example of what you should see.

## Built With

* [Python](https://www.python.org/downloads/) - Python is a programming language that lets you work quickly and integrate systems more effectively
* [PostgreSQL](https://www.postgresql.org/download/) - The World's Most Advanced Open Source Relational Database

## Authors

* **[Justin-Tadlock](https://github.com/Justin-Tadlock)** - *Initial work*

## Acknowledgments

* [Udacity VM Setup](https://github.com/udacity/fullstack-nanodegree-vm) - for the initial setup of the Vagrant VM.
