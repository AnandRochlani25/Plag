import csv
from github import Github
from html.parser import HTMLParser
from .keywords import html_close_map, html_open_map
from pprint import pprint
from typing_extensions import final

def home_page_unit(request):
    return render(request,'app/home1.html')
# Creds
TOKEN = "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"
g = Github(TOKEN)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.to_ret = {}
        self.token = ""
        self.content_data = []
        self.ids = []
        self.classes = []
        self.type = []
        self.value = []
        self.hrefs = []
        self.srcs = []
        self.others = []


    def handle_starttag(self, tag, attrs):
        if tag in html_open_map:
            self.token += html_open_map[tag]
        else:
            ## MEANS A TAG WHICH HAS NOT BEEN TAUGHT IS BEING USED ##
            self.token += "+"
        for attr in attrs:
            # print(attr[0], attr[1])
            if attr[0] == 'id':
                self.ids.append(attr[1])
            elif attr[0] == 'class':
                self.classes.append(attr[1])
            elif attr[0] == 'href':
                self.hrefs.append(attr[1])
            elif attr[0] == 'type':
                self.type.append(attr[1])
            elif attr[0] == 'src':
                self.srcs.append(attr[1])
            else:
                self.others.append(attr[1])


    def handle_endtag(self, tag):
        if tag in html_close_map:
            self.token += html_close_map[tag]
        else:
            ## MEANS A TAG WHICH HAS NOT BEEN TAUGHT IS BEING USED ##
            self.token += "="

    def handle_data(self, data):
        self.content_data.append(data)


    def get_token(self):
        self.to_ret['token'] = self.token
        self.to_ret['content_data'] = self.content_data
        self.to_ret['ids'] = self.ids
        self.to_ret['classes'] = self.classes
        self.to_ret['type'] = self.type
        self.to_ret['value'] = self.value
        self.to_ret['hrefs'] = self.hrefs 
        self.to_ret['srcs'] = self.srcs 
        self.to_ret['others'] = self.others 
        return self.to_ret
    

def list_similarity(list1, list2):

    try:
        res = len(set(list1) & set(list2)) / float(len(set(list1) | set(list2))) * 100
        return res
    except:
        return 0


