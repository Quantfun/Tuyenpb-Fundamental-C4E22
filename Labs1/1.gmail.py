from gmail import GMail, Message
from random import choice

gmail=GMail("audit.kvas@gmail.com","AUDIT@12345")
html_template= '''
<p>Hello,</p>
<p><span style="color: #0000ff;"><strong>Today is a {{description}} day.&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></strong></span></p>
'''
des_list = ["nice","rainny","hot"]
html_content = html_template.replace("{{descrption}}",choice(des_list))
msg=Message("Python demo-Gmail", to="tuyencpa@gmail.com",html=html_content)
gmail.send(msg)

#Random reason and sympton