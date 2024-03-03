import sqlite3
from datetime import datetime

class ActionCheckDoctorAvailability(Action):
    def name(self) -> Text:
        return "action_check_doctor_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Retrieve the doctor_id slot value from the tracker
        doctor_id = tracker.get_slot('doctor_id')

        if doctor_id:
            # Connect to your database (assuming SQLite for this example)
            conn = sqlite3.connect('doctor_availability.db')
            c = conn.cursor()

            # Retrieve available slots for the specified doctor from the database
            c.execute("SELECT time_slot FROM doctor_availability WHERE doctor_id = ? AND available = 1", (doctor_id,))
            available_slots = c.fetchall()
            
            # Close the database connection
            conn.close()

            if available_slots:
                # Extract time slots from the query result
                available_slots = [slot[0] for slot in available_slots]
                
                # Format the time slots for display
                formatted_slots = ", ".join(available_slots)
                
                # Send a message to the user with the available time slots
                dispatcher.utter_message(text=f"Available slots for doctor {doctor_id}: {formatted_slots}")
            else:
                dispatcher.utter_message(text=f"Sorry, no slots available for doctor {doctor_id}.")
        else:
            dispatcher.utter_message(text="Doctor ID not provided. Please provide a valid doctor ID.")

        return []
