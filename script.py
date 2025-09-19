from pywebio.input import select
from pywebio.input import input, FLOAT, TEXT
from pywebio.output import put_text, put_html, put_markdown, put_table, put_image, clear
import base64
import time



def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()
    

def body_temp(body_temp, name, age, gender, pulse_rate, Resp_rate, systolic, diastolic):

    #Body Temperature Section
    put_markdown(f"### **Body Temperature**")
    put_html("<hr>")
    put_text("The normal body temperature of a person varies depending on gender, recent activity, food and fluid consumption, " \
    "time of day, and, in women, the stage of the menstrual cycle. Normal body temperature can range from 97.8 degrees F "
    "(or Fahrenheit, equivalent to 36.5 degrees C, or Celsius) to 99 degrees F (37.2 degrees C) for a healthy adult. ")

    put_html("<br>")
    put_table([
        ["Temperature", "Adults (F)", "Children (F)"],
        ["Lower Then Average", "≤ 96.62 F ", "≤ 97.52 F"],
        ["Normal", "96.8 - 98.6 F", "97.7 - 99.5 F"],
        ["Higher Then Average", "98.78 - 100.4 F", "99.5 - 101.12 F"],
        ["Fever", "100.58 - 107.96 F", "101.3 - 107.96 F"]
    ])

    put_html("<br>")


    if  (96.8 <= body_temp <= 98.6 and age >= 18):
        put_text(f"{name} you're body temperature is {body_temp} F and your {age} years old. This is considered Normal for your age.")

    elif (body_temp <= 96.62 and age >= 18):
        put_text(f"{name} you're body temperature is {body_temp} F and your {age} years old. This is considered lower then average for your age.")

    elif (98.78 <= body_temp <= 100.4 and age >= 18):
        put_text(f"{name} you're body temperature is {body_temp} F and your {age} years old. This is considered higher then average for your age.")

    elif (100.58 <= body_temp <= 107.96 and age >= 18):
        put_text(f"{name} you're body temperature is {body_temp} F and your {age} years old. Having an temperature in this range is considered an fever and you should seek medical attention.")




    elif (97.7 <= body_temp <= 99.5 and age < 18):
        put_text(f"{name}, you're body temperature is {body_temp} F and your {age} years old. This is considered Normal for your age.")

    elif (body_temp <= 97.52 and age < 18):
        put_text(f"{name} you're body temperature is {body_temp} F and your {age} years old. This is considered lower then average for your age.")

    elif (99.5 <= body_temp <= 101.12 and age < 18):
        put_text(f"{name} you're body temperature is {body_temp} F and your {age} years old. This is considered higher then average for your age.")

    elif (101.3 <= body_temp <= 107.96 and age < 18):
        put_text(f"{name} you're body temperature is {body_temp} F and your {age} years old. Having an temperature in this range is considered an fever and you should seek medical attention.")

    put_html("""
<p>Body temperature is a measure of how well your body can make and get rid of heat. The body is very good at keeping its temperature within a safe range, even when temperatures outside the body change a lot.</p>
<ul>
  <li>When you are too hot, the blood vessels in your skin widen to carry the excess heat to your skin's surface. You may start to sweat. As the sweat evaporates, it helps cool your body.</li>
  <li>When you are too cold, your blood vessels narrow. This reduces blood flow to your skin to save body heat. You may start to shiver. When the muscles tremble this way, it helps to make more heat.</li>
</ul>
""")
    



