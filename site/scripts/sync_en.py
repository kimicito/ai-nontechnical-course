#!/usr/bin/env python3
"""Sync RU lesson changes to EN version. Run after updating RU lessons."""
import os, shutil, glob

base = "/root/.openclaw/workspace/projects/ai-nontechnical-course/site"
ru_lessons = os.path.join(base, "lessons")
en_lessons = os.path.join(base, "en/lessons")

print("Syncing EN lessons from RU...")

# Copy all RU lessons to EN (overwrite)
for lesson_dir in glob.glob(os.path.join(ru_lessons, "*/")):
    lesson_name = os.path.basename(os.path.dirname(lesson_dir))
    en_dir = os.path.join(en_lessons, lesson_name)
    
    if not os.path.exists(en_dir):
        shutil.copytree(lesson_dir, en_dir)
        print(f"  + Created: {lesson_name}")
    else:
        # Copy index.html
        shutil.copy2(os.path.join(lesson_dir, "index.html"), os.path.join(en_dir, "index.html"))
        print(f"  ~ Updated: {lesson_name}")

print("\nNow run bulk_translate.py to re-apply common phrase translations")
