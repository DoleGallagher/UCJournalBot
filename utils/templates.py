from random import choice

job_sites = (
    'Indeed', 'S1 Jobs', 'Totaljobs', 'Reed', 'Adzuna', 'Gumtree', 'Monster',
    'Jobsite', 'Jobrapido', 'Jobstoday', 'JobisJob', 'Jobswype', 'Fish4Jobs',
    'Job Today', 'The Independent Jobs', 'CV Library'
)


templates = [
    ('Spent {0} hours searching on {1} for possible job.Spent {2} hours on '
     'looking up the company and tailoring the cv for it then applied for the job'),
    ('I spent {0} hours searching {1} for a job opportunity and then spent '
     'additional time researching the company and adjusting my CV before applying'),
    ('{0} hours were dedicated to scouring {1} for a job opening, followed by another '
     '{2} hours of researching the company and customizing my CV before submitting an application'),
    ('I spent {0} hours on {1} searching for job opportunities and then spent another {2} '
     'hours researching the company and customizing my CV before submitting my application'),
    ('{0} hours were spent searching {1} for a job and then {2} more hours were spent '
     'researching the company and customizing my CV before applying'),
    ('I took {0} hours to search {1} for job opportunities and then spent another {2} '
     'hours to researching the company and tailoring my CV before submitting my application'),
    ('I spent {0} hours looking for job prospects on {1} and then spent another {2} hours '
     'researching the company and adjusting my CV before applying'),
    ('My job search on {1} took {0} hours, after which I spent another {2} hours '
     'researching the company and customizing my CV before submitting my application'),
    ('I allocated {0} hours for searching for job opportunities on {1} and then '
     'spent another {2} hours researching the company and personalizing my CV before applying'),
    ('{0} hours were spent searching on {1} for job openings, followed by an additional '
     '{2} hours of researching the company and fine-tuning my CV before submitting my application'),
    ('Spent {0} hours scouring {1} for potential job prospects before dedicating an equal amount '
     'of time to researching the company and tailoring my CV for the position, which I eventually applied for.'),
    ('I spent {0} hours searching on {1} for job opportunities and then spent another {2} hours '
     'researching the company and customizing my CV before submitting my application.'),
    ('Spent {0} hours searching {1} for job openings, followed by another {2} hours spent '
     'researching the company and adjusting my CV before submitting my application.'),
    ('I took {0} hours to search {1} for job prospects, and then spent another {2} hours researching '
     'the company and personalizing my CV before applying.'),
    ('I allocated {0} hours for searching {1} for job opportunities, and then spent another {2} hours '
     'researching the company and fine-tuning my CV before submitting my application.'),
    ('Spent {0} hours on {1} searching for job openings, followed by another {2} hours '
     'researching the company and adjusting my CV before applying.'),
    ('My job search on {1} took {0} hours, after which I spent another {2} hours '
     'researching the company and customizing my CV before submitting my application.'),
    ('I spent {0} hours on {1} looking for job prospects, and then spent another {2} hours '
     'researching the company and tailoring my CV before applying.'),
    ('Dedicated {0} hours to scouring {1} for job opportunities, followed by another '
     '{2} hours of researching the company and customizing my CV before submitting an application.'),
    ('I spent {0} hours searching {1} for possible job opportunities, and then spent another {2} hours '
     'researching the company and tailoring my CV before applying for the job.'),
]


def create_templates(n):
    notes = []
    for _ in range(n):
        note = choice(templates)
        notes.append(note.format(choice((2, 3)), choice(job_sites), choice((2, 3))))
    return notes



