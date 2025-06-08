"""Super minimal test to verify EidosUI HTML rendering"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import fastapi_tags as ft

app = FastAPI()


@app.get("/", response_class=ft.FTResponse)
def home():
    return ft.Html(
        ft.Head(
            ft.Title("Test"),
            ft.Script(src="https://cdn.tailwindcss.com")
        ),
        ft.Body(
            ft.H1("Pure FastAPI-Tags Works!"),
            ft.Button("Click me", cls="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"),
            cls="min-h-screen p-8"
        )
    )

if __name__ == "__main__":
    import uvicorn
    print("🚀 Testing minimal EidosUI...")
    print("Visit http://localhost:8000")
    uvicorn.run("test_minimal:app", host="0.0.0.0", port=8000, reload=True)