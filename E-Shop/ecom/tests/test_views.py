from django.test import TestCase

# Create your tests here.
# ecom/tests/test_views.py

import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_product_list_view():
    client = Client()
    response = client.get(reverse('product_list'))
    assert response.status_code == 200
    assert 'products' in response.context

