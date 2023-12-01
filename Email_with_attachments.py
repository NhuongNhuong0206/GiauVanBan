
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# thiết lập port và server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# địa chỉ email của mình
email_from = "trannguyentrungtin.work2@gmail.com"
# một danh sách các địa chỉ mail cần gửi file.
email_list = ["1951012139tin@ou.edu.vn"]

# Mật khẩu ứng dụng/ app password là từ khóa tìm kiếm trong mục quản lý gmail . tạo một app sẽ có mật khẩu này, tương  ứng với  email. một gmail có thể tạo nhiều app.
pswd = "vohbaiuwriproxkp"


# Ghi tiêu  đề email cần gửi đến người nhận 
subject = "An toàn hệ thống thông tin" #


def send_emails(email_list):

    for person in email_list:

        # Nôị dung văn bản muốn gửi đến người nhận
        body = f"""
        Bên dưới là file mã hóa cần gửi đi đến người nhận có địa chỉ email!
        etc
        """

    
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        
        msg.attach(MIMEText(body, 'plain'))

        # Định nghĩa một file để gửi
        filename = "random_data.csv"

        attachment= open(filename, 'rb')  # r for read and b for binary

        # Encode as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()


        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    TIE_server.quit()


# Run the function
send_emails(email_list)




        





