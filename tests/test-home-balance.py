import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
import pytest
from tool_call.tool_call_models.home_balance import (
    HomeBalance,
    HomeBalanceDetails,
)


def test_home_balance_details():
    # Test initialization with balance in cents
    details = HomeBalanceDetails(balance=10000, details={"123": 5000})
    assert details.balance == 100  # Should be converted from cents to dollars

    # Test initialization with balance already in dollars
    details = HomeBalanceDetails(balance=100, details={"123": 5000})
    assert details.balance == 1


def test_home_balance_model():
    # Test data
    test_data = {
        "homeName": "Test Home",
        "gas": {"balance": 10000, "details": {"123": 5000}},
        "electricity": {"balance": 20000, "details": {"456": 10000}},
        "coldWater": {"balance": 15000, "details": {"789": 7500}},
    }

    # Create model instance
    home_balance = HomeBalance(**test_data)
    print(home_balance)
    # Test homeName
    assert home_balance.homeName == "Test Home"

    # Test services extraction
    assert "gas" in home_balance.services
    assert "electricity" in home_balance.services
    assert "coldWater" in home_balance.services

    # Test balance conversion
    assert home_balance.services["gas"].balance == 100
    assert home_balance.services["electricity"].balance == 200
    assert home_balance.services["coldWater"].balance == 150

    # Test details preservation
    assert home_balance.services["gas"].details == {"123": 5000}
    assert home_balance.services["electricity"].details == {"456": 10000}
    assert home_balance.services["coldWater"].details == {"789": 7500}


def test_home_balance_filter_for_llm():
    test_data = {
        "homeName": "Test Home",
        "gas": {"balance": 10000, "details": {"123": 5000}},
        "electricity": {"balance": 20000, "details": {"456": 10000}},
        "coldWater": {"balance": 15000, "details": {"789": 7500}},
    }

    home_balance = HomeBalance(**test_data)
    filtered_data = home_balance.filter_for_llm()

    print("Filtered data: ", filtered_data)

    # Test that the filtered data contains the expected structure
    assert "homeName" in filtered_data
    assert "services" in filtered_data
    assert "gas" in filtered_data["services"]
    assert "electricity" in filtered_data["services"]
    assert not filtered_data["services"]["coldWater"].get("details")
