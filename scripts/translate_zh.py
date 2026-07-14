#!/usr/bin/env python3
"""Bulk translate RU lessons to Chinese (Simplified) using Google Translate API."""
import os, re, time, html
import urllib.request
import urllib.parse
import urllib.error

def translate_text(text, source="ru", target="zh-CN"):
    """Translate text using Google Translate free endpoint."""
    if not text or not text.strip():
        return text
    
    # Skip code blocks, URLs, and HTML tags
    if text.startswith("http") or text.startswith("<") or text.startswith("```"):
        return text
    
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source}&tl={target}&dt=t&q={urllib.parse.quote(text)}"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read().decode("utf-8")
            # Parse the response: [[["translated","original",...]],...]
            result = eval(data)
            translated = ""
            for sentence in result[0]:
                if sentence[0]:
                    translated += sentence[0]
            return translated
    except Exception as e:
        print(f"  Translation error: {e}")
        return text

def translate_html_file(filepath, output_path):
    """Translate HTML file preserving structure."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Translate title
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        title = title_match.group(1)
        translated_title = translate_text(title, "auto", "zh-CN")
        content = content.replace(f'<title>{title}</title>', f'<title>{translated_title}</title>')
    
    # Translate text content between tags (simplified approach)
    # Find all text nodes that are not inside <script>, <style>, <code>, <pre>
    def translate_text_node(match):
        text = match.group(1)
        if not text.strip() or text.strip().startswith("http"):
            return match.group(0)
        # Skip if it's just whitespace or HTML entities
        if re.match(r'^[\s\n\r\t]*(&[^;]+;)*[\s\n\r\t]*$', text):
            return match.group(0)
        translated = translate_text(text, "auto", "zh-CN")
        return match.group(0).replace(text, translated)
    
    # Pattern: >text< (between > and <)
    # Be careful to skip script/style/code blocks
    content = re.sub(r'>([^<]{10,})<', translate_text_node, content)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"  Translated: {os.path.basename(output_path)}")

if __name__ == "__main__":
    base = "/root/.openclaw/workspace/projects/ai-nontechnical-course"
    ru_lessons = os.path.join(base, "lessons")
    zh_lessons = os.path.join(base, "zh/lessons")
    
    print("Translating lessons to Chinese (Simplified)...")
    
    for lesson_dir in sorted(os.listdir(ru_lessons)):
        ru_path = os.path.join(ru_lessons, lesson_dir, "index.html")
        zh_path = os.path.join(zh_lessons, lesson_dir, "index.html")
        
        if os.path.exists(ru_path):
            translate_html_file(ru_path, zh_path)
            time.sleep(0.5)  # Rate limit
    
    print("\nDone! Now translate catalog.html and glossary.html manually.")
