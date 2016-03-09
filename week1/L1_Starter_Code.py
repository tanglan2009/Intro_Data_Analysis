

import unicodecsv
import csv

## Longer version of code (replaced with shorter, equivalent version below)

enrollments = []
f = open('enrollments.csv', 'rb')
reader = unicodecsv.DictReader(f)
for row in reader:
    enrollments.append(row)
f.close()

print enrollments[0]
with open('enrollments.csv', 'rb') as f:
    reader =unicodecsv.DictReader(f)
    enrollments = list(reader)




#####################################
#                 1                 #
#####################################

## Read in the data from daily_engagement.csv and project_submissions.csv 
## and store the results in the below variables.
## Then look at the first row of each table.

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f) #each row is a dictionary
        return list(reader)
    
enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

print enrollments[0]
print daily_engagement[0]
print project_submissions[0]


# ## Fixing Data Types


from datetime import datetime as dt

# Takes a date as a string, and returns a Python datetime object. 
# If there is no date given, returns None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
    
# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    
enrollments[0]



# Clean up the data types in the engagement table
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
    
daily_engagement[0]



# Clean up the data types in the submissions table
for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

project_submissions[0]



for engagement_record in daily_engagement:
    
    engagement_record['account_key'] = engagement_record['acct']
    del engagement_record['acct']


# ## Investigating the Data



#####################################
#                 2                 #
#####################################

## Find the total number of rows and the number of unique students (account keys)
## in each table.


    

def getUiqueStudents(data):
    unique_students = set()
    for account_key in data:
        unique_students.add(account_key['account_key'])
    return unique_students
    
enrollment_num_rows = len(enrollments)  
print 'the total number of rows in "enrollment" is', enrollment_num_rows
enrollment_num_unique_students = len(getUiqueStudents (enrollments))  # Replace this with your code
print 'the number of unique students in "enrollment" is', enrollment_num_unique_students

engagement_num_rows = len(daily_engagement)           # Replace this with your code
print 'the total number of rows in "daily_engagement" is', engagement_num_rows
# engagement_num_unique_students = set()
# for accou in daily_engagement:
#     engagement_num_unique_students.add(accou['acct'])
# print 'the number of unique students in "daily_engagement" is', len(engagement_num_unique_students)
engagement_num_unique_students = len(getUiqueStudents(daily_engagement))
print 'the number of unique students in "daily_engagement" is', engagement_num_unique_students

submission_num_rows = len(project_submissions)           # Replace this with your code
print 'the total number of rows in "project_submissions" is ', submission_num_rows
submission_num_unique_students = len(getUiqueStudents(project_submissions))
print 'the number of unique students in "project_submissions" is ', submission_num_unique_students


# ## Problems in the Data

# In[48]:

#####################################
#                 3                 #
#####################################

# ## Rename the "acct" column in the daily_engagement table to "account_key".

# for ele in daily_engagement:
#     ele['account_key'] = ele['acct']
#     del ele['acct']
# print daily_engagement[0]['account_key']


# ## Missing Engagement Records

# In[64]:

#####################################
#                 4                 #
#####################################

## Find any one student enrollments where the student is missing from the daily engagement table.
## Output that enrollment.
# missingStudents= []
# for student in getUiqueStudents(enrollments):
#     if  student not in getUiqueStudents(daily_engagement):
#         missingStudents.append(student)
# print missingStudents

for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in getUiqueStudents(daily_engagement):
        print enrollment
        break


# ## Checking for More Problem Records

# In[66]:

#####################################
#                 5                 #
#####################################

## Find the number of surprising data points (enrollments missing from
## the engagement table) that remain, if any.
numOfSurprise = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in getUiqueStudents(daily_engagement) and enrollment['days_to_cancel'] != 0:
        print enrollment
        numOfSurprise += 1
print numOfSurprise
print 'done'


# ## Tracking Down the Remaining Problems

# In[68]:

# Create a set of the account keys for all Udacity test accounts
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
len(udacity_test_accounts)


# In[69]:

# Given some data with an account_key field, removes any records corresponding to Udacity test accounts
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data


# In[70]:

# Remove Udacity test accounts from all three tables
non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print len(non_udacity_enrollments)
print len(non_udacity_engagement)
print len(non_udacity_submissions)


# ## Refining the Question

# In[77]:

#####################################
#                 6                 #
#####################################

## Create a dictionary named paid_students containing all students who either
## haven't canceled yet or who remained enrolled for more than 7 days. The keys
## should be account keys, and the values should be the date the student enrolled.
paid_students = {}
for enrollment in non_udacity_enrollments:
    #if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
    if enrollment['days_to_cancel'] == None or enrollment['days_to_cancel'] > 7:
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        
        if account_key not in paid_students or enrollment_date > paid_students[account_key]:
            paid_students[account_key] = enrollment_date
        
        
print paid_students


# ## Getting Data from First Week

# In[75]:

# Takes a student's join date and the date of a specific engagement record,
# and returns True if that engagement record happened within one week
# of the student joining.
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7 and time_delta.days >= 0


