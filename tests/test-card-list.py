import os
import sys
import json

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
import pytest
from tool_call.tool_call_models.cards import (
    CardsBalanceResponse,
    CardsByPhoneNumberResponse,
    CardInfoByPhoneNumber,
    CardInfoByCardNumberResponse,
)

# This is the example response structure from cache_responses.py
# It will be used to mock the API response.
# We need to wrap it in the expected structure: {"body": [card_balance_response_from_cache]}
mock_api_response_payload = {
    "custNo": "60005982",
    "phoneNumber": "998331191213",
    "firstname": "ASLONXO'JA",
    "middlename": "JALOLIDDINOVICH",
    "lastname": "HAMIDOV",
    "birthDate": "2001-12-13",
    "pinfl": "51312016860023",
    "createdAt": "2024-04-09T20:37:13.764699",
    "cardList": [
        {
            "panMask": "7478",
            "panToken": "87a4be2d-7115-4d63-bf93-d76450b2b1fc",
            "requestId": "87a4be2d-7115-4d63-bf93-d76450b2b1fc",
            "pan": "************7478",
            "expiry": "2604",
            "bankIssuer": "SmartBank",
            "uzcardToken": None,
            "processingSystem": "humo",
            "salaryAmount": 500000000,
            "isVerified": True,
            "createdAt": "2024-04-09T20:42:48.535911",
            "cardDetails": {
                "cardDetailsId": 7846,
                "cardName": "Smartbank Virtual",
                "cardColor": "0006",
                "cardIsPrimary": False,
            },
            "cardBalance": {"balance": "909222", "status": 0},
            "isVirtual": True,
            "bankIcon": {
                "bankLogo": "https://s3.smartbank.uz/bank-logos/smart.png",
                "bankLogoMini": "https://s3.smartbank.uz/bank-logos/smart-mini.png",
                "bankWhiteLogo": "https://s3.smartbank.uz/bank-logos/smart-white.png",
                "bankWhiteLogoMini": "https://s3.smartbank.uz/bank-logos/smart-mini-white.png",
            },
        },
        {
            "panMask": "5289",
            "panToken": "ea8dc9ea-7aba-4bbc-b219-c37f8b6dcfd5",
            "requestId": "ea8dc9ea-7aba-4bbc-b219-c37f8b6dcfd5",
            "pan": "************5289",
            "expiry": "2602",
            "bankIssuer": "Kapital",
            "uzcardToken": None,
            "processingSystem": "humo",
            "salaryAmount": 500000000,
            "isVerified": True,
            "createdAt": "2024-07-02T10:55:27.266157",
            "cardDetails": {
                "cardDetailsId": 23192,
                "cardName": "kapital",
                "cardColor": "0000",
                "cardIsPrimary": False,
            },
            "cardBalance": {"balance": "1000", "status": 0},
            "isVirtual": False,
            "bankIcon": {
                "bankLogo": "https://s3.smartbank.uz/bank-logos/kapital.png",
                "bankLogoMini": "https://s3.smartbank.uz/bank-logos/kapital-mini.png",
                "bankWhiteLogo": "https://s3.smartbank.uz/bank-logos/kapital-white.png",
                "bankWhiteLogoMini": "https://s3.smartbank.uz/bank-logos/kapital-mini-white.png",
            },
        },
        {
            "panMask": "7704",
            "panToken": "8e96ef48-6c03-431a-bc7b-081af3c98d1d",
            "requestId": "8e96ef48-6c03-431a-bc7b-081af3c98d1d",
            "pan": "************7704",
            "expiry": "2907",
            "bankIssuer": "SmartBank",
            "uzcardToken": None,
            "processingSystem": "humo",
            "salaryAmount": 500000000,
            "isVerified": True,
            "createdAt": "2024-07-16T11:34:28.535018",
            "cardDetails": {
                "cardDetailsId": 42946,
                "cardName": "Smartbank fiz",
                "cardColor": "0000",
                "cardIsPrimary": False,
            },
            "cardBalance": {"balance": "28494142", "status": 0},
            "isVirtual": False,
            "bankIcon": {
                "bankLogo": "https://s3.smartbank.uz/bank-logos/smart.png",
                "bankLogoMini": "https://s3.smartbank.uz/bank-logos/smart-mini.png",
                "bankWhiteLogo": "https://s3.smartbank.uz/bank-logos/smart-white.png",
                "bankWhiteLogoMini": "https://s3.smartbank.uz/bank-logos/smart-mini-white.png",
            },
        },
        {
            "panMask": "9710",
            "panToken": "c39cef39-07ab-4439-8c2b-25d07a912c28",
            "requestId": "c39cef39-07ab-4439-8c2b-25d07a912c28",
            "pan": "************9710",
            "expiry": "2910",
            "bankIssuer": "BRB",
            "uzcardToken": None,
            "processingSystem": "humo",
            "salaryAmount": 500000000,
            "isVerified": True,
            "createdAt": "2024-10-23T13:00:01.056936",
            "cardDetails": {
                "cardDetailsId": 166412,
                "cardName": "brb",
                "cardColor": "0000",
                "cardIsPrimary": False,
            },
            "cardBalance": {"balance": "50000", "status": 0},
            "isVirtual": False,
            "bankIcon": {
                "bankLogo": "https://s3.smartbank.uz/bank-logos/brb.png",
                "bankLogoMini": "https://s3.smartbank.uz/bank-logos/brb-mini.png",
                "bankWhiteLogo": "https://s3.smartbank.uz/bank-logos/brb-white.png",
                "bankWhiteLogoMini": "https://s3.smartbank.uz/bank-logos/brb-mini-white.png",
            },
        },
    ],
}


