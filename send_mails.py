import smtplib
import pandas as pd
import csv
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email import encoders

sender_email = "devscript.community@gmail.com"
sender_name = "DevScript Community"
password = "Dev*2020"

form = pd.read_csv("leela.csv")
receiver_emails = form['receiver_emails'].values
receiver_names = form["receiver_names"].values

for receiver_email, receiver_name in zip(receiver_emails, receiver_names):        
        
        print("Sending to " + receiver_name)
        msg = MIMEMultipart()
        msg['Subject'] = 'Mindshift vs Careershift || DevScript'
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = formataddr((receiver_name, receiver_email))

        msg.attach(MIMEText("""<h2>Hello, """ + receiver_name + """</h2>

<p>Greetings from Team DevScript!</p>

<p>Thanks for taking part in the session on "MINDSHIFT VS CAREERSHIFT" organized by DevScript in association with Microsoft Learn Student Ambassadors, on 4th October, 2020.</p>

<p>On behalf of the community, I would like to take the opportunity to express my sincere gratitude to all participants for making their precious time available for the session. The program was indeed a collaborative work and without your support and words of encouragement, our success would not have been possible.</p>

<p>We really look forward for conducting many more sessions like this again.</p>

<p>Your certificate of participation is attached in this email. Kindly share your achievement on LinkedIn, and do not forget to tag our Community! 
<br>Use <a style="cursor:pointer; color:blue;">#devscript</a></p>

<p>Follow us on LinkedIn for more opportunities.</p>

<ul>
<li><a href= 'https://www.linkedin.com/company/devscripts/'>LinkedIn</a></li>
</ul>

 <p>For getting more updates about our technical sessions, Please subscribe to our YouTube channel.</p>
<ul>
<li><a href= 'https://www.youtube.com/channel/UCQWgtNSqWGu_PJFQqAiCSNw'>YouTube Channel</a></li>
</ul>

<p>STAY TUNED!!</p>

<p>Regards, <br>
Team DevScript</p>
                           """, 'html'))




        filename = receiver_name + ".pdf"
        #filename = "Additional_Resources.rar"

        try:
            with open(filename, "rb") as attachment:
                            part = MIMEBase("application", "octet-stream")
                            part.set_payload(attachment.read())

            encoders.encode_base64(part)
            part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
            )

            msg.attach(part)
        except Exception as e:
                print(f'Oh no! We didnt found the attachment!\n{e}')
                break

        try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                context = ssl.create_default_context()
                server.starttls(context=context)
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
                print('Email sent!')
        except Exception as e:
                print(f'Oh no! Something bad happened!\n{e}')
                break
        finally:
                #print('Closing the server...')
                server.quit()