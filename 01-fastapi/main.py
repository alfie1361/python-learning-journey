from fastapi import FastAPI

# ساخت اپلیکیشن
app = FastAPI(
    title="Python Learning Journey",
    description="اولین API من با FastAPI",
    version="0.1.0"
)


# endpoint اول - صفحه اصلی
@app.get("/")
def read_root():
    return {
        "message": "سلام دنیا! 🚀",
        "status": "success",
        "data": {
            "project": "Python Learning Journey",
            "phase": "Phase 1: FastAPI",
            "day": 1
        }
    }


# endpoint دوم - درباره ما
@app.get("/about")
def about():
    return {
        "name": "python-learning-journey",
        "author": "reza gharib",
        "goal": "تبدیل شدن به یک توسعه‌دهنده بک‌اند و دیتا ساینتیست",
        "tech_stack": ["Python", "FastAPI", "PostgreSQL", "Docker"]
    }


# endpoint سوم - سلام کردن به یه شخص
@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"سلام {name}! خوش اومدی 🎉",
        "name": name
    }