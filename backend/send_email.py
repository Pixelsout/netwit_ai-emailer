from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, TrackingSettings, ClickTracking, OpenTracking
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, subject, html_content):
    try:
        from_email = 'valenkurai92@gmail.com'
        reply_to = 'valenkurai92@gmail.com'

        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content,
        )
        message.reply_to = Email(reply_to)

        # ✅ Enable open and click tracking
        tracking_settings = TrackingSettings()
        tracking_settings.click_tracking = ClickTracking(enable=True, enable_text=True)
        tracking_settings.open_tracking = OpenTracking(enable=True)
        message.tracking_settings = tracking_settings

        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)

        return "sent" if response.status_code < 300 else "failed"

    except Exception as e:
        return f"failed: {str(e)}"
