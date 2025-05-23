## MAKE SURE TO CHANGE THE EMAILS AND NAMES AND PDF PATHS 😁

```python

import random
import shutil
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
  
# List of students
students = [
	'20-0042@student.gutech.edu.om', '20-0044@student.gutech.edu.om', '20-0074@student.gutech.edu.om',
	'20-0104@student.gutech.edu.om', '21-0051@student.gutech.edu.om', '21-0061@student.gutech.edu.om',
	'21-0064@student.gutech.edu.om', '21-0196@student.gutech.edu.om', '21-0225@student.gutech.edu.om',
	'21-0285@student.gutech.edu.om', '21-0292@student.gutech.edu.om', '21-0293@student.gutech.edu.om',
	'21-0294@student.gutech.edu.om', '21-0315@student.gutech.edu.om', '21-0453@student.gutech.edu.om',
	'21-0454@student.gutech.edu.om', '21-0485@student.gutech.edu.om', '21-0521@student.gutech.edu.om',
	'22-0031@student.gutech.edu.om', '22-0037@student.gutech.edu.om', '22-0038@student.gutech.edu.om',
	'22-0047@student.gutech.edu.om', '22-0050@student.gutech.edu.om', '22-0054@student.gutech.edu.om',
	'22-0064@student.gutech.edu.om', '22-0069@student.gutech.edu.om', '22-0111@student.gutech.edu.om',
	'22-0126@student.gutech.edu.om', '22-0128@student.gutech.edu.om', '22-0134@student.gutech.edu.om',
	'22-0157@student.gutech.edu.om', '22-0159@student.gutech.edu.om', '22-0169@student.gutech.edu.om',
	'22-0173@student.gutech.edu.om', '22-0193@student.gutech.edu.om', '22-0200@student.gutech.edu.om',
	'22-0214@student.gutech.edu.om', '22-0226@student.gutech.edu.om', '22-0227@student.gutech.edu.om',
	'22-0257@student.gutech.edu.om', '22-0259@student.gutech.edu.om', '22-0262@student.gutech.edu.om',
	'22-0263@student.gutech.edu.om', '22-0272@student.gutech.edu.om', '22-0278@student.gutech.edu.om',
	'22-0281@student.gutech.edu.om', '22-0284@student.gutech.edu.om', '22-0286@student.gutech.edu.om',
	'22-0287@student.gutech.edu.om', '22-0303@student.gutech.edu.om', '22-0305@student.gutech.edu.om',
	'22-0307@student.gutech.edu.om', '22-0312@student.gutech.edu.om', '22-0321@student.gutech.edu.om',
	'22-0330@student.gutech.edu.om', '22-0337@student.gutech.edu.om', '22-0341@student.gutech.edu.om',
	'22-0357@student.gutech.edu.om', '22-0361@student.gutech.edu.om', '22-0383@student.gutech.edu.om',
	'22-0410@student.gutech.edu.om', '22-0411@student.gutech.edu.om', '22-0421@student.gutech.edu.om',
	'22-0430@student.gutech.edu.om', '22-0434@student.gutech.edu.om', '22-0452@student.gutech.edu.om',
	'22-0454@student.gutech.edu.om', '22-0459@student.gutech.edu.om', '22-0464@student.gutech.edu.om',
	'22-0476@student.gutech.edu.om', '22-0479@student.gutech.edu.om', '22-0481@student.gutech.edu.om',
	'22-0487@student.gutech.edu.om', '22-0532@student.gutech.edu.om', '22-0577@student.gutech.edu.om',
	'22-0585@student.gutech.edu.om', '22-0597@student.gutech.edu.om', '22-0608@student.gutech.edu.om',
	'22-0613@student.gutech.edu.om', '22-0619@student.gutech.edu.om', '22-0624@student.gutech.edu.om',
	'22-0626@student.gutech.edu.om', '22-0645@student.gutech.edu.om', '22-0668@student.gutech.edu.om',
	'22-0674@student.gutech.edu.om', '22-0679@student.gutech.edu.om', '22-0703@student.gutech.edu.om',
	'22-0706@student.gutech.edu.om', '22-0708@student.gutech.edu.om', '22-0711@student.gutech.edu.om',
	'22-0767@student.gutech.edu.om', '22-0773@student.gutech.edu.om', '22-0795@student.gutech.edu.om',
	'22-0817@student.gutech.edu.om', '22-0818@student.gutech.edu.om', '22-0840@student.gutech.edu.om',
	'22-0869@student.gutech.edu.om', '22-0873@student.gutech.edu.om', '22-0908@student.gutech.edu.om',
	'23-0010@student.gutech.edu.om', '23-0040@student.gutech.edu.om', '23-0068@student.gutech.edu.om',
	'23-0106@student.gutech.edu.om', '23-0200@student.gutech.edu.om', '23-0359@student.gutech.edu.om',
	'23-0404@student.gutech.edu.om', '23-0540@student.gutech.edu.om', '23-0556@student.gutech.edu.om',
	'23-0630@student.gutech.edu.om', '23-0635@student.gutech.edu.om', '23-0640@student.gutech.edu.om',
	'23-0655@student.gutech.edu.om', '24-0727@student.gutech.edu.om'
]

  

names = [
	'Khalid', 'Awadh', 'Qusai', 'Mohamed', 'As\'Ad', 'Aya', 'Azhar', 'Qasi', 'Salim', 'Humaid', 'Jamil',
	'Al Raha', 'Mohammed', 'Majid', 'Ayah', 'Haifa', 'Hussain', 'Abdulrahman', 'Maraj', 'Hawraa', 'Fatma',
	'Aaisha', 'Shahad', 'Salim', 'Haitham', 'Al Haitham', 'Abdu Al Aziz', 'Sarah', 'Muaz', 'Ola', 'Riyadh',
	'Anas', 'Areen', 'Qusay', 'Tasneem', 'Aamna', 'Salim', 'Tebyan', 'Qusai', 'Basma', 'Nihad', 'Raiyan',
	'Al Zubair', 'Mohamed', 'AL Hawra', 'Salim', 'Tooba', 'Al Ayham', 'Jameela', 'Hamzah', 'Al Warith', 'Ethar',
	'Abdul Hamed', 'Noor', 'Ahmed', 'Riham', 'Haneen', 'Ahmed', 'Mohammed', 'Abdul Rahman', 'Lulua', 'Juman',
	'Abdullah', 'Salim', 'Zain', 'Ahmed', 'Ahmed', 'Ahmed', 'Aadam', 'Afnan', 'Al Azwar', 'Al Baraa', 'Al Rayan',
	'Tahlil', 'Rinad', 'Rayyan', 'Zeinab', 'Salim', 'Said', 'Salman', 'Suhail', 'Saif', 'Tariq', 'Abdullah',
	'Adnan', 'Ula', 'Fatema', 'Fatima', 'Fatma', 'Feras', 'Maryam', 'Muadh', 'Nouyar', 'Ahmed', 'Yaqeen', 'Mohammed',
	'Ameen', 'Ali', 'Ameya', 'Muthla', 'Mohammed', 'Raiya', 'Abdullah', 'Shikha', 'Ward', 'Rashid', 'Ahmed', 'Mubeen',
	'Mariam', 'Khalid', 'Wael', 'Jinan', 'Navid'
]

# List of paths to the pdfs

pdf_files = [
	'quizes/Thermodynamics Quizzes (1).pdf', 'quizes/Thermodynamics Quizzes (2).pdf',
	'quizes/Thermodynamics Quizzes (3).pdf', 'quizes/Thermodynamics Quizzes (4).pdf',
	'quizes/Thermodynamics Quizzes (5).pdf', 'quizes/Thermodynamics Quizzes (6).pdf',
	'quizes/Thermodynamics Quizzes (7).pdf', 'quizes/Thermodynamics Quizzes (8).pdf',
	'quizes/Thermodynamics Quizzes (9).pdf'
]

# Folder to save pdfs (optional)
destination_folder = 'path_to_destination_folder'

# Email server details
sender_email = "adham.osman@gutech.edu.om"
password = "Ao2708_a"

# Function to send email
def send_email(student_email, pdf_file, name):
	msg = MIMEMultipart()
	msg['From'] = sender_email
	msg['To'] = student_email
	msg['Subject'] = "Quiz Details and Instructions"
	  
	# Body of the email (plain text)
	body = f"""
Dear {name},
I hope this email finds you well.
Kindly find attached your assigned quiz.Please ensure that you solve all questions and upload your PDF solutions on Moodle.
You have one hour from 4:00 PM to 5:00 PM, late submissions will not be accepted by the system.
Kindly save your final solutions as a PDF file named in the format: {student_email[0:7]}_Quiz2Submission.pdf.
If you have any questions or require assistance, do not hesitate to reach out.
Wishing you the best of luck!
Kind regards,
Adham Osman
	"""

	# Attach the plain text body
	msg.attach(MIMEText(body, 'plain'))
	
	# Attach the pdf file
	with open(pdf_file, "rb") as f:
		attach = MIMEApplication(f.read(), _subtype="pdf")
		attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_file))
		msg.attach(attach)
	
	# Connect to Outlook's SMTP server and send the email
	with smtplib.SMTP('smtp.office365.com', 587) as server:
		server.starttls() # Secure the connection
		server.login(sender_email, password) # Log in using the email and password
		server.sendmail(sender_email, student_email, msg.as_string()) # Send email

# Randomly shuffle the PDFs
random.shuffle(pdf_files)

# Randomly assign and send PDFs
for i in range(len(students)):
	# Pick the first PDF in the shuffled list for the current student
	selected_pdf = pdf_files[i % len(pdf_files)]
	email = students[i]
	name = names[i]
	
	# Optional: save pdf to folder
	# shutil.copy(selected_pdf, os.path.join(destination_folder, f"{student}_{os.path.basename(selected_pdf)}"))
	
	# Send the PDF via email
	send_email(email, selected_pdf, name)
	
	print(f"Sent {os.path.basename(selected_pdf)} to {email}")
```