from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime, timedelta

class ActionGenerateDates(Action):
    def name(self):
        return "action_generate_dates"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        today = datetime.now().date()
        dates = [today + timedelta(days=i) for i in range(4)]

        date_buttons = [
            {"title": date.strftime("%Y-%m-%d"), "payload": "date"}
            for date in dates
        ]

        dispatcher.utter_message(
            text="Please select a date:",
            buttons=date_buttons
        )

        return []
