# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import (
    ActivityHandler,
    TurnContext,
    UserState,
    CardFactory,
    MessageFactory,
)
from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardImage,
    CardAction,
    ActionTypes,
)

from data_models import FlightBookingUserState, QuestionAsked
from .luis_client import LuisClient
from datetime import date
import datetime

import sys

class FlightBookingBot(ActivityHandler):

    def __init__(self, user_state: UserState, key, appId, endpoint):
        if user_state is None:
            raise TypeError(
                "[FlightBookingBot]: Missing parameter. user_state is required but None was given"
            )
        self.luis_key = key
        self.luis_appid = appId
        self.luis_endpoint = endpoint
        self.user_state = user_state
        self.user_state_accessor = self.user_state.create_property("FlightBookingUserState")
        self.WELCOME_MESSAGE = """Ik ben Fly.  Ik ben je bot om vluchten te boeken."""


    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)

        # save changes to FlightBookingUserState after each turn
        await self.user_state.save_changes(turn_context)

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        """
        Greet when users are added to the conversation.
        """
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    f"Hi there { member.name }. " + self.WELCOME_MESSAGE
                )

                await turn_context.send_activity(
                    """You can just ask your question to Fly to book your flight."""
                )

    async def on_message_activity(self, turn_context: TurnContext):
        """
        Respond to messages sent from the user.
        """
        # Get the state properties from the turn context.
        flight_user_state = await self.user_state_accessor.get(
            turn_context, FlightBookingUserState
        )

        if not flight_user_state.did_welcome_user:
            flight_user_state.did_welcome_user = True

            name = turn_context.activity.from_property.name
            await turn_context.send_activity(
                f"Welkom {name}"
            )

        user_text = turn_context.activity.text

        #Verify intent
        try:
            # Handle incoming request
            if flight_user_state.question_asked == QuestionAsked.NoQuestion:
                # We are getting a request without having asked a question before, 
                # so we're applying Luis intent logic to check for travel.flight
                intent = LuisClient.getIntent(user_text, self.luis_key, self.luis_endpoint, self.luis_appid, False)
                if intent.prediction.topIntent!='travel.flight':
                    # We get an intent that is not known or expected
                    # In real world, we should log these for further enhancements
                    await turn_context.send_activity(
                        f'Fly zegt sorry: De intent {intent.prediction.topIntent} is nog niet gekend door mij'
                    )
                    return
                
                # Now we have successfully interpreted the request as travel.flight intent and we try to get Origin & Destination
                if ('Origin' in intent.prediction.entities):
                    flight_user_state.origin_airport = intent.prediction.entities['Origin'][0][0]
                if ('Destination' in intent.prediction.entities):
                    flight_user_state.destination_airport = intent.prediction.entities['Destination'][0][0]
            else:
                # We are getting an answer to a question asked, so let's store the information 
                # Saving the answer in the user state
                if flight_user_state.question_asked == QuestionAsked.Origin:
                    # We could use the entities on Luis to translate Oostende to OST, but this is not in scope
                    flight_user_state.origin_airport = user_text
                elif flight_user_state.question_asked == QuestionAsked.Destination:
                    # We could use the entities on Luis to translate Oostende to OST, but this is not in scope
                    flight_user_state.destination_airport = user_text
                elif flight_user_state.question_asked == QuestionAsked.PassengerCount:
                    # Interpret the intent and check for passengercount intent, with the number entity
                    intent = LuisClient.getIntent(user_text, self.luis_key, self.luis_endpoint, self.luis_appid, False)
                    if intent.prediction.topIntent!='travel.passengercount':
                        await turn_context.send_activity(
                            f'Fly zegt sorry: De intent {intent.prediction.topIntent} is nog niet gekend door mij'
                        )
                        return
                    # Reading the number value from the parsed intent
                    if ('number' in intent.prediction.entities):
                        flight_user_state.number_of_passengers = str(intent.prediction.entities['number'][0])
                    else:
                        flight_user_state.number_of_passengers = 1

            # Send response to ask for more information, where needed
            if flight_user_state.origin_airport == '':
                flight_user_state.question_asked = QuestionAsked.Origin
                await turn_context.send_activity(f"Perfect.  Van welke luchthaven wil je vertrekken?")
                return
            if flight_user_state.destination_airport == '':
                flight_user_state.question_asked = QuestionAsked.Destination
                await turn_context.send_activity(f"Dank je.  Naar welke luchthaven wil je vliegen?")
                return
            if flight_user_state.number_of_passengers == 0:
                flight_user_state.question_asked = QuestionAsked.PassengerCount
                await turn_context.send_activity(f"Met hoeveel wil je vliegen?")
                return
            
            # Since we arrive here, we can return the final confirmation in a card
            await self.__send_flight_confirmation(turn_context, flight_user_state.origin_airport, flight_user_state.destination_airport, flight_user_state.number_of_passengers)
        except Exception as e:
            await turn_context.send_activity(
                f'Fly zegt sorry: ik ben serieus gecrashed met deze Engelstalige fout: {e}'
            )

    async def __send_flight_confirmation(self, turn_context: TurnContext, origin, destination, passengerCount):
        departure_date = date.today() + datetime.timedelta(days=5)
        return_date = date.today() + datetime.timedelta(days=10)
        
        card = HeroCard(
            title="Fly heeft jouw vlucht voorbereid!",
            text=f"Hier kan je alle informatie voor jouw vlucht van {origin} naar {destination} vinden voor {passengerCount} volwassenen",
            images=[CardImage(url="https://aka.ms/bf-welcome-card-image")],
            buttons=[
                CardAction(
                    type=ActionTypes.open_url,
                    title="Vlucht informatie",
                    text="Vlucht details",
                    display_text="Vlucht details",
                    value=f"https://v2.vliegtickets.be/results/outbound/{origin}-{destination}/{departure_date.strftime('%Y-%m-%d')}/{return_date.strftime('%Y-%m-%d')}/{passengerCount},0,0/?airline=&departureAirports={origin}&arrivalAirports={destination}&isFiltersOpen=0",
                )
            ],
        )

        return await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.hero_card(card))
        )
