import json
import requests
import argparse
import time


def req(text):
    data = json.dumps({'text': text})
    start_time = time.time()
    res = requests.post("http://127.0.0.1:5010/", data=data)
    end_time = time.time()
    print(res.text)
    print("Response time:", end_time-start_time)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    description = 'This is the server for OpenAI.'
    parser = argparse.ArgumentParser(description=description)
    # Add long and short argument
    parser.add_argument("--sentence", "-s", help="Input text")
    args = parser.parse_args()
    if not args.sentence:
        # sentence = "A quale argomento appartiene la frase 'ieri la mia amica mi ha offesa mentre parlavamo di cinema perché non abbiamo gli stessi gusti' tra person-public person-medical staff-nurse, person-public person-medical staff-doctor, person-public person-medical staff-psychologist, person-public person-medical staff-social worker. Se secondo te nessuno è sufficientemente adeguato, rispondi None."
        # sentence = "Tell me which is the most appropriate topic for the sentence 'mi piace molto mangiare un dessert inglese per colazione' among the following: cooking-english breakfast food, going to the restaurant-english breakfast food, having breakfast-english breakfast food. If none is appropriate, answer None."
        # sentence = "Tell me which is the most appropriate topic for the sentence 'questo letto nella stanza di ospedale è scomodo, preferirei andare a comprare del cibo alle macchinette.' between the following:" \
        #            "Hospital-HOSPITALBEDROOM," \
        #            "Hospital-HOSPITALROUNDABOUTAREA," \
        #            "Hospital-HOSPITALGYM," \
        #            "Hospital-HOSPITALPOOL," \
        #            "Hospital-HOSPITALSHAREDBATHROOM," \
        #            "Hospital-HOSPITALCOMMONDININGROOM, Hospital-HOSPITALCOFFEEMACHINEARE"
        # sentence = "Tell me which is the most appropriate topic for the sentence 'adoro il mio vibratore' among the following: Kitchenware, other house object, personal care, furniture, appliance, decoration."
        # sentence = "Your task is to tell me which are (if any) the most appropriate topics for the sentence: 'quando mangio il panettone sono felice'. If you think that there are no topics that can be associated to this sentence, just answer 'None'."

        client_sentence = "I want to talk about my town"
        possible_sentence_topic_str = "dogs, town, food"
        curr_speaker_name = "Lucrezia"
        addressed_speaker_name = "Enrico"
        prev_dialogue_sentence = "Do you like sex?"
        prev_topic_name = "sex"
        sent_type = "say an interesting positive sentence"
        next_topic_name = "sex"
        tone = "in a funny way"
        prompt = "Context: you have to help me manage a conversation. I will ask you to provide me some information " \
                 "about a sentence, generate an appropriate reply, and finally proceed the dialogue generating a sentence." \
                 "The overall reply should be an XML string, where I can easily extract your answers in Python." \
                 " 1) Tell me which is the topic of the following sentence '" + client_sentence + "', among the following: " \
                 + possible_sentence_topic_str + ". " \
                 "Put the answer in lowercase and surround it with the XML tag <topic>. " \
                 "2) Tell me if the sentence : " + client_sentence + " is positive, negative or neutral. " \
                 "Surround the answer with the tag <sentiment>. " \
                 "3) Pretend you are talking with a person called " + curr_speaker_name + " and you said: '" \
                 + prev_dialogue_sentence + "'. " + curr_speaker_name + " answered to what you said by saying: '" + \
                 client_sentence + "'. Reply with just one sentence (not a question) to " + curr_speaker_name + " " \
                 + tone + ", explicitly saying the name of your interlocutor. Surround the sentence with the tag <reply>. " \
                 "4) Choose the correct one among the following two cases: " \
                 "4a) If the topic you previously surrounded with the <topic> tag is 'none' or '" + prev_topic_name + "', " + sent_type + \
                 " to " + addressed_speaker_name + " about a topic called " + next_topic_name + ".  " \
                 "Explicitly mention the name to make clear who you are addressing. " \
                 "If any, surround the sentence with the tag <question1>. " \
                 "4b) If the topic you previously surrounded with the <topic> tag is different from 'none' and " + \
                 prev_topic_name + " ask a yes/no question to " + addressed_speaker_name + " about the topic you found " \
                 "in 1). If any, surround the sentence with the tag <question2>." \

        print(prompt)
    else:
        prompt = args.sentence
    req(prompt)
