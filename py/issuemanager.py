"""Insert new issue page in main page
"""
#pylint: disable=W0223

def issue_insert(container, content1, content2, input_file):
    """Insert issue html code in main issue page"""
    with open(input_file, 'r+') as issue_file:
        lines = issue_file.readlines()
        for line in lines:
            if line.strip().startswith(container):
                print(line)
                i = (lines.index(line))
                lines.insert(i+1, content1)
                lines.insert(i+2, content2)
                print(lines[i+1])
                #fh.seek(0)
        issue_file.seek(0)
        issue_file.writelines(lines)

def main():
    """Main"""
    issue_file = './issues/issues2.html'
    container = '<div class="row center" id="issue_container">'
    content1 = '\n<div class="row center"><a href="http://www.deepmerlingweekly.com/issues/20190803.html" id="download-button"\n'
    content2 = 'class="btn-large waves-effect waves-light yellow darken-2">03-08-2019</a></div>\n'
    issue_insert(container, content1, content2, issue_file)

main()
