#!/usr/bin/python
"""
    	This is the main module.

    	Luis Filipe Ribeiro Dias
              DTV Research
                  2016
"""
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
from database import DB

def main():
	"""
		main function

    :return: 0 on success
	"""
	J = Jenkins('http://localhost:8080')
	jobs = server.get_jobs()
    print jobs
    d_b = DB("jenkins.db")
    d_b.connect()
    return 0

if __name__ == '__main__':
    main()
