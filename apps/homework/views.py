from django.http import HttpResponse

from apps.homework.processing_users import format_users, output_user_info


def generate_users(request, name: str, amount: int = 100):
    formatted_users = format_users(amount)
    output = output_user_info(formatted_users)
    return HttpResponse(f"Hello {name}. Generated users for you: <ol>{output}</ol>")
