from threading import Thread
import subprocess
import logging

import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def run(tests_file, report_file):
    logging.info(f"Run pytest -v {tests_file} --html={report_file}")
    subprocess.run(["pytest", "-v", tests_file, f"--html={report_file}"])


thread1 = Thread(target=run, args=('test_api.py', 'reportapi.html'))
thread2 = Thread(target=run, args=('test_ui_neg.py', 'reportuineg.html'))
thread3 = Thread(target=run, args=('test_ui_pos.py', 'reportuipos.html'))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

# fromaddr = ""
# toaddr = ""
# mypass = ""
# reports = ["reportapi.html", "reportuineg.html", "reportuipos.html"]
#
# logging.info(f"Sending email to {toaddr} from {fromaddr}")
#
# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Отчет о тестировании"
#
# for report in reports:
#     with open(report, "rb") as f:
#         part = MIMEApplication(f.read(), Name=basename(report))
#         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(report)
#         msg.attach(part)
#
# body = "Тесты завершены"
# msg.attach(MIMEText(body, 'plain'))
#
# server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
# server.login(fromaddr, mypass)
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()

logging.info("Bye bye")
