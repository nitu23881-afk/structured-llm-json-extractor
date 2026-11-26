import pytest
from pydantic import ValidationError
from main import InvoiceData


def test_valid_invoice():
    invoice = InvoiceData(
        invoice_number="INV-3050",
        invoice_date="25 November 2026",
        customer_name="Priya Sharma",
        customer_address="Bengaluru, Karnataka",
        product="Dell Wireless Keyboard",
        quantity=3,
        subtotal=4500,
        gst=810,
        total=5310,
        payment_status="Paid"
    )

    assert invoice.total == 5310
    assert invoice.quantity == 3


def test_missing_information():
    invoice = InvoiceData(
        invoice_number="INV-3051",
        customer_name="Rahul",
        product="Monitor",
        quantity=1,
        total=12000
    )

    assert invoice.invoice_date is None
    assert invoice.customer_address is None
    assert invoice.gst is None


def test_invalid_quantity():
    with pytest.raises(ValidationError):
        InvoiceData(quantity=0)


def test_incorrect_total():
    with pytest.raises(ValidationError):
        InvoiceData(
            subtotal=4500,
            gst=810,
            total=5000
        )