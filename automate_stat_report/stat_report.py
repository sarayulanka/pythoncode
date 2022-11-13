import pandas
import docx

csvfile1 = "automate_statusreport.csv"

def statReport(csv_file):
    data = pandas.read_csv(csv_file)
    doc = docx.Document()
    doc.save('automate.docx')
    for index, row in data.iterrows():
        para = doc.add_paragraph(f'Participated in a {row["Meeting title"]} meeting on {row["Meeting Date"]}. {row["meeting organizer"]} organized the meeting. Attendees include {row["Workers needed"]}. The purpose of the meeting is to {row["Reason"]}. \n')
        para.style = 'Arrow Bullet'
        doc.save('automate.docx')

statReport(csvfile1)