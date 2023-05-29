from django.shortcuts import redirect, render
from .forms import Text_Form
import cv2
from django.conf import settings
import numpy as np
import uuid
import os


def create_scroll_text_video(text, width=100, height=100, duration=3):

    image = np.zeros((height, width, 3), dtype=np.uint8)
    image.fill(0)

    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 0.8
    font_thickness = 2

    (text_width, text_height), _ = cv2.getTextSize(
        text, font, font_scale, font_thickness)

    x = width
    y = height - int((height - text_height) / 2)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    file_name = os.path.join(settings.BASE_DIR, "videos")
    file_name = os.path.join(file_name, str(uuid.uuid4())+".mp4")
    video = cv2.VideoWriter(file_name, fourcc, 30, (width, height))

    target_frame_count = int(duration * 30)
    frame_number = 0
    speed = int((text_width + 10) / (duration * 30))
    while frame_number < target_frame_count:

        frame = np.copy(image)

        cv2.putText(frame, text, (x, y), font, font_scale,
                    (255, 255, 255), font_thickness)

        x -= speed

        video.write(frame)

        frame_number += 1

    video.release()


# Create your views here.
def crawl_line(request):
    if request.method == "POST":
        form = Text_Form(request.POST)
        if form.is_valid():
            form.save()
            create_scroll_text_video(form.data["text"])
            return redirect("home")
    form = Text_Form()
    return render(request, "index.html", {"form": form})
