import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_registration():
    client = Client()
    response = client.post(reverse('register'), {
        'username': 'testuser',
        'password1': 'testpassword',
        'password2': 'testpassword'
    })
    assert response.status_code == 302  # Redirects after successful registration
    assert User.objects.filter(username='testuser').exists()

@pytest.mark.django_db
def test_user_login():
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = Client()
    response = client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 302  # Redirects after successful login
    assert client.session['_auth_user_id'] == str(user.pk)
