import speech_recognition as sr
r = sr.Recognizer()
while True:
    lang = input('Enter 1 for English and 2 for Hindi:\n\t')
    if lang == '1':
        language = "en-IN"
        break
    elif lang == '2':
        language = 'hi-IN'
        break
    else :
        print('Wrong Input! Enter Again')
while True:
    with sr.Microphone() as source:
        print('Speak Now!')
        audio = r.listen(source)
        try :
            text = r.recognize_google(audio, language = language)
            print(f'You said: "{text}"')
        except IndexError:                                  # the API key didn't work
            print("No internet connection")
        except KeyError:                                    # the API key didn't work
            print("Invalid API key or quota maxed out")
        except LookupError:                                 # speech is unintelligible
            print("Could not understand audio")
    y = input('If you want to speak again then press "y" else press "n" \n\t')
    if y == 'n' : 
        break

print('Thank you for using me!\tSee you soon.')