# In[85]:


def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data


# In[86]:

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

print len(paid_enrollments)
print len(paid_engagement)
print len(paid_submissions)


# In[92]:

for engagement_record in paid_engagement:
    if engagement_record['num_courses_visited'] > 0:
        engagement_record['has_visited'] = 1
    else:
        engagement_record['has_visited'] = 0


# In[93]:

#####################################
#                 7                 #
#####################################

## Create a list of rows from the engagement table including only rows where
## the student is one of the paid students you just found, and the date is within
## one week of the student's join date.
paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']
    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)    
    

print len(paid_engagement_in_first_week)

# ## Exploring Student Engagement

# In[94]:

from collections import defaultdict

def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

engagement_by_account = group_data(paid_engagement_in_first_week, 'account_key')

# Create a dictionary of engagement grouped by student.
# The keys are account keys, and the values are lists of engagement records.
# engagement_by_account = defaultdict(list)
# for engagement_record in paid_engagement_in_first_week:
#     account_key = engagement_record['account_key']
#     engagement_by_account[account_key].append(engagement_record)



# In[96]:

# Create a dictionary with the total minutes each student spent in the classroom during the first week.
# The keys are account keys, and the values are numbers (total minutes)
def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
            summed_data[key] = total
    return summed_data
total_minutes_by_account = sum_grouped_items(engagement_by_account, 'total_minutes_visited')


# In[97]:



import numpy as np

# # Summarize the data about minutes spent in the classroom
# total_minutes = total_minutes_by_account.values()
# print 'Mean:', np.mean(total_minutes)
# print 'Standard deviation:', np.std(total_minutes)
# print 'Minimum:', np.min(total_minutes)
# print 'Maximum:', np.max(total_minutes)

def describe_data(data):
    print 'Mean:', np.mean(data)
    print 'Standard deviation:', np.std(data)
    print 'Minimum:', np.min(data)
    print 'Maximum:', np.max(data)

total_minutes = total_minutes_by_account.values()
describe_data(total_minutes)





# ## Debugging Data Analysis Code

# In[98]:

#####################################
#                 8                 #
#####################################

## Go through a similar process as before to see if there is a problem.
## Locate at least one surprising piece of data, output it, and take a look at it.
student_with_max_minutes = None
max_minutes = 0

for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes = student
        
print max_minutes


# In[99]:

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] == student_with_max_minutes:
        print engagement_record
    


# ## Lessons Completed in First Week

# In[104]:

#####################################
#                 9                 #
#####################################

## Adapt the code above to find the mean, standard deviation, minimum, and maximum for
## the number of lessons completed by each student during the first week. Try creating
# ## one or more functions to re-use the code above.
# total_numOfLessons_by_account = {}
# for account_key, engagement_for_student in engagement_by_account.items():
#     total_numOfLessions = 0
#     for engagement_record in engagement_for_student:
#         total_numOfLessions += engagement_record['lessons_completed']
#     total_numOfLessons_by_account[account_key] = total_numOfLessions
    
# total_numOfLessions = total_numOfLessons_by_account.values()
# print 'Mean:', np.mean(total_numOfLessions)
# print 'Standard deviation:', np.std(total_numOfLessions)
# print 'Minimum:', np.min(total_numOfLessions)
# print 'Maximum:', np.max(total_numOfLessions)
lessons_completed_by_account = sum_grouped_items(engagement_by_account, 'lessons_completed')
total_lessons_completed = lessons_completed_by_account.values()
describe_data(total_lessons_completed)



# ## Number of Visits in First Week

# In[36]:

######################################
#                 10                 #
######################################

## Find the mean, standard deviation, minimum, and maximum for the number of
## days each student visits the classroom during the first week.

days_visited_by_account = sum_grouped_items(engagement_by_account, 'has_visited')
describe_data(days_visited_by_account.values())


# ## Splitting out Passing Students

# In[107]:

######################################
#                 11                 #
######################################

## Create two lists of engagement data for paid students in the first week.
## The first list should contain data for students who eventually pass the
## subway project, and the second list should contain data for students
## who do not.

subway_project_lesson_keys = ['746169184', '3176718735']

pass_subway_project =set()

for submission in paid_submissions:
    project = submission['lesson_key']
    rating = submission['assigned_rating']
    if (project in subway_project_lesson_keys) and (rating == 'PASSED'or rating == 'DISTINCTION'):
#         print 'testig..'
#         print submission['account_key']
        pass_subway_project.add(submission['account_key'])

len(pass_subway_project)
print pass_subway_project
# print u'344' in pass_subway_project, type(u'344')


# In[108]:

# subway_project_lesson_keys = ['746169184', '3176718735']

# pass_subway_project = set()

# for submission in paid_submissions:
#     project = submission['lesson_key']
#     rating = submission['assigned_rating']    

#     if ((project in subway_project_lesson_keys) and
#             (rating == 'PASSED' or rating == 'DISTINCTION')):
#         pass_subway_project.add(submission['account_key'])

