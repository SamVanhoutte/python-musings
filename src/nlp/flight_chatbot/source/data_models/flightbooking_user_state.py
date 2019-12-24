# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from enum import Enum
class QuestionAsked(Enum):
    Origin = 1
    Destination = 2
    PassengerCount = 3
    NoQuestion = 0

class FlightBookingUserState:

    def __init__(self, did_welcome: bool = False):
        self.did_welcome_user = did_welcome
        self.origin_airport = ''
        self.destination_airport = ''
        self.number_of_passengers = 0
        self.question_asked = QuestionAsked.NoQuestion
