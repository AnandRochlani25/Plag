"""
PRIMARY
this program does the most of the work - once the arguments are set (cohort, sprint eval, unit, etc) - it fetches the code of all the students of that the
batch from github and does the required task - like breaking into words, removing comments, running edit distance algo, etc. and then further creates
a csv file and saves the three parameters - student_1, student_2 and similarity of their codes
"""


# Setting up the connection

from queue import Empty
from github import Github
from pprint import pprint
import csv
# Global variables
from github import Github
from pprint import pprint
from .keywords import js_char_map, js_keyword_map

from pprint import pprint
import re

def home_page(request):
    return render(request,'app/home.html')


def remove_boilerp(code):
    """
    removes the common part present in all code to reduce useless inflation in plagiarism percentage
        - simply finds the start of boiler part code and takes entire string before it and returns     
    """
    post_removal = ""
    start_boilerp_1 = "process.stdin.resume"  
    start_boilerp_2 = "process.env.USERNAME"
    if code.find(start_boilerp_1) ==  -1 and code.find(start_boilerp_2) == -1:
        return code
    if code.find(start_boilerp_1) != -1:
        post_removal = code.split(start_boilerp_1)[0]
    else:
        post_removal = code.split(start_boilerp_2)[0]
    return post_removal


def break_in_words(code):
    """ breaks a string in sequence of individual words - vector of string \
        it does so by splitting around space 
    """
    fragments = code.split()
    return fragments



def compress_code(codex):
    """
    going through all the words present in the list of words, if that word is directly present in the dicttionary 
    then a character associated with it is included in the compressed version, otherwise there is a possibility that 
    the given string is not directly present but one of its substring can be present, for instance : var x=3; x+=2 - 
    that is a case where there was no space - such a case won't be captured, for that reason if the direct word is not
    present, all the substrings are generated and checked for its presence and then mapped to a char 
    challenges - if a variable name has some substring which is a keyword - then that will also get included
    1. should the current method be continued or
    2. instead of generating all substring and check if it's a keyword, all the keyword's presence can be checked in the word
        and the coded char added to compressed version accordingly
    """

    compressed_version = ""
    for word in codex:
        if word in js_keyword_map:
            compressed_version += js_char_map[js_keyword_map[word]]
            # print(word)
        else:
            n = len(word)
            for i in range(n):  
                for j in range(i,n):  
                    curr_substr = word[i:(j+1)]
                    # print(curr_substr)
                    if curr_substr in js_keyword_map:
                        # print(curr_substr)
                        compressed_version += js_char_map[js_keyword_map[curr_substr]]
                        # break
    return compressed_version



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




# ------- added later --------- #
def remove_comments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
    return string




def list_similarity(list1, list2):
    """
    Returns similarity percentage between elements of two lists
    """
    try:
        res = len(set(list1) & set(list2)) / float(len(set(list1) | set(list2))) * 100
        return res
    except:
        return 0




def collate_variables(broken_code):
    """
    Creates a list of all the variable names used in the code. 
    Either the variable will be present in form of var x = 2 or
    it can be present in form of var x=2 or for(let i = ), the 
    code handles all 
    """

    list_variables = []
    possible_declarations = [k for k, v in js_keyword_map.items() if v == "VARIABLE_DECLARATION"]
    for i in range(len(broken_code)):
        temp = broken_code[i]
        if '(' in broken_code[i]:
            temp = temp.split('(')[1]
        if temp in possible_declarations:
            if broken_code[i + 1].find('=') != -1:
                post_removal = broken_code[i + 1].split('=')[0]
                list_variables.append(post_removal)
            else:
                list_variables.append(broken_code[i + 1])
    list_variables = [i.lstrip().rstrip() for i in list_variables]
    return list_variables





def collate_functions(code):
    """
    Creates a dict of two important information : list of all function names
    and list of all arguments passed to function
    ISSUE : Fails to capture functions of following format
    function(product)
    """
    to_ret = {}
    list_args = []
    list_functions = []
    for i in range(len(code)):
        name_arg = ''
        if code[i : i + 8] == "function":
            j = i + 9
            while code[j] != '{':
                name_arg += code[j]
                j += 1
            # print("name_arg", name_arg)
            try:
                args = name_arg[name_arg.index('(') + len('(') : name_arg.index(')')]
                function_name = name_arg[ : name_arg.index('(')]
                all_args = args.split(',')
                all_args = [i.lstrip().rstrip() for i in all_args]
                list_args.extend(all_args)
                list_functions.append(function_name)
            except:
                print("given function syntax currently not handled")
    list_args = [i for i in list_args if i]
    list_functions = [i for i in list_functions if i]
    to_ret['list_args'] = list_args
    to_ret['list_functions'] = list_functions
    return to_ret
            





