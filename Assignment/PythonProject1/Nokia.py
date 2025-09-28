

class Menu:
    def __init__(self, phonebook, messages, chat, call_register, tone, settings, call_divert,
                 games, calculator, reminders, clock, profiles, sim_services):
        self.Phonebook = phonebook
        self.Messages = messages
        self.Chat = chat
        self.Call_Register = call_register
        self.Tone = tone
        self.Settings = settings
        self.Call_Divert = call_divert
        self.Games = games
        self.Calculator = calculator
        self.Reminders = reminders
        self.Clock = clock
        self.Profiles = profiles
        self.SimServices = sim_services

    def get_phonebook(self):
        return self.Phonebook

    def set_phonebook(self, search, service_nos, add_name, edit, assign_tone,
                      type_of_view, memory_status, send_b_card, options,
                      speed_dials, voice_tags):

        if search == self.Phonebook:
            return search
        elif service_nos == self.Phonebook:
            return service_nos
        elif add_name == self.Phonebook:
            return add_name
        elif edit == self.Phonebook:
            return edit
        elif assign_tone == self.Phonebook:
            return assign_tone
        elif send_b_card == self.Phonebook:
            return send_b_card
        elif options == self.Phonebook:
            options = type_of_view
            options = memory_status
            return options
        elif speed_dials == self.Phonebook:
            return speed_dials
        elif voice_tags == self.Phonebook:
            return voice_tags
        else:
            raise Exception('Invalid option')

