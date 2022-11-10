
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#firebase imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('.json') #enter your firebase generated credential json file

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://.firebasedatabase.app/' #enter your firebase databaseURL 
})

class ActionLightOn(Action):
    def name(self) -> Text:
        return "action_light_on"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ref = db.reference('/')
        ref.update({
            'lightState':'true'
        })
        #read from table
        print(ref.get())
        dispatcher.utter_message(text=f"light on {ref.get()}")

        return []


class ActionLightOn(Action):
    def name(self) -> Text:
        return "action_light_off"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ref = db.reference('/')
        ref.update({
            'lightState':'false'
        })
        #read from table
        print(ref.get())
        dispatcher.utter_message(text=f"light off {ref.get()}")

        return []