def collate_comments(code):
    """
    Creates a dictionary which has two attributes : list of all comments present in the code
    and number of lines in the code
    Following types of comments it can collate:
    1. // this is a comment
    2. //this is a comment
    3. /* this is another comment */
    """
    to_ret = {}
    num_lines = 0
    list_comments = []
    for i in range(len(code)):
        if code[i] == '/' and code[i + 1] == '/':
            comment = ''
            j = i + 2
            while code[j] != '\n':
                comment += code[j]
                j += 1
            list_comments.append(comment)
        if code[i] == '/' and code[i + 1] == '*':
            comment = ''
            j = i + 2
            while code[j] != '*' and code[j + 1] != '/':
                comment += code[j]
                j += 1
            list_comments.append(comment)
        if(code[i] == '\n'):
            num_lines += 1
    to_ret['num_lines'] = num_lines
    list_comments = [ i.lstrip().rstrip() for i in list_comments ]
    to_ret['list_comments'] = list_comments
    return to_ret


# "NOT CONFIDENT AT ALL" - 1
# "SLIGHTLY CONFIDENT" - 2
# "SOMEWHAT CONFIDENT" - 3
# "FAIRLY CONFIDENT" - 4
# "COMPLETELY CONFIDENT" - 5
TOKEN = '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'
g = Github(TOKEN)
BASE_URL = "masai-course"

#--------------------------------------------------------------------------#


def get_repo_list(cohort):
    """
    Returns a list of all repository present in a particular cohort
    Sample Use : get_cohort_repo("fw11")
    """ 
    repos = []
    cohort_name = cohort + "_"
    for repo in g.get_organization(BASE_URL).get_repos():
        if cohort_name in repo.name:
            repos.append(repo.name)
    print(repos)
    return repos



def get_js(code):
    try:
        start_point = code.find("<script>") + len("<script>")
        end_point = code.find("</script>")
    except:
        return "<script> tag is missing"
    js_code = code[start_point : end_point]
    return js_code




def get_particular_code(student_id, unit, sprint, filename, extension):
    """
    Returns code of a given student for a given unit, sprint and certain filename and extension
    """
    url = BASE_URL + '/'
    url += student_id
    repo = g.get_repo(url)
    unit_slug = 'unit-' + str(unit) + '/'
    sprint_slug = 'sprint-' + str(sprint) + '/'
    sub_url = unit_slug + sprint_slug + 'evaluation/' + filename + '.' + extension
    try:
        contents = repo.get_contents(sub_url)
    except:
        return -1
    s = contents.decoded_content.decode()
    return s

# pprint(get_particular_code("khushbu_fw11_265", 2, 4, "products", "html"))



def get_all_codes(cohort, unit, sprint, filename, extension):
    """
    gets all the codes of a particular unit, sprint for one particular cohort of students
    """
    cohort_repos = get_repo_list(cohort)
    for i in cohort_repos:
        student_id = str(i)
        pprint(get_js(get_particular_code(student_id, unit, sprint, filename, extension)))




def filter_repos(all_repos, unit, sprint, filename, extension):
    """
    Takes the list of all repository and removes those which has the filename not present
    It is to be noted that filename in appropriate case and extension should be present
    """
    to_ret = {}
    all_missing = []
    all_present = []
    for repo in all_repos:
        if(get_particular_code(str(repo), unit, sprint, filename, extension)) == -1:
            all_missing.append(repo)
        else:
            all_present.append(repo)
    to_ret['present_repos'] = all_present
    to_ret['missing_repos'] = all_missing
    return to_ret


def tokenise(code):
    """
    Cozam stands for codezam inspired from shazam
    """
    comments_removed = remove_comments(code)
    boilerp_removed = remove_boilerp(comments_removed)
    fragmented_code = break_in_words(boilerp_removed)
    cozam = compress_code(fragmented_code)
    return cozam



