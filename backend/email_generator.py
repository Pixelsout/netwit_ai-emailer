def generate_email_html(full_name, company, insights):
    return f"""
    <html>
    <body style="font-family:sans-serif; padding:20px;">
        <p>Hi {full_name},</p>
        <p>I came across <strong>{company}</strong> and was impressed with what you’re doing.</p>
        <p>{insights}</p>
        <p>Let me know if you'd be open to a quick chat!</p>

        <a href="https://netwit.ca/demo"
           style="display:inline-block; margin:10px 0; padding:10px 20px; background-color:#007BFF;
                  color:#fff; text-decoration:none; border-radius:5px;">
           📅 Book a Demo
        </a>

        <p>Best,<br>Dave Chatpar<br>NetWit AI</p>
    </body>
    </html>
    """
