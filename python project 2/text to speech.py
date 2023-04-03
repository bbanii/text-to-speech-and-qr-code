import PySimpleGUI as sg
import pyttsx3 as pt

# Initialize the text-to-speech engine
speaker = pt.init()

# Create a list of available voices
voices = speaker.getProperty('voices')

# Define the layout of the GUI
layout = [
    [sg.Input(key='text'), sg.Button('Speak')],
    [sg.Radio('Male', "RADIO1", key='male', default=True),
     sg.Radio('Female', "RADIO1", key='female')],
    [sg.Text('Speed'), sg.Slider(range=(50, 400), default_value=200, orientation='h', key='speed')],
    [sg.Text('Volume'), sg.Slider(range=(0, 100), default_value=50, orientation='h', key='volume')],
]

# Create the window
window = sg.Window('Text-to-Speech App', layout)

# Start the event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        # Set the voice
        if values['male']:
            speaker.setProperty('voice', voices[0].id)
        elif values['female']:
            speaker.setProperty('voice', voices[1].id)
        # Set the reading speed
        speaker.setProperty('rate', values['speed'])
        # Set the volume
        speaker.setProperty('volume', values['volume'] / 100)
        # Speak the text
        speaker.say(values['text'])
        speaker.runAndWait()

# Close the window
window.close()