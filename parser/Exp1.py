from dateutil import relativedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime


def req_to_list(data):
    """
    Convert Dates from request TO
    List of (startDate, endDate)
    """

    exp_dates_list = []
    titles = []
    for ex in data['experiences']:
        startDate = ex['startDate']
        endDate = ex['endDate']
        exp_dates_list.append((startDate, endDate))
        titles.append(ex['jobTitle'])


    return exp_dates_list, titles


def dates_to_experience(exp_dates_list, titles):
    """
    Takes list of start and end dates (Generated by `~Exp.req_to_list`) and calculate experience
    """
    # initializing total_exp i.e creating emplty relativedelta with Y=0, M=0 D=0
    total_exp = relativedelta()
    
    exp_list = {}

    i = 0
    for startDate, endDate in exp_dates_list:
        start = datetime.strptime(startDate, "%d/%m/%Y")
        end = datetime.strptime(endDate, "%d/%m/%Y")
        # Get the interval between two dates
        diff = relativedelta(end, start)
        total_exp = total_exp + diff


        if titles[i] in exp_list:
            exp_list[titles[i]] += diff
        else:
            exp_list[titles[i]] = diff
        i += 1
            
    return total_exp, exp_list



def exp_correction(exp):

    years = exp.years
    months = exp.months,
    days = exp.days

    new_days = days % 30
    
    new_months = months[0] + days // 30
  
    new_years = years + new_months // 12

    new_months = new_months % 12

    new_years = new_years + round(new_months/12, 1)

    # final_exp = relativedelta(years=new_years, months=new_months, days=new_days)
    return new_years
    # return final_exp

def get_total_experience(request_query: dict) -> relativedelta:
    """
    Takes request query (dict) and return total experience.

    Parameters:
        request_query (dict): Request data containing experience information.

    Returns:
        Total experience (relativedelta): containing total experience in years, months and days
        Relative experience (dict): job titles with respective experience.
    """
    if not isinstance(request_query, dict):
        raise AssertionError('input must be dict object')
    x = req_to_list(request_query)

    exp, exp_list = dates_to_experience(x[0], x[1])

    
    final_exp = exp_correction(exp)
    for job_title in exp_list:
        exp_list[job_title] = exp_correction(exp_list[job_title])

    return final_exp, exp_list