def edit_distance(cozam1, cozam2):
    """
    classical lavenstein distance - edit distance algo 
    """

    s1 = cozam1
    s2 = cozam2
    n = len(s1)
    m = len(s2)
    dp = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(n+1):
        dp[0][i] = i
    for i in range(m+1):
        dp[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    ans = dp[m][n]
    return ans


def calculate_similarity_coeff(cozam_fst, cozam_sec):
    """
    Runs the standard min-edit distance algo and returns a % of similarity 
    between tokenised version of both codes
    """
    #print(cozam_fst, cozam_sec)
    len_fst = len(cozam_fst)
    len_sec = len(cozam_sec)
    min_ed = edit_distance(cozam_fst, cozam_sec)
    base = max(len_fst, len_sec)
    similarity_coeffecient = (float(base - min_ed)/float(base)) * 100
    return round(similarity_coeffecient, 2) 


def remove_css(code):
    """
    as the name describes, it removes the css part from html code
    """
    final_code = code
    if '<style>' in code:
        removal_start = code.find('<style>')
        removal_end = code.find('</style>') + len('</style>')
        final_code = code[:removal_start] + code[removal_end:] 
    return final_code


def get_code(file_name, extension, student1_repo):
    url = student1_repo
    repo = g.get_repo(url)
    print("how you doiin")
    print(repo)
    sub_url = file_name + extension
    try:
        contents = repo.get_contents(sub_url)
        s_code = contents.decoded_content.decode()
    except:
        pprint("Error here")
        return -1
    return s_code

## Just fill the list with student github file links, filename, extension and the work will be done 
#
STUDENTS_GITHUB = ["mahesh_fw14_576", "shoaib_fw14_157","tejaswini_fw14_688","megha_fw14_307","nikhil_fw14_698", "alok_fw14_018"]
#,“masai-course/tarasish_fw14_482”]FILENAME = "getPayment"
from .models import RecordHtml
from blog.models import Report
from blog.forms import ReportForm
from blog.views import get_particular_code

def get_report(request):
    form = ReportForm()
    print("before")
    if request.method == 'GET':
        form = ReportForm(request.GET)	
        context = {'form':form}
        return render(request, 'app/index.html', context)
    form = ReportForm(request.POST)	
    print(form['unit'].value())
    cohort=form['cohort_id'].value()
    unit=form['unit'].value()
    sprint=form['sprint'].value()
    filename=form['filename'].value()
    extension=form['extension'].value()
    s='SELECT id from blog_report where cohort_id="'+cohort+'" and unit='+str(unit)+' and sprint='+str(sprint)+' and filename="'+filename+'"and extension="'+extension+'"'
    id= Report.objects.raw(s)
   # print(id[0].id)
    try:
        x=id[0]
    except:
        return HttpResponse("no record found")
    
    s='select id,student_1,student_2,similarity_code,similarity_ids,similarity_classes,similarity_content,similarity_type,similarity_value,similatity_hrefs,similarity_others from account_recordhtml where report_id='+str(id[0].id)
    records=RecordHtml.objects.raw(s)
    #return HttpResponse(records)
    unit_slug = 'unit-' + str(unit) + '/'
    sprint_slug = 'sprint-' + str(sprint) + '/'
    sub_url = unit_slug + sprint_slug + 'evaluation/' + filename + '.' + extension
    
    return render(request,'app/all_list.html',{'records':records,'sub_url':sub_url})



def generate_report(request):
    form = ReportForm()
    print("before")
    if request.method == 'GET':
        form = ReportForm(request.GET)	
        context = {'form':form}
        return render(request, 'app/index.html', context)
    form = ReportForm(request.POST)	
    print(form['unit'].value())
    cohort=form['cohort_id'].value()
    unit=form['unit'].value()
    sprint=form['sprint'].value()
    filename=form['filename'].value()
    extension=form['extension'].value()
    s='SELECT id from blog_report where cohort_id="'+form['cohort_id'].value()+'" and unit='+str(form['unit'].value())+' and sprint='+str(form['sprint'].value())+' and filename="'+form['filename'].value()+'"and extension="'+form['extension'].value()+'"'
    
    id= Report.objects.raw(s)
    
     #   s="YOur request is being processed try after 2 hours"
    try:
        x=id[0]
        return HttpResponse("Record already exist")
    except:
        
        print('emty')
        report=Report(cohort_id=cohort,unit=unit,sprint=sprint,filename=filename,extension=extension)
        report.save()
        s='SELECT id from blog_report where cohort_id="'+cohort+'" and unit='+str(unit)+' and sprint='+str(sprint)+' and filename="'+filename+'"and extension="'+extension+'"'
         
        id= Report.objects.raw(s)[0]
    for i in range(len(STUDENTS_GITHUB)):
        student_1 = STUDENTS_GITHUB[i]
        parser_1 = MyHTMLParser()
        #code_1 = get_code("/unit 5/assignment/reduxthunk/index", ".html", student_1)
        code_1 = get_particular_code(student_1, unit, sprint, filename, extension)
                
        if code_1 != -1:   
            html_code_1 = remove_css(code_1)
            parser_1.feed(html_code_1)
            ids_1 = parser_1.get_token()['ids']
            token_1 = parser_1.get_token()['token']
            classes_1 = parser_1.get_token()['classes']
            content_data_1 = parser_1.get_token()['content_data']
            type_1 = parser_1.get_token()['type']
            value_1 = parser_1.get_token()['value']
            hrefs_1 = parser_1.get_token()['hrefs']
            srcs_1 = parser_1.get_token()['srcs']
            others_1 = parser_1.get_token()['others']
            for j in range(i + 1, len(STUDENTS_GITHUB)):
                student_2 = STUDENTS_GITHUB[j]
                parser_2 = MyHTMLParser()
                code_2 = get_particular_code(student_2, unit, sprint, filename, extension)
                if code_2 != -1:
                    html_code_2 = remove_css(code_2)
                    parser_2.feed(html_code_2)
                    ids_2 = parser_2.get_token()['ids']
                    token_2 = parser_2.get_token()['token']
                    classes_2 = parser_2.get_token()['classes']
                    content_data_2 = parser_2.get_token()['content_data']
                    type_2 = parser_2.get_token()['type']
                    value_2 = parser_2.get_token()['value']
                    hrefs_2 = parser_2.get_token()['hrefs']
                    srcs_2 = parser_2.get_token()['srcs']
                    others_2 = parser_2.get_token()['others']
                    similarity_code = round(calculate_similarity_coeff(token_1, token_2))
                    similarity_ids = round(list_similarity(ids_1, ids_2))
                    similarity_classes = round(list_similarity(classes_1, classes_2))
                    similarity_content = round(list_similarity(content_data_1, content_data_2))
                    similarity_type = round(list_similarity(type_1, type_2))
                    similarity_value = round(list_similarity(value_1, value_2))
                    similatity_hrefs = round(list_similarity(hrefs_1, hrefs_2))
                    similarity_srcs = round(list_similarity(srcs_1, srcs_2))
                    similarity_others = round(list_similarity(others_1, others_2))
                    record=RecordHtml(report_id=id.id,student_1=student_1,student_2=student_2,
                    similarity_code=similarity_code,similarity_ids=similarity_ids,
                    similarity_classes=similarity_classes,similarity_content=similarity_content,
                    similarity_type=similarity_type,similarity_value =similarity_value,
                    similatity_hrefs=similatity_hrefs,similarity_srcs=similarity_srcs,similarity_others=similarity_others)
                    record.save()
                else:

                    s="Mistake in fetching second code of "+' '+student_2
        else:
            s="Error in fetching first code, "+" "+ student_1
    s="Report Generated Successfully"
    return HttpResponse(s)

#generate_report(FILENAME)









from django.shortcuts import render
from django.http import HttpResponse


