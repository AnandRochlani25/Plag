cohort = "fw10"
unit = 3
sprint = 2
filename = "scripts/checkout"
extension = "js"

s='SELECT report_id from blog_report where cohort_id="'+cohort+'" and unit='+str(unit)+' and sprint='+str(sprint)+' and filename="'+filename+'"and extension="'+extension+'"'
print(s)