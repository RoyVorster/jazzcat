from datetime import datetime, timedelta, date, time
import numpy as np
import os
import click
import git

from .characters import *

DEFAULT_FILE = "run.py"
DEFAULT_CODE = "lorem=sum(40, 2)"

DATE_FMT = "%Y-%m-%d %H:%M:%S" # ISO format for git commits
DATE_TZ = "UTC" # Github board is timezone aware

# Edit a file
def make_edit(file_name, code):
    with open(file_name, 'w') as f:
        f.write(code)

# Make edit and commit
def make_commit(repo, dt, msg, file_name=DEFAULT_FILE, code=DEFAULT_CODE):
    make_edit(file_name, code)

    repo.index.add([DEFAULT_FILE])
    date_string = dt.strftime(DATE_FMT)

    os.environ['GIT_AUTHOR_DATE'] = date_string
    os.environ['GIT_COMMITTER_DATE'] = date_string
    os.environ['TZ'] = DATE_TZ
    repo.index.commit(msg)

# Need to start on a sunday to line up with contribution graph
def get_start_date(start_year, start_month):
    start_date = date(start_year, start_month, 1)

    n_day = start_date.weekday()
    if n_day == 0:
        return start_date

    offset = (6 - n_day) % 7
    return start_date + timedelta(days=offset)

# Jazz it up
def jazz_it_up(text, start_year, dry_run=False, file_name=DEFAULT_FILE, code=DEFAULT_CODE, start_month=1):
    bmp = get_bitmap(text)

    if dry_run:
        plt_bitmap(bmp)
        return

    # Offset dates correctly
    start_date = get_start_date(start_year, start_month)
    dates = [start_date + i*timedelta(days=1) for i in range(np.prod(bmp.shape))]

    commit = bmp.T.flatten()
    dates = [d for (d, c) in zip(dates, commit) if c]

    t = time(hour=11, minute=59) # All commits just before lunch, consistent in timezones

    # Make the commits
    repo = git.Repo.init(os.getcwd())
    for i, date in enumerate(dates):
        print(f"Making commit {i}/{len(dates)}", end="\r")
        make_commit(repo, datetime.combine(date, t), f"easteregg commit {i}")

if __name__ == '__main__':
    jazz("ROY VORSTER", dry_run=True)
