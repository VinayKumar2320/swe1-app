import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


def create_question(question_text="What's new?", days=0):
    return Question.objects.create(
        question_text=question_text,
        pub_date=timezone.now() + datetime.timedelta(days=days),
    )


class QuestionModelTests(TestCase):
    def test_question_string(self):
        question = create_question("Favorite programming language?")
        self.assertEqual(str(question), "Favorite programming language?")

    def test_recent_question(self):
        question = create_question(days=0)
        self.assertTrue(question.was_published_recently())

    def test_old_question(self):
        question = create_question(days=-5)
        self.assertFalse(question.was_published_recently())

    def test_choice_string(self):
        question = create_question()
        choice = Choice.objects.create(
            question=question,
            choice_text="Python",
        )
        self.assertEqual(str(choice), "Python")

    def test_choice_default_votes(self):
        question = create_question()
        choice = Choice.objects.create(
            question=question,
            choice_text="Java",
        )
        self.assertEqual(choice.votes, 0)


class IndexViewTests(TestCase):
    def test_index_without_questions(self):
        Question.objects.all().delete()

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_index_with_question(self):
        question = create_question("Which framework?")
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.question_text)

    def test_questions_ordered_newest_first(self):
        Question.objects.all().delete()

        older = create_question("Older question", days=-2)
        newer = create_question("Newer question", days=-1)

        response = self.client.get(reverse("polls:index"))
        questions = list(response.context["latest_question_list"])

        self.assertEqual(questions, [newer, older])

    def test_index_displays_only_five_questions(self):
        for i in range(7):
            create_question(f"Question {i}", days=-i)

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(len(response.context["latest_question_list"]), 5)


class DetailViewTests(TestCase):
    def test_detail_page(self):
        question = create_question("Best Python library?")
        response = self.client.get(reverse("polls:detail", args=[question.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.question_text)

    def test_detail_page_not_found(self):
        response = self.client.get(reverse("polls:detail", args=[9999]))
        self.assertEqual(response.status_code, 404)


class ResultsViewTests(TestCase):
    def test_results_page(self):
        question = create_question("Favorite database?")
        Choice.objects.create(
            question=question,
            choice_text="PostgreSQL",
            votes=3,
        )

        response = self.client.get(reverse("polls:results", args=[question.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "PostgreSQL")

    def test_results_page_not_found(self):
        response = self.client.get(reverse("polls:results", args=[9999]))
        self.assertEqual(response.status_code, 404)


class VoteViewTests(TestCase):
    def setUp(self):
        self.question = create_question("Favorite language?")
        self.choice = Choice.objects.create(
            question=self.question,
            choice_text="Python",
        )
        self.vote_url = reverse("polls:vote", args=[self.question.id])

    def test_valid_vote(self):
        response = self.client.post(
            self.vote_url,
            {"choice": self.choice.id},
        )

        self.assertRedirects(
            response,
            reverse("polls:results", args=[self.question.id]),
        )
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 1)

    def test_multiple_votes(self):
        for _ in range(3):
            self.client.post(
                self.vote_url,
                {"choice": self.choice.id},
            )

        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 3)

    def test_vote_without_choice(self):
        response = self.client.post(self.vote_url, {})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["error_message"],
            "You didn't select a choice.",
        )

    def test_vote_with_invalid_choice(self):
        response = self.client.post(
            self.vote_url,
            {"choice": 9999},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["error_message"],
            "You didn't select a choice.",
        )

    def test_vote_for_missing_question(self):
        response = self.client.post(
            reverse("polls:vote", args=[9999]),
            {"choice": self.choice.id},
        )
        self.assertEqual(response.status_code, 404)
