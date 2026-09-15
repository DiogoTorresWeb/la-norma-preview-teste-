import subprocess, os

base_dir = r"c:\Users\Diogo Torres\diogo-base\Projetos\La Norma\contexto"
html_path = os.path.join(base_dir, "propuesta-daniel-5slides.html")

with open(html_path, "r", encoding="utf-8") as f:
    full_html = f.read()

body_start = full_html.find("<body>") + 6
header_part = full_html[:body_start]

for i in range(1, 6):
    s_tag = f'<section class="slide" id="slide-{i}">'
    start = full_html.find(s_tag)
    end = full_html.find("</section>", start) + len("</section>")
    slide_content = full_html[start:end]
    
    single_html = header_part + slide_content + "</body></html>"
    tmp_file = os.path.join(base_dir, f"tmp-slide-{i}.html")
    with open(tmp_file, "w", encoding="utf-8") as f:
        f.write(single_html)
        
    shot_file = os.path.join(base_dir, f"preview-slide-{i}.png")
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--window-size=1920,1080",
        f"--screenshot={shot_file}",
        tmp_file
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Slide {i} screenshot ready: {shot_file}")
