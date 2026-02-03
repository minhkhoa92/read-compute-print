from pytest_bdd import scenario, given, when, then
import pytest
from src import *

@pytest.fixture(scope='function')
def context():
    return {}

@scenario('text_edit.feature', 'change to uppercase')
def test_edit():
    pass

@given('Any kind of text')
def text(context):
    context['input_text'] = 'Test text'

@when('I run certain executions')
def transform(context):
    context['changed_text'] = to_uppercase(context['input_text'])

@then('I should see the same text like length is the same')
def same_length(context):
    print(len(context['input_text'] ))
    assert len(context['input_text'] ) == len(context['changed_text'] )

@then('the text is in uppercase')
def all_uppercase(context):
    assert context['changed_text']  == context['changed_text'] .upper()
