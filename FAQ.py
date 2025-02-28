# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SfcEXI9qDO7HEEdONUxf0GtUlt-Y5aKB
"""

!pip install scrapy

import scrapy

!pip install chatterbot chatterbot_corpus

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.sqlite3')
cursor = conn.cursor()

# Create a table for storing questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS qa_pairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Commit and close connection
conn.commit()
conn.close()

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.sqlite3')
cursor = conn.cursor()

# List of question-answer pairs to insert into the database
qa_pairs = [
    ("What is UC doing in response to the college admissions fraud investigation?",
     "UC initiated a comprehensive, systemwide audit as soon as we became aware of individuals exploiting the admissions process across universities nationwide. This audit by Ethics, Compliance and Audit Services (ECAS) — the independent audit and investigative arm of UC that reports directly to the University of California Board of Regents — is helping guide significant enhancements to our admissions procedures. Additionally, UC is continuing to collaborate closely with federal and state authorities on any ongoing investigations. We will stay proactive, transparent and accountable — and keep the public, the UC community and others apprised of our steadfast efforts in this matter."),
    ("Does UC give preference to students whose family members attended UC?",
     "No. As a public institution, and according to long-established UC admissions policy, we do not grant preferential admission to the children of alumni or donors."),
    ("Do donations to UC affect a student’s chances for admission?",
     "No, we prohibit this practice per our longstanding UC Board of Regents policy: 'Admissions motivated by concern for financial, political or other such benefit to the University do not have a place in the admissions process.' As a public institution, and according to long-established UC admissions policy, we do not grant preferential admission to the children of alumni or donors."),
    ("What happens to students who were admitted under false pretenses?","Current UC practices dictate that all applicants abide by the Statement of Integrity. If a student is alleged to have falsified information in their application, the student will undergo a thorough review. Under university policy, failure of a student to submit accurate information will jeopardize consideration for admission to UC for the current or any future terms. UC has taken, and will continue to take, appropriate action in response to substantiated admissions fraud. This includes revocation of admission. The Family Education Rights and Privacy Act (FERPA) is a federal law that protects the privacy of student education records, and prohibits the university from discussing any individual student’s academic standing or any investigations. UC is not permitted to disclose the identity of any students involved in the admissions fraud investigation, nor discuss actions or decisions involving a specific student."
),
 ("What happens if UC staff or faculty are implicated in the federal investigation, or any other?","We impose appropriate discipline for all individuals found culpable. UC will take appropriate action if any of our employees are implicated in the admissions investigation. Any individual involved will undergo a thorough review, which could result in disciplinary action, including dismissal, if allegations are substantiated."
),
    ("How does the athletic recruitment process work?","Student-athletes submit the same admission application and receive a comprehensive review like all other students. The same general standards for admission developed by the campus Academic Senate committees are applied to both student-athletes and the general applicant pool. Student-athletes undergo additional consideration by faculty and admissions staff to ensure they will be able to succeed academically and graduate in a timely manner."
),(
    "Is UC getting rid of its admissions requirement for standardized testing?","In July 2018, President Napolitano requested that UC’s Academic Senate conduct a formal review based on factual, historical data to determine whether SAT and ACT tests are useful measures of academic performance for the admissions process. The Senate has since established a Task Force and the university is currently waiting for the assessment and recommendations from this group before UC determines whether any steps should be taken on this important issue."
),
    ("How do you ensure that students are not lying on their application?","Current UC practices dictate that all applicants abide by the Statement of Integrity. We verify the accuracy of a student’s academic record with certified transcripts and test score reports. We also select random applications from the applicant pool each year for verification of applicants’ activities and achievements outside of the classroom through requests for documentation. We understand that not every process is perfect. We are constantly reviewing our current practices, and always looking for ways to improve them."
),
    (
        "The recent national investigation raised concerns that the college admissions processes nationwide generally limit access to students with fewer resources or means. What is UC doing to provide for those students?","UC is committed to a fair and transparent admissions process that is based on student merit and achievement and represents a level playing field for every applicant. UC attracts the best and brightest and prides itself in being a university of trailblazers, admitting thousands of students seeking to be the first in their families to attend a UC or earn a degree. In fact, over 40 percent of UC undergraduates will be the first generation in their family to graduate from college, and UC educates more first-generation students than other institutions of its caliber. Nearly half of UC first-generation students are African American, Latino/Chicano, or American Indian, and 39 percent speak English as their second language. Additionally, the university offers one of the nation’s strongest financial aid programs, awarding $1.64 billion in university financial aid to students, and 57 percent of California undergraduates have their tuition fully covered. In recent years, UC resident tuition and fees as well as total costs have remained relatively flat, as UC works to maintain its ongoing commitment to keeping college affordable. The university also works to engage future students through our early outreach programs, designed to prepare disadvantaged K-12 Californian students for higher education. These programs strive to make college and the application process less daunting, and currently UC has over 1,400 K-12 school partnerships, which help 70 percent of their participants go on to college. UC plays a role in the education of millions of California K-12 students, whether or not they are UC-bound."
    ),
    ("How will UC prevent these problems from happening again?","Our investigation of possible wrongdoing will not only help us find any improper or illegal activity, but may identify gaps in our processes that need to be addressed. Our own diligent efforts, and the outcome of investigations by law-enforcement agencies, will help ensure that these activities are prevented in the future. In addition, the University of California has identified clear and concrete steps that will improve the entire admissions process through our internal audit that included an exhaustive review of campus practices."
),
    ("How does “Admission by Exception” work?","The Admission by Exception policy allows a UC campus to consider an applicant who falls short of the minimum admission requirements, but is otherwise competitive and has shown the potential to succeed academically. This designation is typically reserved for students with non-traditional educational backgrounds, such as homeschooled students or students from rural or extraordinarily disadvantaged circumstances, or students with special talents, including athletic ability, who have demonstrated that they can succeed academically at UC. Campuses use this policy very sparingly, with such students comprising approximately 2 percent of newly enrolled students systemwide."
),
    ("How do you make sure that students don’t cheat on their tests?","Standardized tests are administered by the testing agency, not UC, and scores are sent from the testing agency directly to the university. If the administration of an exam or the integrity of a score is compromised, the testing agency cancels the score and does not release the scores to the university. In the event scores have been released and subsequently invalidated by the ACT or College Board, the agency notifies the university that such action was taken. Appropriate action is taken by the university which may include denial of admission, withdrawal of an offer of admission, or registration cancellation. The ACT has provided additional information here, while the College Board, which administers the SAT, has provided information here."
),
    ("What are your admissions policies? Do the recent revelations and charges in the admissions fraud investigation change them?","We share the outrage and concerns over fraudulent activity to try to gain admission at public and private universities across the nation, including, in a few instances, at UC. As the preeminent public higher education institution, we hold ourselves to the highest standards, so we are taking proactive steps to strengthen our admissions practices and procedures to protect the integrity of the UC admissions process. UC is committed to a fair and transparent admissions process that is based on student merit and achievement. Current UC practices dictate that all applicants abide by the Statement of Integrity. We verify the accuracy of a student’s academic record with certified transcripts and test score reports. We also select random applications from the applicant pool each year for verification of applicants’ activities and achievements outside of the classroom through requests for documentation. The university has a comprehensive admissions process, and as a public, land-grant institution, takes pride in its commitment to prioritizing the enrollment of California residents, consistent with the California Master Plan for Higher Education. In accordance with Regents Policy 2109, California residents represent a minimum of 82 percent of all undergraduate students. Students are admitted based on UC’s comprehensive review of their applications, as we consider multiple factors of achievement in the context of the opportunities available to them and their demonstrated potential to contribute to the intellectual and cultural life at UC. Also, as a public institution, and according to long-established UC admissions policy, we do not grant preferential admission to the children of alumni or donors. While we believe the current UC admissions process is effective and has established safeguards in place, ECAS will be implementing a number of improvements and enhancements to continue to improve and refine our admissions. Our goal is to provide an admissions process that represents a fair and level playing field for all those who apply, and one that employs the strongest defenses and controls against those who attempt to inappropriately, illegally or unethically influence the outcomes and decisions of UC admissions. Students get in to UC through their intellect, achievements, hard work and passion. We’ve admitted, educated and supported millions of students from all walks of life since UC opened its doors more than 150 years ago, and that remains our central mission."
)
]

# Insert data into the table
cursor.executemany('''
INSERT INTO qa_pairs (question, answer)
VALUES (?, ?)
''', qa_pairs)

# Commit and close connection
conn.commit()
conn.close()

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.sqlite3')
cursor = conn.cursor()

# Query to retrieve all question-answer pairs
cursor.execute('SELECT * FROM qa_pairs')

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print out each row
for row in rows:
    print(f"ID: {row[0]}")
    print(f"Question: {row[1]}")
    print(f"Answer: {row[2]}")
    print()

# Close the connection
conn.close()

!pip install --upgrade pip

!pip install pyyaml

!sudo apt-get install build-essential

!pip install chatterbot==1.0.5

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot(
    'AdmissionsBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='/content/database.sqlite3'# path to the database
)

# Training with the provided questions and answers
conversation = [
    "What is UC doing in response to the college admissions fraud investigation?",
    "UC initiated a comprehensive, systemwide audit as soon as we became aware of individuals exploiting the admissions process across universities nationwide. This audit by Ethics, Compliance and Audit Services (ECAS) — the independent audit and investigative arm of UC that reports directly to the University of California Board of Regents — is helping guide significant enhancements to our admissions procedures. Additionally, UC is continuing to collaborate closely with federal and state authorities on any ongoing investigations. We will stay proactive, transparent and accountable — and keep the public, the UC community and others apprised of our steadfast efforts in this matter.",
    "Does UC give preference to students whose family members attended UC?",
    "No. As a public institution, and according to long-established UC admissions policy, we do not grant preferential admission to the children of alumni or donors.",
    "Do donations to UC affect a student’s chances for admission?",
    "No, we prohibit this practice per our longstanding UC Board of Regents policy: 'Admissions motivated by concern for financial, political or other such benefit to the University do not have a place in the admissions process.' As a public institution, and according to long-established UC admissions policy, we do not grant preferential admission to the children of alumni or donors.",
    "What happens to students who were admitted under false pretenses?",
    "Current UC practices dictate that all applicants abide by the Statement of Integrity. If a student is alleged to have falsified information in their application, the student will undergo a thorough review. Under university policy, failure of a student to submit accurate information will jeopardize consideration for admission to UC for the current or any future terms. UC has taken, and will continue to take, appropriate action in response to substantiated admissions fraud. This includes revocation of admission. The Family Education Rights and Privacy Act (FERPA) is a federal law that protects the privacy of student education records, and prohibits the university from discussing any individual student’s academic standing or any investigations. UC is not permitted to disclose the identity of any students involved in the admissions fraud investigation, nor discuss actions or decisions involving a specific student.",
    "What happens if UC staff or faculty are implicated in the federal investigation, or any other?",
    "We impose appropriate discipline for all individuals found culpable. UC will take appropriate action if any of our employees are implicated in the admissions investigation. Any individual involved will undergo a thorough review, which could result in disciplinary action, including dismissal, if allegations are substantiated.",
    "How does the athletic recruitment process work?",
    "Student-athletes submit the same admission application and receive a comprehensive review like all other students. The same general standards for admission developed by the campus Academic Senate committees are applied to both student-athletes and the general applicant pool. Student-athletes undergo additional consideration by faculty and admissions staff to ensure they will be able to succeed academically and graduate in a timely manner.",
    "Is UC getting rid of its admissions requirement for standardized testing?",
    "In July 2018, President Napolitano requested that UC’s Academic Senate conduct a formal review based on factual, historical data to determine whether SAT and ACT tests are useful measures of academic performance for the admissions process. The Senate has since established a Task Force and the university is currently waiting for the assessment and recommendations from this group before UC determines whether any steps should be taken on this important issue.",
    "How do you ensure that students are not lying on their application?",
    "Current UC practices dictate that all applicants abide by the Statement of Integrity. We verify the accuracy of a student’s academic record with certified transcripts and test score reports. We also select random applications from the applicant pool each year for verification of applicants’ activities and achievements outside of the classroom through requests for documentation. We understand that not every process is perfect. We are constantly reviewing our current practices, and always looking for ways to improve them.",
    "The recent national investigation raised concerns that the college admissions processes nationwide generally limit access to students with fewer resources or means. What is UC doing to provide for those students?",
    "UC is committed to a fair and transparent admissions process that is based on student merit and achievement and represents a level playing field for every applicant. UC attracts the best and brightest and prides itself in being a university of trailblazers, admitting thousands of students seeking to be the first in their families to attend a UC or earn a degree. In fact, over 40 percent of UC undergraduates will be the first generation in their family to graduate from college, and UC educates more first-generation students than other institutions of its caliber. Nearly half of UC first-generation students are African American, Latino/Chicano, or American Indian, and 39 percent speak English as their second language. Additionally, the university offers one of the nation’s strongest financial aid programs, awarding $1.64 billion in university financial aid to students, and 57 percent of California undergraduates have their tuition fully covered. In recent years, UC resident tuition and fees as well as total costs have remained relatively flat, as UC works to maintain its ongoing commitment to keeping college affordable. The university also works to engage future students through our early outreach programs, designed to prepare disadvantaged K-12 Californian students for higher education. These programs strive to make college and the application process less daunting, and currently UC has over 1,400 K-12 school partnerships, which help 70 percent of their participants go on to college. UC plays"
]

from chatterbot.trainers import ListTrainer

# Create a new instance of the ListTrainer
trainer = ListTrainer(chatbot)

# Train the chatbot with the predefined conversation
trainer.train(conversation)

# Context dictionary to hold conversation state
context = {'topic': 'general'}

def update_context(user_input):
    """
    Update the context based on user input.
    """
    global context
    user_input_lower = user_input.lower()

    if 'admissions' in user_input_lower:
        context['topic'] = 'admissions'
    elif 'donations' in user_input_lower:
        context['topic'] = 'donations'
    else:
        context['topic'] = 'general'

def generate_response(user_input):
    """
    Generate a response from the chatbot and modify it based on context.
    """
    global context
    response = chatbot.get_response(user_input)

    if context['topic'] == 'admissions':
        return "Regarding admissions: " + str(response)
    elif context['topic'] == 'donations':
        return "About donations: " + str(response)
    else:
        return str(response)

def chat_with_bot():
    print("Hello! I am AdmissionsBot. Ask me anything about admissions.")
    while True:
        try:
            # Get user input
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            # Update context based on user input
            update_context(user_input)

            # Get and print the chatbot's response
            response = generate_response(user_input)
            print(f"AdmissionsBot: {response}")

        except KeyboardInterrupt:
            print("Goodbye!")
            break

if __name__ == "__main__":
    chat_with_bot()