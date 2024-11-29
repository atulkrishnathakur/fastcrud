from fastapi.staticfiles import StaticFiles

def mount_uploaded_files(app):
    UPLOAD_DIRECTORY = "./uploads/"
    app.mount("/uploads", StaticFiles(directory=UPLOAD_DIRECTORY), name="uploads")