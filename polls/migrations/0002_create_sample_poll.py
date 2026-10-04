from django.db import migrations
from django.utils import timezone


def create_sample_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Choice = apps.get_model("polls", "Choice")

    question, created = Question.objects.get_or_create(
        question_text="What's new?",
        defaults={"pub_date": timezone.now()},
    )

    if created:
        Choice.objects.create(
            question=question,
            choice_text="Not much",
            votes=0,
        )
        Choice.objects.create(
            question=question,
            choice_text="The sky",
            votes=0,
        )
        Choice.objects.create(
            question=question,
            choice_text="Just hacking again",
            votes=0,
        )


def remove_sample_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Question.objects.filter(question_text="What's new?").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_sample_poll,
            remove_sample_poll,
        ),
    ]
