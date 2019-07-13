"""
https://app.codesignal.com/company-challenges/dropbox/RMJDiTprBf5HQY3oa

Dropbox holds a competition between schools called CampusCup. If you verify an email address from a college, 
university, or higher education institution, you earn 20 points toward your school's overall ranking. When a 
school receives at least 100 points, all of its registered members receive an additional 3 Gb of bonus space each.
 When the school receives at least 200 points, its registered members receive an additional 8 Gb. If the school 
 receives at least 300 points, its members receive an additional 15 Gb. And finally, when a school receives at 
 least 500 points, members receive an additional 25 Gb each.

You are given n registered emails, all of them unique. Each email has the following format: "<name>@<domain>", 
where <name> and <domain> are non-empty strings consisting of lowercase letters and a '.'. Identical domains 
correspond to the same school and vice versa.

Your task is to make a scoreboard, i.e. to sort the schools according to the amount of bonus space they each 
received (per student not in total). School A must be higher in the standings than school B if A received more 
space than B, or if they received equal number of gigabytes but the domain string of school A is lexicographically 
smaller than the one of school B.

For emails = ["john.doe@mit.edu", "admin@rain.ifmo.ru", "noname@mit.edu"], the output should be
campusCup(emails) = ["mit.edu", "rain.ifmo.ru"].

"mit.edu" scored 40 points, and "rain.ifmo.ru" just 20. Both universities got no additional space, so "mit.edu" 
must be higher in the standings because it is lexicographically smaller than "rain.ifmo.ru".

For

emails = ["b@harvard.edu", "c@harvard.edu", "d@harvard.edu", 
          "e@harvard.edu", "f@harvard.edu",
          "a@student.spbu.ru", "b@student.spbu.ru", "c@student.spbu.ru", 
          "d@student.spbu.ru", "e@student.spbu.ru", "f@student.spbu.ru", 
          "g@student.spbu.ru"]
the output should be
campusCup(emails) = ["harvard.edu", "student.spbu.ru"].

"harvard.edu" - 100 points, 3 Gb of additional space.
"student.spbu.ru" - 140 points, also 3 Gb of additional space.

"harvard.edu" must be higher in the standings because it is lexicographically smaller than "student.spbu.ru".

For

emails = ["a@rain.ifmo.ru", "b@rain.ifmo.ru", "c@rain.ifmo.ru", 
          "d@rain.ifmo.ru", "e@rain.ifmo.ru", "noname@mit.edu"]
the output should be
campusCup(emails) = ["rain.ifmo.ru", "mit.edu"].

"mit.edu" - 20 points, no additional space.
"rain.ifmo.ru" - 100 points, 3 Gb of additional space.

Therefore, "rain.ifmo.ru" must be higher in the standings.

Input/Output

[execution time limit] 4 seconds (py)

[input] array.string emails

Registered emails.

Guaranteed constraints:
2 ≤ emails.length ≤ 40,
5 ≤ emails[i].length ≤ 20.

[output] array.string
emails: ["a@rain.ifmo.ru", 
 "b@rain.ifmo.ru", 
 "c@rain.ifmo.ru", 
 "d@rain.ifmo.ru", 
 "e@rain.ifmo.ru", 
 "noname@mit.edu"]

The list of unique school domains sorted as described above
"""
from collections import defaultdict
import collections
def campusName (email):
    return email.split('@')[-1]

def campusCup(emails):
    campusMails = defaultdict(int)
    for i in emails:
        nameCampus = campusName(i)
        campusMails[nameCampus]+=20
    ordCampus = {0:[], 1: [], 2:[], 3:[], 4:[]}
    print(campusMails)
    for campus in campusMails:
        if (campusMails[campus]< 100):
            ordCampus[4].append(campus)
        elif (100 <= campusMails[campus] and campusMails[campus]<200):
            ordCampus[3].append(campus)
        elif(200<= campusMails[campus] and campusMails[campus]<300):
            ordCampus[2].append(campus)
        elif(300<= campusMails[campus] and campusMails[campus] <500):
            ordCampus[2].append(campus)
        else:
            ordCampus[1].append(campus)
    for i in ordCampus:
            ordCampus[i].sort()
    l = lambda dic: [item for list in dic for item in dic[list]]
    return l(ordCampus)

print(campusCup(["b@rain.ifmo.ru", 
 "c@rain.ifmo.ru", 
 "d@rain.ifmo.ru", 
 "e@rain.ifmo.ru", 
 "f@rain.ifmo.ru", 
 "g@rain.ifmo.ru", 
 "h@rain.ifmo.ru", 
 "i@rain.ifmo.ru", 
 "j@rain.ifmo.ru", 
 "k@rain.ifmo.ru", 
 "l@rain.ifmo.ru", 
 "m@rain.ifmo.ru", 
 "n@rain.ifmo.ru", 
 "o@rain.ifmo.ru", 
 "p@rain.ifmo.ru", 
 "q@rain.ifmo.ru", 
 "r@rain.ifmo.ru", 
 "s@rain.ifmo.ru", 
 "t@rain.ifmo.ru", 
 "u@rain.ifmo.ru", 
 "v@rain.ifmo.ru", 
 "w@rain.ifmo.ru", 
 "x@rain.ifmo.ru", 
 "y@rain.ifmo.ru", 
 "a@mit.edu.ru", 
 "b@mit.edu.ru", 
 "c@mit.edu.ru", 
 "d@mit.edu.ru", 
 "e@mit.edu.ru", 
 "f@mit.edu.ru", 
 "g@mit.edu.ru", 
 "h@mit.edu.ru", 
 "i@mit.edu.ru", 
 "j@mit.edu.ru", 
 "k@mit.edu.ru", 
 "l@mit.edu.ru", 
 "m@mit.edu.ru", 
 "n@mit.edu.ru", 
 "o@mit.edu.ru"]))