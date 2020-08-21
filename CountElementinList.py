# 6) How to count the occurrences of a particular element in the list?
#
# A) In Python list, we can count the occurrences of an individual element by using a <count()> function.
#
# Example # 1:

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(weekdays.count('mon'))


# Example # 2:

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[x,weekdays.count(x)] for x in set(weekdays)])