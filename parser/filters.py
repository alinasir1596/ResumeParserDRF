
def filteration(tool, ex, job_title):
    _tool = False,
    _experience = False
    _title = False
    if isinstance(tool, list) and len(tool) > 0 and tool[0] == '1':
        _tool = True
    if isinstance(ex, list) and len(ex) > 0 and ex[0] == 1:
        _experience = True
    if isinstance(job_title, list) and len(job_title) > 0 and job_title[0] == 1:
        _title = True

    return _tool, _experience, _title
