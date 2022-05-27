# All mapping is with respect to Javascript

js_keyword_map = {
    "const" : "VARIABLE_DECLARATION",
    "let" : "VARIABLE_DECLARATION",
    "var" : "VARIABLE_DECLARATION",
    "if" : "CONDITIONAL_IF",
    "else" : "CONDITIONAL_ELSE",
    "for" : "FOR_LOOP",
    "while" : "WHILE_LOOP",
    "function" : "FUNCTION",
    # "." : "BUILT_IN",
    "++" : "VARIABLE_UPDATE",
    "+=" : "VARIABLE_UPDATE",
    "-=" : "VARIABLE_UPDATE",
    "*=" : "VARIABLE_UPDATE",
    "/=" : "VARIABLE_UPDATE",
    "<" : "COMPARATOR",
    "<=" : "COMPARATOR",
    ">" : "COMPARATOR",
    ">=" : "COMPARATOR",
    "!=" :  "COMPARATOR",
    "!==" : "COMPARATOR",
    "===" : "COMPARATOR",
    "==" :  "COMPARATOR",
    "return" : "RETURN",
    "console.log" : "PRINT",
    "break" : "BREAK",
    "[" : "ARRAY_INDEX",
    "case" : "CASE",
    "continue" : "CONTINUE",
    "switch" : "SWITCH",
    "class" : "CLASS",
    "default" : "DEFAULT",
    "delete" : "DELETE",
    "export" : "EXPORT",
    "extends" : "EXTENDS",
    "typeof" : "TYPE",
    "this" : "THIS",
    "new" : "NEW",
    ".prototype" : "PROTOTYPE",
    "await" : "AWAIT",
    "async" : "ASYNC",
    "append" : "APPEND",
    "constructor(" : "CONSTRUCTOR",
    ".then(" : "THEN",
    ".addEventListener" : "ADD_EVENT",
    ".createElement" : "CREATE_ELEMENT",
    ".querySelector" : "QUERY_SELECTOR",
    ".querySelectorAll" : "QUERY_SELECTORALL",
    ".getElementById" : "GET_ELEMENT",
    ".getElementByClassNames" : "GET_ELEMENT",
    ".onclick" : "ON_CLICK",
    ".innerHTML" : "INNER_ELEM",
    ".innerText" : "INNER_ELEM",
    "alert(" : "ALERT",
    "appendChild" : "APPEND",
    ".textContent" : "INNER_ELEM",
    ".value" : "VALUE",
    ".preventDefault" : "PREVENT_DEFAULT",
    ".removeChild" : "REMOVE_CHILD",
    ".insertBefore" : "INSERTION",
    "onClick" : "ON_CLICK",
    "onclick" : "ON_CLICK",
    "onmouse" : "MOUSE_EVENT",
    "onkey" : "KEY_EVENT",
    "onMouse" : "MOUSE_EVENT",
    "onKey" : "KEY_EVENT",    
    ".setAttribute" : "SET_ATTRIBUTE",
    ".getAttribute" : "GET_ATTRIBUTE",
    ".removeAttribute" : "REMOVE_ATTRIBUTE",
    ".style." : "STYLING",
    ".removeEventListener" : "REMOVE_EVENT",
    "document." : "DOCUMENT",
    "getElementsByClassName" : "GET_ELEMENT",
    "getElementsByTagName" : "GET_ELEMENT",
    ".floor(" : "ROUNDING",
    ".ceil(" : "ROUNDING",
    ".round(" : "ROUNDING",
    "Number(" : "TYPE_CASTING",
    "parseFloat(" : "TYPE_CASTING",
    "parseInt(" : "TYPE_CASTING",
    "String(" : "TYPE_CASTING",
    ".toString(" : "TYPE_CASTING",
    ".create(" : "CREATE",
    ".assign(" : "ASSIGN",
    ".map(" : "MAP",
    ".filter(" : "FILTER",
    ".trim(" : "TRIM",
    ".split(" : "SPLIT",
    ".reduce(" : "REDUCE",
    ".sort(" : "SORT",
    ".find(" : "FIND",
    ".findIndex(" : "FIND_INDEX",
    ".includes(" : "INCLUDES",
    ".indexOf(" : "INDEX_OF",
    ".join(" : "JOIN",
    ".substring(" : "SUBSTRING",
    ".shift(" : "SHIFT",
    ".unshift(" : "UNSHIFT",
    ".pop(" : "POP",
    ".push(" : "PUSH",
    ".reverse(" : "REVERSE",
    ".slice(" : "SLICE",
    ".splice(" : "SPLICE",
    ".forEach(" : "FOR_EACH",
    "window." : "WINDOW",
    "JSON.parse(" : "JSONPARSE",
    "JSON.stringify(" : "JSONSTRINGIFY",
    "localStorage.setItem(" : "LOCALSTORAGE",
}
# X, ] are not used yet
js_char_map = {
    "VARIABLE_DECLARATION" : "A",
    "CONDITIONAL_IF" : "B",
    "CONDITIONAL_ELSE" : "C",
    "FOR_LOOP" : "D",
    "WHILE_LOOP" : "E",
    "FUNCTION" : "F",
    "CASE" : "G",
    "VARIABLE_UPDATE" : "H",
    "RETURN" : "I",
    "PRINT" : "J",
    "CONTINUE" : "K",
    "BREAK" : "L",
    "ARRAY_INDEX" : "M",
    "MAP" : "N",
    "FILTER" : "O",
    "TRIM" : "P",
    "SPLIT" : "Q",
    "REDUCE" : "R",
    "SORT" : "S",
    "FIND" : "T",
    "FIND_INDEX" : "U",
    "INCLUDES" : "V",
    "INDEX_OF" : "W",
    "COMPARATOR" : "X",
    "JOIN" : "Y",
    "SUBSTRING" : "Z",
    "SHIFT" : "0",
    "UNSHIFT" : "1",
    "POP" : "2",
    "PUSH" : "3",
    "REVERSE" : "4",
    "SLICE" : "5",
    "SPLICE" : "6",
    "FOR_EACH" : "7",
    "SWITCH" : "8",
    "CLASS" : "9",
    "DEFAULT" : "a",
    "AWAIT" : "b",
    "ASYNC" : "c",
    "APPEND" : "d",
    "CONSTRUCTOR" : "e",
    "THEN" : "f",
    "ADDEVENT" : "g",
    "CREATEELEMENT" : "h",
    "QUERYSELECTOR" : "i",
    "QUERYSELECTORALL" : "j",
    "GETELEMENT" : "k",
    "GETELEMENT" : "l",
    "ONCLICK" : "m",
    "INNERELEM" : "n",
    "INNERELEM" : "o",
    "ALERT" : "p",
    "APPEND" : "q",
    "INNERELEM" : "r",
    "VALUE" : "s",
    "PREVENTDEFAULT" : "t",
    "ROUNDING" : "u",
    "TYPECASTING" : "v",
    "EXTENDS" : "w",
    "JSONPARSE" : "x",
    "EXPORT" : "y",
    "NEW" : "z",
    "PROTOTYPE" : "!",
    "QUERY_SELECTORALL" : "@", 
    "GET_ELEMENT" : "#",
    "CREATE" : "$",
    "INNER_ELEM" : "%",
    "KEY_EVENT" : "^",
    "REMOVE_CHILD" : "&",
    "INSERTION" : "*",
    "DOCUMENT" : "(",
    "ASSIGN" : ")",
    "JSONSTRINGIFY" : "-", 
    "GET_ATTRIBUTE" : "_",
    "STYLING" : "=",
    "LOCALSTORAGE" : "+", 
    "REMOVE_ATTRIBUTE" : ":",
    "PREVENT_DEFAULT" : ";",
    "THIS" : "’",
    "TYPE_CASTING" : "/", 
    "ON_CLICK" : "<",
    "SET_ATTRIBUTE" : ">", 
    "WINDOW" : ".",
    "MOUSE_EVENT" : ",",
    "REMOVE_EVENT" : "~",
    "DELETE" : "`",
    "TYPE" : "?",
    "ADD_EVENT" : "{",
    "QUERY_SELECTOR" : "}", 
    "CREATE_ELEMENT" : "[",
}

