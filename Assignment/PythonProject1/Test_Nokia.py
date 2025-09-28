import unittest
from Nokia import Menu



class TestNokia(unittest.TestCase):

    def setUp(self):
        self.phone = Menu(
            phonebook="Contacts",
            messages="Inbox",
            chat="ChatApp",
            call_register="Missed Calls",
            tone="Classic",
            settings="Default",
            call_divert="Off",
            games="Snake",
            calculator="Basic",
            reminders="None",
            clock="12:00",
            profiles="General",
            sim_services="SIM1"
        )

    def test_get_phonebook(self):
        self.assertEqual(self.phone.get_phonebook(), "Contacts")

    def test_set_phonebook_search(self):
        result = self.phone.set_phonebook(
            search="Contacts",
            service_nos="12345",
            add_name="John",
            edit="EditName",
            assign_tone="Tone1",
            type_of_view="List",
            memory_status="Full",
            send_b_card="CardSent",
            options="Options",
            speed_dials="Speed1",
            voice_tags="VoiceTag1"
        )
        self.assertEqual(result, "Contacts")




