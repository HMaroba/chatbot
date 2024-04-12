import re
import random

# Define a function to generate responses
def get_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()

    # Extract information using regular expressions
    match = re.search(r'hi|hello|hey', user_input)
    if match:
        responses = ["Hi there!", "Hello!", "Hey!"]
        return random.choice(responses)
    
    match = re.search(r'thanks|bye|alright', user_input)
    if match:
        byeresponses = ["You are welcome", "See you next time"]
        return random.choice(byeresponses)
    
    match = re.search(r'what is HIV|HLV|AIDS', user_input)
    if match:
        return "HIV stands for Human Immunodeficiency Virus. It attacks the body's immune system, specifically targeting CD4 cells (T cells), which are crucial for fighting off infections. Over time, HIV can lead to AIDS (Acquired Immunodeficiency Syndrome), a condition where the immune system becomes severely compromised, leaving the body vulnerable to opportunistic infections and certain cancers. It's important to practice safe sex, get tested regularly, and seek medical treatment if you suspect you've been exposed to HIV."
    
    match = re.search(r'symptoms of AIDS|symptoms of HIV', user_input)
    if match:
        return "Common symptoms of AIDS include persistent fever, swollen lymph nodes, rapid weight loss, frequent diarrhea, night sweats, and skin rashes. However, it's important to note that not everyone with HIV will develop AIDS, and symptoms can vary widely from person to person. Early detection and treatment are crucial for managing HIV and preventing the progression to AIDS."
    
    match = re.search(r'prevention of AIDS|how to prevent HIV', user_input)
    if match:
        return "Preventing HIV/AIDS involves a combination of strategies, including practicing safe sex by using condoms consistently and correctly, limiting your number of sexual partners, and avoiding sharing needles or syringes. Additionally, getting tested for HIV regularly and seeking medical care if you are diagnosed with HIV can help prevent the spread of the virus. Education and awareness about HIV/AIDS are also important in reducing stigma and promoting healthy behaviors."
    
    match = re.search(r'treatment of HIV|management of AIDS', user_input)
    if match:
        return "Treatment for HIV/AIDS typically involves antiretroviral therapy (ART), which helps control the virus and prevent its progression to AIDS. ART involves taking a combination of medications daily to suppress the virus, boost the immune system, and reduce the risk of transmission to others. It's important to adhere to your treatment regimen, attend regular medical appointments, and monitor your health closely while living with HIV/AIDS."
    
    match = re.search(r'testing for HIV|HIV testing', user_input)
    if match:
        return "Getting tested for HIV is an essential part of prevention and early detection. HIV tests are widely available and can be done at healthcare facilities, community clinics, and testing centers. Common types of HIV tests include blood tests, oral swab tests, and rapid tests that provide results in minutes. It's important to know your HIV status and get tested regularly, especially if you are at risk of exposure."
    
    match = re.search(r'support services for HIV|HIV support', user_input)
    if match:
        return "There are various support services available for people living with HIV/AIDS, including counseling, support groups, and access to healthcare. Organizations such as HIV/AIDS advocacy groups, community health centers, and nonprofit organizations offer resources and support for individuals affected by HIV/AIDS. Additionally, mental health services and legal assistance may be available to address the unique needs of people living with HIV/AIDS."
    
    match = re.search(r'PrEP|PEP|Pre-Exposure Prophylaxis|Post-Exposure Prophylaxis', user_input)
    if match:
        return "Pre-Exposure Prophylaxis (PrEP) and Post-Exposure Prophylaxis (PEP) are preventive measures used to reduce the risk of HIV infection. PrEP involves taking a daily medication (usually a combination of tenofovir and emtricitabine) to prevent HIV transmission in individuals who are at high risk of exposure. PEP, on the other hand, involves taking antiretroviral medications within 72 hours of potential HIV exposure to prevent infection. These strategies are effective when used correctly and consistently alongside other prevention methods such as condom use and regular testing."
    
    match = re.search(r'statistics on HIV|HIV statistics', user_input)
    if match:
        return "Global statistics on HIV/AIDS show that approximately 38 million people are living with HIV worldwide, with around 1.5 million new HIV infections and 680,000 AIDS-related deaths each year. While significant progress has been made in HIV prevention and treatment efforts, there are still challenges to overcome, particularly in regions with high prevalence rates and limited access to healthcare. Continued investment in HIV/AIDS research, education, and advocacy is crucial for achieving the goal of ending the HIV/AIDS epidemic."
    
    match = re.search(r'legal rights for HIV|HIV discrimination', user_input)
    if match:
        return "People living with HIV/AIDS are protected by various legal rights and anti-discrimination laws aimed at preventing discrimination and ensuring equal access to healthcare, employment, housing, and education. These laws vary by country and jurisdiction but generally prohibit discrimination based on HIV status and provide mechanisms for recourse in cases of discrimination or human rights violations. Additionally, advocacy efforts and community mobilization play a vital role in challenging stigma and promoting the rights and dignity of people living with HIV/AIDS."
    
    match = re.search(r'what is your name', user_input)
    if match:
        return "My name is Chatbot"
    
    match = re.search(r'my name is (.+)', user_input)
    if match:
        name = match.group(1)
        responses = ["Nice to meet you, " + name + "!", "Hello, " + name + "!"]
        return random.choice(responses)
    
    match = re.search(r'joke|funny|laugh', user_input)
    if match:
        jokes = ["Why did the tomato turn red? Because it saw the salad dressing!", 
                 "Why did the chicken cross the playground? To get to the other slide!", 
                 "What do you call a bear with no teeth? A gummy bear!"]
        return random.choice(jokes)
    
    # Generate longer responses
    greetings = ['Hello!', 'Hi!', 'Hey there!', 'Howdy!', 'Greetings!']
    topics = ['weather', 'food', 'movies', 'books', 'travel', 'music']
    questions = ['How are you today?', 'What have you been up to?', 'What do you think of the ' + random.choice(topics) + '?']
    responses = ['I am a chatbot and I do not have emotions, but thank you for asking!', 
                 'I am here to assist you with your needs. How can I help you today?', 
                 'I am programmed to talk about a variety of topics, such as ' + ', '.join(topics) + '. What would you like to discuss?', 
                 'I am sorry, I did not understand your question. Could you please rephrase it?', 
                 'Interesting, tell me more about that.']
    if user_input.endswith('?'):
        return random.choice(questions)
    else:
        return random.choice(greetings) + ' ' + random.choice(responses)

# Main loop
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)