html_open_map = {
    "DOCTYPE" : "A",
    "html" : "B",
    "a" : "C",
    "b" : "D",
    "body" : "E",
    "br" : "F",
    "button" : "G",
    "div" : "H",
    "form" : "I",
    "h1" : "J",
    "h2" : "J",
    "h3" : "J",
    "h4" : "J",
    "h5" : "J",
    "h6" : "J",
    "head" : "K",
    "hr" : "L",
    "img" : "M",
    "input" : "N",
    "label" : "O",
    "li" : "P",
    "link" : "Q",
    "meta" : "R",
    "option" : "S",
    "p" : "T",
    "script" : "U",
    "select" : "V",
    "small" : "W",
    "span" : "X",
    "style" : "Y",
    "table" : "Z",
    "tbody" : "1",
    "td" : "2",
    "textarea" : "3",
    "tfoot" : "4",
    "th" : "5",
    "thead" : "6",
    "title" : "7",
    "tr" : "8",
    "u" : "9",
    "ul" : "0",
    "main" : "!"
}

html_close_map = {
    "html" : "a",
    "a" : "b",
    "b" : "c",
    "body" : "d",
    "br" : "e",
    "button" : "f",
    "div" : "g",
    "form" : "h",
    "h1" : "i",
    "h2" : "i",
    "h3" : "i",
    "h4" : "i",
    "h5" : "i",
    "h6" : "i",
    "head" : "o",
    "hr" : "p",
    "img" : "q",
    "input" : "r",
    "label" : "s",
    "li" : "t",
    "link" : "u",
    "meta" : "v",
    "option" : "w",
    "p" : "x",
    "script" : "y",
    "select" : "z",
    "small" : "j",
    "span" : "k",
    "style" : "l",
    "table" : "m",
    "tbody" : "n",
    "td" : "!",
    "textarea" : "@",
    "tfoot" : "#",
    "th" : "$",
    "thead" : "%",
    "title" : "^",
    "tr" : "&",
    "u" : "(",
    "ul" : ")",
    "main" : "-"
}


# following to check which all values from js_keyword_map is not encoded yet
keyword_set = set()
for k in js_keyword_map:
    value = js_keyword_map[k]
    keyword_set.add(value)

char_set = set()
for k in js_char_map:
    char_set.add(k)


char_set_encoding = set()
for k in js_char_map:
    char_set_encoding.add(js_char_map[k])



# as long as following prints 0, it means all correctly encoded with a char

# print(len(keyword_set - char_set))
# print(len(char_set_encoding) - len(char_set))

# # if the length is not 0, following elements haven’t been encoded yet
# print(keyword_set - char_set)