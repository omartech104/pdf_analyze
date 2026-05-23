import os
from dotenv import load_dotenv
from groq import Groq
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from PyPDF2 import PdfReader

load_dotenv()

console = Console()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    console.print("[bold red]Missing GROQ_API_KEY in .env[/bold red]")
    exit()

client = Groq(api_key=api_key)

def extract_pdf_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text

    except Exception as e:
        console.print(f"[red]Error reading PDF:[/red] {e}")
        return None

def ask_pdf_question(pdf_text, question):
    try:
        prompt = f"""
You are a PDF assistant.

Answer ONLY using the provided PDF content.

PDF CONTENT:
{pdf_text[:12000]}

QUESTION:
{question}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"

def main():
    console.print(
        Panel.fit(
            "[bold cyan]PDF Analyzer with Groq[/bold cyan]\nAsk questions about any PDF",
            border_style="cyan"
        )
    )

    pdf_path = Prompt.ask("\n[bold yellow]Enter PDF path[/bold yellow]")

    if not os.path.exists(pdf_path):
        console.print("[bold red]File does not exist[/bold red]")
        return

    console.print("\n[green]Reading PDF...[/green]")

    pdf_text = extract_pdf_text(pdf_path)

    if not pdf_text:
        console.print("[red]Could not extract text[/red]")
        return

    console.print("[bold green]PDF Loaded Successfully![/bold green]")

    while True:
        question = Prompt.ask(
            "\n[bold cyan]Ask a question ('exit' to quit)[/bold cyan]"
        )

        if question.lower() in ["exit", "quit"]:
            console.print("\n[bold yellow]Goodbye![/bold yellow]")
            break

        console.print("\n[green]Thinking...[/green]")

        answer = ask_pdf_question(pdf_text, question)

        console.print(
            Panel(
                Markdown(answer),
                title="[bold magenta]Answer[/bold magenta]",
                border_style="magenta"
            )
        )

if __name__ == "__main__":
    main()