def test_cards_balance_model():
    # Test data from cache_responses.py
    test_data = mock_api_response_payload

    # Create model instance
    cards_balance = CardsBalanceResponse(**test_data)

    # Test basic fields
    assert cards_balance.custNo == "60005982"
    assert cards_balance.phoneNumber == "998331191213"
    assert cards_balance.firstname == "ASLONXO'JA"
    assert cards_balance.middlename == "JALOLIDDINOVICH"
    assert cards_balance.lastname == "HAMIDOV"
    assert cards_balance.birthDate == "2001-12-13"
    assert cards_balance.pinfl == "51312016860023"
    assert cards_balance.createdAt == "2024-04-09T20:37:13.764699"

    # Test first card details
    first_card = cards_balance.cardList[0]
    assert first_card.panMask == "7478"
    assert first_card.panToken == "87a4be2d-7115-4d63-bf93-d76450b2b1fc"
    assert first_card.bankIssuer == "SmartBank"
    assert first_card.isVirtual == True
    assert first_card.salaryAmount == 5000000
    assert first_card.cardDetails.cardName == "Smartbank Virtual"
    assert first_card.cardBalance.balance == 9092
    assert first_card.cardBalance.status == 0

    # Test bank icon details
    assert (
        first_card.bankIcon.bankLogo == "https://s3.smartbank.uz/bank-logos/smart.png"
    )
    assert (
        first_card.bankIcon.bankLogoMini
        == "https://s3.smartbank.uz/bank-logos/smart-mini.png"
    )
    assert (
        first_card.bankIcon.bankWhiteLogo
        == "https://s3.smartbank.uz/bank-logos/smart-white.png"
    )
    assert (
        first_card.bankIcon.bankWhiteLogoMini
        == "https://s3.smartbank.uz/bank-logos/smart-mini-white.png"
    )

    # filter for llm
    assert [
        "pan",
        "balance",
        "bankIssuer",
        "processingSystem",
        "cardDetails",
    ] == list(json.loads(cards_balance.filter_for_llm())[0].keys())


cards_by_phone_number_mock_data = [
    {
        "pan": "3b1cdf68-cd9f-496a-b756-cd7884b5b9f9",
        "name": "A. H",
        "processing": "uzcard",
        "mask": "561468******9682",
    },
    {
        "pan": "29d95efd-bb2b-4227-9793-eb6044de3315",
        "name": "A. K",
        "processing": "humo",
        "mask": "986010******5289",
    },
    {
        "pan": "46620d73-73a5-41b9-a7c6-aa6d07dd56b0",
        "name": "A. H",
        "processing": "humo",
        "mask": "406707******7704",
    },
    {
        "pan": "af610af3-cece-4c87-8a40-63db78b621cc",
        "name": "A. H",
        "processing": "humo",
        "mask": "406707******8177",
    },
    {
        "pan": "76cd8ea6-cfc6-4196-8ad0-d95455ec9dce",
        "name": "A. H",
        "processing": "humo",
        "mask": "406707******7478",
    },
    {
        "pan": "c43ebaca-1c5a-466f-96bf-87e5ce4eb3a7",
        "name": "A. K",
        "processing": "humo",
        "mask": "986006******9710",
    },
    {
        "pan": "e7d6f906-95a8-41b3-b2da-f2e089ead243",
        "name": "A. H",
        "processing": "humo",
        "mask": "986003******4907",
    },
]


def test_cards_by_phone_number_model():
    cards_by_phone_number = CardsByPhoneNumberResponse(cards_by_phone_number_mock_data)
    assert isinstance(cards_by_phone_number.cards, list)
    for card in cards_by_phone_number.cards:
        assert isinstance(card, CardInfoByPhoneNumber)
    assert (
        json.loads(cards_by_phone_number.filter_for_llm())
        == cards_by_phone_number_mock_data
    )


mock_card_found = {
    "processingSystem": "humo",
    "iconMini": "https://s3.smartbank.uz/bank-logos/smart-mini-white.png",
    "isFound": True,
    "maskedPan": "************7704",
    "errorMessage": None,
    "icon": "https://s3.smartbank.uz/bank-logos/smart-white.png",
    "fullName": "ASLONXOJA HAMIDOV",
    "errorCode": None,
    "token": "ca236d2f-b592-45fb-aac0-5b32e8fddf76",
}

mock_card_not_found = {
    "processingSystem": None,
    "iconMini": None,
    "isFound": False,
    "maskedPan": None,
    "errorMessage": "Card not found",
    "icon": None,
    "fullName": None,
    "errorCode": "5000",
    "token": None,
}


def test_card_info_by_card_number_model():
    card_info_by_card_number = CardInfoByCardNumberResponse(**mock_card_found)
    assert card_info_by_card_number.processingSystem == "humo"
    assert (
        card_info_by_card_number.iconMini
        == "https://s3.smartbank.uz/bank-logos/smart-mini-white.png"
    )
    assert card_info_by_card_number.isFound == True
    assert card_info_by_card_number.maskedPan == "************7704"
    assert card_info_by_card_number.errorMessage == None
    assert (
        card_info_by_card_number.icon
        == "https://s3.smartbank.uz/bank-logos/smart-white.png"
    )
    assert card_info_by_card_number.fullName == "ASLONXOJA HAMIDOV"

    # not found
    card_info_by_card_number = CardInfoByCardNumberResponse(**mock_card_not_found)
    assert card_info_by_card_number.processingSystem == None
    assert card_info_by_card_number.iconMini == None
    assert card_info_by_card_number.isFound == False
    assert card_info_by_card_number.maskedPan == None
    assert card_info_by_card_number.errorMessage == "Card not found"
    assert card_info_by_card_number.icon == None
    assert card_info_by_card_number.fullName == None
    assert card_info_by_card_number.errorCode == "5000"
    assert card_info_by_card_number.token == None
