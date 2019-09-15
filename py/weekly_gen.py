##Usage : python3 weekly_gen.py 20190728
import sys
file_name = str(sys.argv[1])

def issue_insert(container, content1, content2, input_file):
    """Insert issue html code in main issue page"""
    with open(input_file, 'r+') as issue_file:
        lines = issue_file.readlines()
        for line in lines:
            if line.strip().startswith(container):
                #print(line)
                i = (lines.index(line))
                lines.insert(i+1, content1)
                lines.insert(i+2, content2)
                #print(lines[i+1])
        issue_file.seek(0)
        issue_file.writelines(lines)

with open(file_name+".txt", "r") as f:
    data = f.readlines()
 
    for line in data:
        if line[0] == "#":
            print ("<p class=\"style1\" style=\"margin: 0px; padding: 0px; color: #000000; font-size: 28px; font-family: Helvetica, Arial, sans-serif;\">"+line[1:]+"<br></p>")
        else:
            words = line.split('|')
            print ("<p>"+words[0]+" <a href=\""+words[1]+"\" rel=\"nofollow\">"+words[1][:42]+"...</a></p><p><br></p>")

#print("""
#<div class="row center"><a href="http://www.deepmerlingweekly.com/issues/"""+file_name+""".html" id="download-button" 
#class="btn-large waves-effect waves-light yellow darken-2">"""+file_name[6:8]+"-"+file_name[4:6]+"-"+file_name[0:4]+"""</a></div>
#""")

issue_file = '../issues/issues2.html'
container = '<div class="row center" id="issue_container">'
content1 = '\n<div class="row center"><a href="http://www.deepmerlingweekly.com/issues/'+file_name+'.html" id="download-button"\n'
content2 = 'class="btn-large waves-effect waves-light yellow darken-2">'+file_name[6:8]+"-"+file_name[4:6]+"-"+file_name[0:4]+'</a></div>\n'
issue_insert(container, content1, content2, issue_file)


#######
data_string="edizione del " + file_name[6:8]+"-"+file_name[4:6]+"-"+file_name[0:4]
with open(file_name+".txt", "r") as f:
    data = f.readlines()
    with open("../issues/"+file_name+".html", "w") as myfile:
        myfile.write("""<!DOCTYPE html> <html lang=\"en\"> <head>   
        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"/>   
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1.0\"/>   
        <title>DeepMerlingWeekly.com</title>    
        <!-- CSS  -->
        <link href=\"https://fonts.googleapis.com/icon?family=Material+Icons\" rel=\"stylesheet\">
        <link href=\"css/materialize.css\" type=\"text/css\" rel=\"stylesheet\" media=\"screen,projection\"/>
        <link href=\"css/style.css\" type=\"text/css\" rel=\"stylesheet\" media=\"screen,projection\"/>
        </head><body>
        <nav class="blue lighten-1" role="navigation">
        <div class="nav-wrapper container">
          <!-- <a id="logo-container" href="#" class="brand-logo">Logo che manca</a> -->
        <ul class="right hide-on-med-and-down">
        <li><a href="http://www.deepmerlingweekly.com">Home</a></li>
        <li><a href="http://www.deepmerlingweekly.com/issues/issues.html">Issues</a></li>
        <li><a href="http://www.deepmerlingweekly.com/subscribe.html" id="download-button" class="btn waves-effect waves-light yellow darken-2">Subscribe!</a></li>
        </ul>
        </div>
        </nav>
        <h5 class=\"header col s12 light\">"""+data_string+"""</h5>
        </div>
        <div class=\"row center\">""")
        myfile.write("<div class=\"collection\">")
        for line in data:
            if line[0] == "#":
                myfile.write("<a href=\"#!\" class=\"collection-item\">"+line[1:]+"</a>")
            else:
                words = line.split('|')
                myfile.write("<p>"+words[0]+" <a href=\""+words[1]+"\" rel=\"nofollow\">"+words[1][:42]+"...</a></p><p><br></p>")
        myfile.write("</div>")
        myfile.write("""</div>
      <br><br>

    </div>
  </div>

    </div>
    <br><br>
  </div>

  <footer class=\"page-footer yellow darken-2\">
    <div class=\"container\">
      <div class=\"row\">
        <div class=\"col l6 s12\">
          <h5 class=\"white-text\">Company Bio</h5>
          <p class=\"grey-text text-lighten-4\">Nata per scherzo, in crescita costante, si spera non muoia</p>


        </div>
        <!-- <div class=\"col l3 s12\">
          <h5 class=\"white-text\">Settings</h5>
          <ul>
            <li><a class=\"white-text\" href=\"#!\">Link 1</a></li>
            <li><a class=\"white-text\" href=\"#!\">Link 2</a></li>
            <li><a class=\"white-text\" href=\"#!\">Link 3</a></li>
            <li><a class=\"white-text\" href=\"#!\">Link 4</a></li>
          </ul>
        </div>
        <div class=\"col l3 s12\">
          <h5 class=\"white-text\">Connect</h5>
          <ul>
            <li><a class=\"white-text\" href=\"#!\">Link 1</a></li>
            <li><a class=\"white-text\" href=\"#!\">Link 2</a></li>
            <li><a class=\"white-text\" href=\"#!\">Link 3</a></li>
            <li><a class=\"white-text\" href=\"#!\">Link 4</a></li>
          </ul>
        </div>-->
      </div>
    </div>
    <div class=\"footer-copyright\">
      <div class=\"container\">
      Made by <a class=\"yellow-text text-lighten-3\" href=\"http://materializecss.com\">Materialize</a>
      </div>
    </div>
  </footer>


  <!--  Scripts-->
  <script src=\"https://code.jquery.com/jquery-2.1.1.min.js\"></script>
  <script src=\"js/materialize.js\"></script>
  <script src=\"js/init.js\"></script>

  </body>
</html>""")