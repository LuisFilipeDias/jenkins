#!/usr/bin/python
"""
    This is the main module.

    Luis Filipe Ribeiro Dias
        DTV Research
            2016
"""
from jenkinsapi.jenkins import Jenkins
from database import DB


def main():
    """
        main function

    :return: 0 on success
    """
    jenkins = Jenkins('http://localhost:8080/jenkins', 'user', '16794350')
    keys = jenkins.keys()
    # jobs = jenkins.get_jobs()
    for key in keys:
        job = jenkins.get_job(key)
        print("\nJob: %s" % job)
        builds = job.get_build_dict()
        for b_i in builds:
            status = job.get_build(b_i).get_status()
            print("Status of build: %d %s" % (b_i, status))
    return 0


if __name__ == '__main__':
    main()
