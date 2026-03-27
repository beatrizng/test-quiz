from model import Question, Choice
import pytest

def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# NOVOS UNIT TESTES (Commit 2)

def test_question_title_too_long():
    with pytest.raises(Exception):
        Question(title='a' * 201)

def test_invalid_points_low():
    with pytest.raises(Exception):
        Question(title='q1', points=0)


def test_invalid_points_high():
    with pytest.raises(Exception):
        Question(title='q1', points=101)

def test_choice_empty_text():
    with pytest.raises(Exception):
        Choice(id=1, text='')
    
def test_choice_text_too_long():
    with pytest.raises(Exception):
        Choice(id=1, text='a' * 101)

def test_remove_choice_by_id():
    q = Question(title='q1')
    c = q.add_choice('a', False)

    q.remove_choice_by_id(c.id)

    assert len(q.choices) == 0


def test_remove_all_choices():
    q = Question(title='q1')
    q.add_choice('a', False)
    q.add_choice('b', True)

    q.remove_all_choices()

    assert len(q.choices) == 0


def test_set_correct_choices():
    q = Question(title='q1')
    c1 = q.add_choice('a', False)
    c2 = q.add_choice('b', False)

    q.set_correct_choices([c2.id])

    assert c2.is_correct
    assert not c1.is_correct


def test_remove_invalid_choice_id():
    q = Question(title='q1')
    q.add_choice('a', False)

    with pytest.raises(Exception):
        q.remove_choice_by_id(999)


def test_exceed_max_selections():
    q = Question(title='q1', max_selections=1)
    c1 = q.add_choice('a', True)
    c2 = q.add_choice('b', False)

    with pytest.raises(Exception):
        q.correct_selected_choices([c1.id, c2.id])


# FIXTURE (Commit 3)

@pytest.fixture
def sample_question():
    q = Question(title='q1')
    q.add_choice('a', False)
    q.add_choice('b', True)
    return q


def test_fixture_choice_count(sample_question):
    assert len(sample_question.choices) == 2

def test_fixture_has_one_correct(sample_question):
    correct = [c for c in sample_question.choices if c.is_correct]
    assert len(correct) == 1