def calculate_similarity_coeff(cozam_fst, cozam_sec):
    """
    Runs the standard min-edit distance algo and returns a % of similarity 
    between tokenised version of both codes
    """
    print(cozam_fst)
    len_fst = len(cozam_fst)
    len_sec = len(cozam_sec)
    min_ed = edit_distance(cozam_fst, cozam_sec)
    base = max(len_fst, len_sec)
    print(base)
    similarity_coeffecient = (float(base - min_ed)/float(base)) * 100
    return round(similarity_coeffecient, 2)    

cohort = "fw10"
unit = 3
sprint = 23
filename = "scripts/checkout"
extension = "js"



from .models import Record,Report

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
    
    s='select id,student_1, student_2,similarity_coeff from blog_record where report_id='+str(id[0].id)
    records=Record.objects.raw(s)
    for record in records:
        print(record)
    return render(request,'app/show_record.html',{'records':records})

from django.shortcuts import render
from .forms import ReportForm




    
    
@staticmethod
def generate_result(request):
    
    """
    //c11,3,2,abc.html
    //c11,4,3,index.html
    
    Generates two csv reports : one with all repository where required files were not present
    the other which has all combination of students and the similarity between their codes : 3 fields

    Be careful with the name, it may overwrite existing files with same name
    """
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
        
        print('empty')
        report=Report(cohort_id=cohort,unit=unit,sprint=sprint,filename=filename,extension=extension)
        report.save()
        s='SELECT id from blog_report where cohort_id="'+cohort+'" and unit='+str(unit)+' and sprint='+str(sprint)+' and filename="'+filename+'"and extension="'+extension+'"'
         
        id= Report.objects.raw(s)[0]
    #report.object.create(cohort,unit,sprint,filename,extension)
        
        cohort_repos = get_repo_list(cohort)
    # cohort_repos = ['ankit_fw10_011', 'sonam_nj2_113', 'bicky_fw10_069', 'neeraj_fw10_110', 'akhil_fw10_030', 'krishna_fw10_133', 'deevanshu_fw10_194']
        filtered_repo = filter_repos(cohort_repos, unit, sprint, filename, extension)
        print(filtered_repo)
        present_repos = filtered_repo['present_repos']
        #present_repos = ['pd_demo_3','pd_demo_2','pd_demo_1']
        missing_repos = filtered_repo['missing_repos']
    # # pprint(missing_repos)
        fieldnames_missing = ['student_code']
        fieldnames_similarity = ['student_1', 'student_2', 'similarity_percentage']
        with open('missed_files_1.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames_missing)
            writer.writeheader()
            for repo in missing_repos:
                writer.writerow({'student_code': repo})
        with open('similarity_files_2.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames_similarity)
            writer.writeheader()
            for i in range(len(present_repos)):
                student_1 = str(present_repos[i])
                code_1 = get_particular_code(student_1, unit, sprint, filename, extension)
                print('code')
                print(code_1)
                js_code_1 = get_js(code_1)
                print('JsCode')
                print(js_code_1)
                tokenised_code_1 = tokenise(code_1)
                for j in range(i, len(present_repos)):
                    student_2 = str(present_repos[j])
                    code_2 = get_particular_code(student_2, unit, sprint, filename, extension)
                    js_code_2 = get_js(code_2)
                    tokenised_code_2 = tokenise(code_2)
                    similarity_coeff = calculate_similarity_coeff(tokenised_code_1, tokenised_code_2)
                    record=Record(report_id=id.id,student_1=student_1,student_2=student_2,similarity_coeff=similarity_coeff)
                    record.save()
                    print("s")
                    writer.writerow({'student_1': student_1, 'student_2': student_2, 'similarity_percentage': similarity_coeff})
                    pprint(student_1 + ' | ' + student_2 + ' -> ' + str(similarity_coeff))
        return HttpResponse("Report submitted successfully")
    


    
        
    
    


from django.http import HttpResponse


# Update following variables as per the requirements


#get_repo_list(cohort)
#generate_result()


# ==================== EXPERIMENTS & CODE SNIPPETS =======================#

"""
 SO code for finding all subfolders withing a repo

from github import Github
g = Github()
repo = g.get_repo("PyGithub/PyGithub")
contents = repo.get_contents("github")
while len(contents)>0:
  file_content = contents.pop(0)
  if file_content.type=='dir':
    contents.extend(repo.get_contents(file_content.path))
  else :
    print(file_content)
"""
#Autoincremented primary key
#String cohortId
