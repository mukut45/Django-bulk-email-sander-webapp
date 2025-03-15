from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages
import os

def send_bulk_email(request):
    if request.method == 'POST':
        recipients = request.POST.get('recipients', '').split(',')
        subject = request.POST.get('subject', '')
        message = request.POST.get('body', '')
        from_email = "mukutdutta45@icloud.com"

        # Handle file upload
        uploaded_file = request.FILES.get('attachment')  # Get the uploaded file

        try:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=[],  # Keep empty for privacy
                bcc=recipients  # Send to BCC to hide email addresses
            )

            # Attach the file (if provided)
            if uploaded_file:
                email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)

            email.send(fail_silently=False)

            # Save to Sent Items Log
            with open("sent_emails_log.txt", "a") as log_file:
                log_file.write(f"To: {recipients}, Subject: {subject}\n")

            messages.success(request, "Emails sent successfully!")
            return redirect('sent_items')  # Redirect to Sent Items page

        except Exception as e:
            messages.error(request, f"Error sending emails: {str(e)}")

    return render(request, 'send_email.html')

def sent_items(request):
    sent_emails = []

    # Read the log file and display the sent emails
    if os.path.exists("sent_emails_log.txt"):
        with open("sent_emails_log.txt", "r") as log_file:
            sent_emails = log_file.readlines()

    return render(request, 'sent_items.html', {'sent_emails': sent_emails})
