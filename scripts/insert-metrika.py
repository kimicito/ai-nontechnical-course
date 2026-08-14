#!/usr/bin/env python3
"""Insert Yandex Metrika counter into all HTML files."""

import os
import re

PROJECT_DIR = "/root/.openclaw/workspace/projects/ai-nontechnical-course"
COUNTER_ID = "111617413"

METRIKA_CODE = f'''<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};
   m[i].l=1*new Date();
   for (var j = 0; j < document.scripts.length; j++) {{if (document.scripts[j].src === r) {{ return; }}}}
   k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym({COUNTER_ID}, "init", {{
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true
   }});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/{COUNTER_ID}" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->'''

def insert_metrika(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has metrika
    if 'mc.yandex.ru' in content or 'ym(' in content:
        return False, "already has metrika"
    
    # Skip if no </head>
    if '</head>' not in content:
        return False, "no </head> tag"
    
    # Insert before </head>
    new_content = content.replace('</head>', METRIKA_CODE + '\n</head>', 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "inserted"

def main():
    updated = []
    skipped = []
    
    for root, dirs, files in os.walk(PROJECT_DIR):
        # Skip .git and node_modules
        dirs[:] = [d for d in dirs if d not in {'.git', 'node_modules', 'pagefind'}]
        
        for fname in files:
            if not fname.endswith('.html'):
                continue
            
            filepath = os.path.join(root, fname)
            success, reason = insert_metrika(filepath)
            
            rel = os.path.relpath(filepath, PROJECT_DIR)
            if success:
                updated.append(rel)
            else:
                skipped.append(f"{rel}: {reason}")
    
    print(f"=== Updated ({len(updated)}) ===")
    for f in updated:
        print(f"  + {f}")
    
    print(f"\n=== Skipped ({len(skipped)}) ===")
    for f in skipped:
        print(f"  - {f}")

if __name__ == "__main__":
    main()