# len(pass_subway_project)

passing_engagement = []
non_passing_engagement = []

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print len(passing_engagement)
print len(non_passing_engagement)


# In[64]:

passing_engagement_by_account = []
non_passing_engagement_by_account = []
for engagement_record in paid_engagement_in_first_week:
#for engagement_record in paid_engagement_in_first_week:

#    # print engagment_record['account_key'], type(engagement_record['account_key'])
    if engagement_record['account_key'] in pass_subway_project:
    #if engagement_record['account_key'] in pass_subway_project:
#         print 'in the pass', engagement_record['account_key']
       # passing_engagement.append(engagement_record)
        passing_engagement_by_account.append(engagement_record)
#     else:
#         non_passing_engagement.append(engagement_record)
        
    else:
        non_passing_engagement_by_account.append(engagement_record)
    

print len(passing_engagement_by_account)
print len(non_passing_engagement_by_account)


# ## Comparing the Two Student Groups

# In[114]:

######################################
#                 12                 #
######################################

## Compute some metrics you're interested in and see how they differ for
## students who pass the subway project vs. students who don't. A good
## starting point would be the metrics we looked at earlier (minutes spent
## in the classroom, lessons completed, and days visited).
passing_minutesSpend_by_account = []
nonpassing_minutesSpend_by_account = []

for engagement_record in passing_engagement:
    passing_minutesSpend_by_account.append(engagement_record['total_minutes_visited'])

for engagement_record in non_passing_engagement:
    
    nonpassing_minutesSpend_by_account.append(engagement_record['total_minutes_visited'])
print len(passing_minutesSpend_by_account)
print len(nonpassing_minutesSpend_by_account)

total_passing = 0
for minutes in passing_minutesSpend_by_account:
    total_passing += minutes
    
mean1 = total_passing/len(passing_minutesSpend_by_account)
print total_passing, mean1

total_nonpassing = 0
for minutes in nonpassing_minutesSpend_by_account:
    total_nonpassing += minutes

mean2 =  total_nonpassing/len(nonpassing_minutesSpend_by_account)
print total_nonpassing, mean2
    
passing_engagement_by_account = group_data(passing_engagement, 'account_key')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')


# In[115]:

data = [1, 2, 1, 3, 3, 1, 4, 2]

import matplotlib.pyplot as plt
plt.hist(data)


# In[120]:

print 'non_passing students:'
non_passing_minutes = sum_grouped_items(non_passing_engagement_by_account, 'total_minutes_visited')
describe_data(non_passing_minutes.values())
print "passing students: "
passing_minutes = sum_grouped_items(passing_engagement_by_account, 'total_minutes_visited')
describe_data(passing_minutes.values())
print passing_minutes.values()

print 'non-passing students:'
non_passing_lessons = sum_grouped_items(
    non_passing_engagement_by_account,
    'lessons_completed'
)
describe_data(non_passing_lessons.values())

print 'passing students:'
passing_lessons = sum_grouped_items(
    passing_engagement_by_account,
    'lessons_completed'
)
describe_data(passing_lessons.values())

print 'non-passing students:'
non_passing_visits = sum_grouped_items(
    non_passing_engagement_by_account, 
    'has_visited'
)
describe_data(non_passing_visits.values())

print 'passing students:'
passing_visits = sum_grouped_items(
    passing_engagement_by_account,
    'has_visited'
)
describe_data(passing_visits.values())


# In[121]:

plt.hist(passing_visits.values())


# In[122]:

import seaborn as sns
plt.xlabel("Total amount of minutes spent")
plt.ylabel("Number of passing students")
plt.hist(passing_minutes.values(), bins = 8)
plt.show()


# In[123]:

plt.hist(non_passing_minutes.values())


# In[90]:

plt.hist(passing_visits.values())


# In[125]:

import seaborn as sns
plt.xlabel("Number of days")
plt.title("Distribution of classroom visists in the first week for students who pass the subway project")
plt.hist(passing_visits.values(), bins = 8)


# In[91]:

plt.hist(non_passing_visits.values())


# ## Making Histograms

# In[110]:

######################################
#                 13                 #
######################################

## Make histograms of the three metrics we looked at earlier for both
## students who passed the subway project and students who didn't. You
## might also want to make histograms of any other metrics you examined.
import matplotlib.pyplot as plt
import numpy as np
def describe_data(data):
    print 'Mean:', np.mean(data)
    print 'Standard deviation:', np.std(data)
    print 'Minimum:', np.min(data)
    print 'Maximum:', np.max(data)
    plt.hist(data)
    
total_minutes = total_minutes_by_account.values()
describe_data(total_minutes)



# ## Improving Plots and Sharing Findings

# In[ ]:

######################################
#                 14                 #
######################################

## Make a more polished version of at least one of your visualizations
## from earlier. Try importing the seaborn library to make the visualization
## look better, adding axis labels and a title, and changing one or more
## arguments to the hist() function.


