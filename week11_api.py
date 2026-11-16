import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError


def main():
    env_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(env_path)

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model = os.getenv("MODEL_NAME", "gpt-4.1-mini").strip()

    if not api_key:
        print("Добавь OPENAI_API_KEY в файл .env")
        return

    question = (
        "Find the median of 10, 20, 30, 40. "
        "Explain the calculation in simple English."
    )

    print("Модель:", model)
    print("Вопрос:", question)
    print("Ожидаем ответ...")

    try:
        with OpenAI(
            api_key=api_key,
            timeout=60.0,
            max_retries=0,
        ) as client:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a data analysis assistant. "
                            "Explain statistical concepts in simple language."
                        ),
                    },
                    {"role": "user", "content": question},
                ],
            )

        if not response.choices:
            print("Модель вернула ответ без вариантов.")
            return

        answer = response.choices[0].message.content

        if not answer or not answer.strip():
            print("Модель вернула пустой ответ.")
            return

        print("\nОтвет:")
        print(answer.strip())

    except OpenAIError as error:
        print("Ошибка подключения:", type(error).__name__)
        print("HTTP-статус:", getattr(error, "status_code", None))


if __name__ == "__main__":
    main()