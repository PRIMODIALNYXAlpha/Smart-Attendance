import smtplib
from email.mime.text import MIMEText

def send_email(to_email, name):
    sender_email = "valhalla3641@gmail.com"
    password = "rdkocuatnietdyic"

    # HTML Email Content
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">

            <h2 style="color: #2E86C1; text-align: center;">📸 Smart Attendance System</h2>

            <p style="font-size: 16px;">Hello <b>{name}</b>,</p>

            <p style="font-size: 15px;">
                Your attendance has been <span style="color: green; font-weight: bold;">successfully marked</span>.
            </p>

            <table style="width: 100%; margin-top: 15px; border-collapse: collapse;">
                <tr>
                    <td style="padding: 10px; border: 1px solid #ddd;"><b>Status</b></td>
                    <td style="padding: 10px; border: 1px solid #ddd; color: green;">Present ✅</td>
                </tr>
            </table>

            <p style="margin-top: 20px; font-size: 14px;">
                Thank you for using the Smart Attendance System.
            </p>

            <hr style="margin-top: 20px;">

            <p style="font-size: 12px; color: gray; text-align: center;">
                This is an automated email. Please do not reply.
            </p>
        </div>
    </body>
    </html>
    """

    msg = MIMEText(html_content, "html")
    msg['Subject'] = "✅ Attendance Confirmed"
    msg['From'] = sender_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)