#Pulse Rate Section

    put_markdown(f"### **Pulse Rate**")
    put_html("<hr>")
    put_text("The pulse rate is a measurement of the heart rate, or the number of times the heart beats per minute. As the heart pushes " \
    "blood through the arteries, the arteries expand and contract with the flow of the blood. The normal pulse for healthy adults ranges " \
    "from 60 to 100 beats per minute. The pulse rate may fluctuate and increase with exercise, illness, injury, and emotions. Females ages " \
    "12 and older, in general, tend to have faster heart rates than do males. Athletes, such as runners, who do a lot of cardiovascular " \
    "conditioning, may have heart rates near 40 beats per minute and experience no problems.")

    put_html("<br>")
    put_table([
        ["Age", "Men", "Women"],
        ["18-25", "62-73 bpm", "64-80 bpm"],
        ["26-35", "62-73 bpm", "64-81 bpm"],
        ["36-45", "63-75 bpm", "65-82 bpm"],
        ["46-55", "64-76 bpm", "66-83 bpm"],
        ["56-65", "62-75 bpm", "64-82 bpm"],
        ["Over 65", "62-73 bpm", "64-81 bpm"]
    ])

    put_html("<br>")


    if  ( ((18 <= age <= 25) and (62 <= pulse_rate <= 73) and (gender == "Male")) or ((18 <= age <= 25) and (64 <= pulse_rate <= 80) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is considered an healthy amount for your age and gender")

    elif  ( ((26 <= age <= 35) and (62 <= pulse_rate <= 73) and (gender == "Male")) or ((26 <= age <= 35) and (64 <= pulse_rate <= 81) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is considered an healthy amount for your age and gender")

    elif  ( ((36 <= age <= 45) and (63 <= pulse_rate <= 75) and (gender == "Male")) or ((36 <= age <= 45) and (65 <= pulse_rate <= 82) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is considered an healthy amount for your age and gender")

    elif  ( ((46 <= age <= 55) and (64 <= pulse_rate <= 76) and (gender == "Male")) or ((46 <= age <= 55) and (66 <= pulse_rate <= 83) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is considered an healthy amount for your age and gender")

    elif  ( ((56 <= age <= 65) and (62 <= pulse_rate <= 75) and (gender == "Male")) or ((56 <= age <= 65) and (64 <= pulse_rate <= 82) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is considered an healthy amount for your age and gender")

    elif  ( ((age > 65) and (62 <= pulse_rate <= 73) and (gender == "Male")) or ((age > 65) and (64 <= pulse_rate <= 81) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is considered an healthy amount for your age and gender")


    
    elif  ( ((18 <= age <= 25) and (pulse_rate > 73 or pulse_rate < 62) and (gender == "Male")) or ((18 <= age <= 25) and (pulse_rate > 80 or pulse_rate < 64) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    elif  ( ((26 <= age <= 35) and (pulse_rate > 73 or pulse_rate < 62) and (gender == "Male")) or ((26 <= age <= 35) and (pulse_rate > 81 or pulse_rate < 64) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    elif  ( ((36 <= age <= 45) and (pulse_rate > 75 or pulse_rate < 63) and (gender == "Male")) or ((36 <= age <= 45) and (pulse_rate > 82 or pulse_rate < 65) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    elif  ( ((46 <= age <= 55) and (pulse_rate > 76 or pulse_rate < 64) and (gender == "Male")) or ((46 <= age <= 55) and (pulse_rate > 83 or pulse_rate < 66) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")
    
    elif  ( ((56 <= age <= 65) and (pulse_rate > 75 or pulse_rate < 62) and (gender == "Male")) or ((56 <= age <= 65) and (pulse_rate > 81 or pulse_rate < 64) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    elif  ( ((age > 65) and (pulse_rate > 73 or pulse_rate < 62) and (gender == "Male")) or ((age > 65) and (pulse_rate > 81 or pulse_rate < 64) and (gender == "Female")) ):
        put_text(f"{name} you're pulse rate is {pulse_rate} bpm and you're an {age} year old {gender}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    
    put_html("""
<p>Your pulse rate reflects the work your heart is doing to pump blood throughout your body.</p>
<ul>
  <li>Normal Range: For a healthy adult at rest, a pulse rate of 60 to 100 bpm is normal.</li>
  <li>Tachycardia: A resting heart rate over 100 bpm is called tachycardia. </li>
    <li>Bradycardia: A resting heart rate under 60 bpm is called bradycardia.  </li>
</ul>
             
<p>While 80-90 bpm is typically normal, consult a healthcare provider if you experience: </p>
<ul>
  <li>A resting heart rate that is consistently above 100 bpm (tachycardia) or below 60 bpm (bradycardia), especially if you are not an athlete.</li>
<li>Dizziness or fainting. </li>
<li>Shortness of breath. </li>
<li>Fatigue or chest discomfort. </li>
<li>A significant and consistent increase in your usual resting heart rate. </li>
</ul>
             


""")
    



#Respiration Rate Section

    put_markdown(f"### **Respiration Rate**")
    put_html("<hr>")
    put_text("Your respiratory rate, or your breathing rate, is the number of breaths you take per minute. The normal respiratory rate for an adult at rest is 12 to 18 breaths per minute. A respiration rate under 12 or over 25 breaths per minute while resting may be a sign of an underlying health condition.")

    put_html("<br>")
    put_table([
        ['Age Range', 'Respiration Rate (bpm)'],
        ['Less than 1 year', '30–40'],
        ['1–2 years', '25–35'],
        ['3–5 years', '25–30'],
        ['6–12 years', '20–25'],
        ['13+ years', '12–20'],
    ])

    put_html("<br>")


    if  ( ((age < 1) and (30 <= Resp_rate <= 40)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an healthy amount for your age.")

    elif ( ((1 <= age <= 2) and (25 <= Resp_rate <= 35)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an healthy amount for your age.")

    elif ( ((3 <= age <= 5) and (25 <= Resp_rate <= 30)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an healthy amount for your age.")

    elif ( ((6 <= age <= 12) and (20 <= Resp_rate <= 25)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an healthy amount for your age.")

    elif ( ((13 <= age) and (12 <= Resp_rate <= 20)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an healthy amount for your age.")
    
    
    elif ( ((age < 1) and (Resp_rate < 30 or Resp_rate > 40)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an unhealthy amount for your age. Consider seeking medical help.")

    elif ( ((1 <= age <= 2) and (Resp_rate < 25 or Resp_rate > 35)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an unhealthy amount for your age. Consider seeking medical help.")

    elif ( ((3 <= age <= 5) and (Resp_rate < 25 or Resp_rate > 30)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an unhealthy amount for your age. Consider seeking medical help.")

    elif ( ((6 <= age <= 12) and (Resp_rate < 20 or Resp_rate > 25)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an unhealthy amount for your age. Consider seeking medical help.")

    elif ( ((13 <= age) and (Resp_rate < 12 or Resp_rate > 20)) ):
        put_text(f"{name} you're respiration Rate is {Resp_rate} bpm and you're {age} years old. This is considered an unhealthy amount for your age. Consider seeking medical help.")



    put_html("""
<p>Health conditions that can affect your respiratory rate include, but aren’t limited to, the following:</p>
<ul>
  <li>Asthma</li>
  <li>Anxiety</li>
    <li>Pneumonia</li>
    <li>Heart disease</li>
    <li>Lung disease</li>
    <li>Substance use disorder</li>
</ul>

""")
    
    


#Blood Pressure Section

    put_markdown(f"### **Respiration Rate**")
    put_html("<hr>")
    put_text("Blood pressure is a measurement of the force of blood against the walls of your arteries. It is typically expressed as two numbers: ")

    put_html("""     
    <ul>
  <li>Systolic pressure: The upper number, which represents the pressure in your arteries when your heart beats. </li>
  <li>Diastolic pressure: The lower number, which represents the pressure in your arteries when your heart rests between beats. </li>
         
</ul><br>""")
         
    put_table([
        ['Blood Pressure Category', 'Systolic (mm Hg)', 'Diastolic (mm Hg)'],
        ["Healthy", "Less than 120", "and less than 180"],
        ["Elevated", "120-129", "and less than 80"],
        ["Stage 1 hypertension", "130-139", "or 80 to 89"],
        ["Stage 2 hypertension", "140 or higher", "or 90 or higher"],
        ["Hypertension crisis", "Over 180", "or over 120"],
    ])

    put_html("<br>")

    if (systolic < 120 and diastolic < 180):
        put_text(f"{name} you're blood pressure is {systolic}/{diastolic} mmHg. This is considered an normal amount. Maintain or adopt a healthy lifestyle.")
    elif (120 < systolic < 129) and (diastolic < 80):
        put_text(f"{name} you're blood pressure is {systolic}/{diastolic} mmHg. This is considered an elevated amount. Maintain or adopt a healthy lifestyle.")
    elif (130 < systolic < 139) or (80 < diastolic < 89):
        put_text(f"{name} you're blood pressure is {systolic}/{diastolic} mmHg. This is considered stage 1 hypertension. Maintain or adopt a healthy lifestyle. Talk to a healthcare professional about taking one or more medicines.")
    elif (systolic >= 140) or (diastolic >= 90):
        put_text(f"{name} you're blood pressure is {systolic}/{diastolic} mmHg. This is considered stage 2 hypertension. Maintain or adopt a healthy lifestyle. Talk to a healthcare professional about taking more than one medicine.")
    elif (systolic >= 180) or (diastolic >= 120):
        put_text(f"{name} you're blood pressure is {systolic}/{diastolic} mmHg. This is considered Hypertension crisis. Please seek immediate medical attention as this is a life-threatening situation.")



    put_html("""
<p>Symptoms from high blood pressure don’t usually occur until it causes serious health problems. About 1 in 3 U.S. adults with high blood pressure aren’t even aware they have it and are not being treated to control their blood pressure. That’s why it is important to have your blood pressure checked at least once a year. Regular monitoring using home blood pressure is also recommended.</p>
             
            <br>
<p>To control or lower high blood pressure, your healthcare provider may recommend that you adopt a heart-healthy lifestyle that includes:</p>


<ul>
  <li>Choosing a heart-healthy dietary pattern and foods such as those in the DASH eating plan, the Dietary Guidelines for Americans, or the Mediterranean eating pattern</li>
  <li>Being physically active and reducing sedentary behavior</li>
    <li>Losing weight for people with overweight or obesity</li>
    <li>Quitting smoking</li>
    <li>Reducing stress</li>
    <li>Getting enough good-quality sleep</li>
</ul>

""")




"""
def pulse_rate(pulse, n, a, sex):
    put_markdown(f"### **Pulse Rate**")
    put_html("<hr>")
    put_text("The pulse rate is a measurement of the heart rate, or the number of times the heart beats per minute. As the heart pushes " \
    "blood through the arteries, the arteries expand and contract with the flow of the blood. The normal pulse for healthy adults ranges " \
    "from 60 to 100 beats per minute. The pulse rate may fluctuate and increase with exercise, illness, injury, and emotions. Females ages " \
    "12 and older, in general, tend to have faster heart rates than do males. Athletes, such as runners, who do a lot of cardiovascular " \
    "conditioning, may have heart rates near 40 beats per minute and experience no problems.")

    put_html("<br>")
    put_table([
        ["Age", "Men", "Women"],
        ["18-25", "62-73 bpm", "64-80 bpm"],
        ["26-35", "62-73 bpm", "64-81 bpm"],
        ["36-45", "63-75 bpm", "65-82 bpm"],
        ["46-55", "64-76 bpm", "66-83 bpm"],
        ["56-65", "62-75 bpm", "64-82 bpm"],
        ["Over 65", "62-73 bpm", "64-81 bpm"]
    ])

    put_html("<br>")


    if  ( ((18 <= a <= 25) and (62 <= pulse <= 73) and (sex == "Male")) or ((18 <= a <= 25) and (64 <= pulse <= 80) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is considered an healthy amount for your age and gender")

    elif  ( ((26 <= a <= 35) and (62 <= pulse <= 73) and (sex == "Male")) or ((26 <= a <= 35) and (64 <= pulse <= 81) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is considered an healthy amount for your age and gender")

    elif  ( ((36 <= a <= 45) and (63 <= pulse <= 75) and (sex == "Male")) or ((36 <= a <= 45) and (65 <= pulse <= 82) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is considered an healthy amount for your age and gender")

    elif  ( ((46 <= a <= 55) and (64 <= pulse <= 76) and (sex == "Male")) or ((46 <= a <= 55) and (66 <= pulse <= 83) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is considered an healthy amount for your age and gender")

    elif  ( ((56 <= a <= 65) and (62 <= pulse <= 75) and (sex == "Male")) or ((56 <= a <= 65) and (64 <= pulse <= 82) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is considered an healthy amount for your age and gender")

    elif  ( ((a > 65) and (62 <= pulse <= 73) and (sex == "Male")) or ((a > 65) and (64 <= pulse <= 81) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is considered an healthy amount for your age and gender")


    
    elif  ( ((18 <= a <= 25) and (pulse > 73 or pulse < 62) and (sex == "Male")) or ((18 <= a <= 25) and (pulse > 80 or pulse < 64) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    elif  ( ((26 <= a <= 35) and (pulse > 73 or pulse < 62) and (sex == "Male")) or ((26 <= a <= 35) and (pulse > 81 or pulse < 64) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    elif  ( ((36 <= a <= 45) and (pulse > 75 or pulse < 63) and (sex == "Male")) or ((36 <= a <= 45) and (pulse > 82 or pulse < 65) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    elif  ( ((46 <= a <= 55) and (pulse > 76 or pulse < 64) and (sex == "Male")) or ((46 <= a <= 55) and (pulse > 83 or pulse < 66) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")
    
    elif  ( ((56 <= a <= 65) and (pulse > 75 or pulse < 62) and (sex == "Male")) or ((56 <= a <= 65) and (pulse > 81 or pulse < 64) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    elif  ( ((a > 65) and (pulse > 73 or pulse < 62) and (sex == "Male")) or ((a > 65) and (pulse > 81 or pulse < 64) and (sex == "Female")) ):
        put_text(f"{n} you're pulse rate is {pulse} bpm and you're an {a} year old {sex}. This is not considered an healthy amount for your age and gender. You should seek medical help from an professional")

    
    put_html(
<p>Body temperature is a measure of how well your body can make and get rid of heat. The body is very good at keeping its temperature within a safe range, even when temperatures outside the body change a lot.</p>
<ul>
  <li>When you are too hot, the blood vessels in your skin widen to carry the excess heat to your skin's surface. You may start to sweat. As the sweat evaporates, it helps cool your body.</li>
  <li>When you are too cold, your blood vessels narrow. This reduces blood flow to your skin to save body heat. You may start to shiver. When the muscles tremble this way, it helps to make more heat.</li>
</ul>
)


"""
    

def vitals():


    put_html("""
        <style>
            body {
                background-image: url("https://static.vecteezy.com/system/resources/previews/025/871/386/non_2x/blue-medical-health-abstract-background-with-plus-sign-template-design-with-concept-and-idea-for-healthcare-technology-innovation-medicine-health-science-and-research-vector.jpg");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
        </style>
    """)

    put_markdown('# **An Comphrensive Guide to Understanding Your Vitals**')
    
    # Dictionary of slide title and image paths
    slides = [
        ("Chart", "Normal.png"),
        ("Doctors", "doctors.jpg"),
        ("Vitals Machine", "vitals_machine.png")
    ]

    # Preload base64 image data
    image_data = [(title, load_image_base64(path)) for title, path in slides]

    # Loop through slides
    for title, data in image_data:
        put_html(f'<img src="data:image/png;base64,{data}" width="1000">')
        time.sleep(1.75)  # Wait 3 seconds before showing next slide


    name = input("What's your name：", type=TEXT)

    gender = select("What's your gender：", ['Male', 'Female'])

    age = input("What's your age：", type=FLOAT)

    body_temperature = input("Your Body Temperature(F)：", type=FLOAT)

    pulse_rate = input("Number of beats per minute:", type=FLOAT)

    respiration_rate = input("Number of breaths per minute", type=FLOAT)

    systolic_pressure = input("Number of pressure inside the artery when the heart contracts and pumps blood through the body(mm)", type=FLOAT)

    diastolic_pressure = input("Number of pressure inside the artery when the heart is at rest and is filling with blood(mm)", type=FLOAT)


    put_html("<br><br>")
    put_markdown(f"### **{name}'s Vitals**")
    put_html("<hr>")
    put_text("Body Temperature: ",  (body_temperature), "F")
    put_html("<br>")
    put_text("Pulse Rate: ",  (pulse_rate), "Beats per minute")
    put_html("<br>")
    put_text("Respiration Rate: ",  (respiration_rate), "Breaths per minute")
    put_html("<br>")
    put_text("Blood Pressure: ",  (systolic_pressure), "/", (diastolic_pressure), "mm Hg")
    put_html("<br>")


    

        
    body_temp(body_temperature, name, age, gender, pulse_rate, respiration_rate, systolic_pressure, diastolic_pressure)

   


if __name__ == '__main__':
    vitals()