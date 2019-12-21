from votingsystem.dbqueries import *

def createset(voting_id):
    voting = getvoting(voting_id)
    options = getoptions(voting_id)
    result = getresult(voting_id)

    dataset = []
    for i in result:
        #d.update({gettitleoptions(i):getresultbyoption(i)})
        dataset.append({'option':gettitleoptions(i), 'count':getresultbyoption(i)})

    print()
    print(dataset)
    print()
    dataset1=[
  {'ticket_class': 1, 'survived_count': 200, 'not_survived_count': 123},
  {'ticket_class': 2, 'survived_count': 119, 'not_survived_count': 158},
  {'ticket_class': 3, 'survived_count': 181, 'not_survived_count': 528}
]
    print()
    return(dataset)


def createsetbyage(voting_id):
    voting = getvoting(voting_id)
    options = getoptions(voting_id)
    result = getresult(voting_id)
    age = getages(voting_id)
    print(age) 

    dataset = []
    for i in result:
        #d.update({gettitleoptions(i):getresultbyoption(i)})
        dataset.append({'option':gettitleoptions(i), 'count':getresultbyoption(i)})

    print()
    print(dataset)
    print()
    dataset1=[
  {'ticket_class': 1, 'survived_count': 200, 'not_survived_count': 123},
  {'ticket_class': 2, 'survived_count': 119, 'not_survived_count': 158},
  {'ticket_class': 3, 'survived_count': 181, 'not_survived_count': 528}
]
    print()
    return(dataset)
# def ticket_class_view(request):
#     dataset = Passenger.objects \
#         .values('ticket_class') \
#         .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
#                   not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
#         .order_by('ticket_class')
#     return render(request, 'ticket_class.html', {'dataset': dataset})
#

# [
#   {'ticket_class': 1, 'survived_count': 200, 'not_survived_count': 123},
#   {'ticket_class': 2, 'survived_count': 119, 'not_survived_count': 158},
#   {'ticket_class': 3, 'survived_count': 181, 'not_survived_count': 528}
# ]
