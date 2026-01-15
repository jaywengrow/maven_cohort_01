from dotenv import load_dotenv
import os
import io
import zipfile
import requests
from bs4 import BeautifulSoup

load_dotenv('.env')
NETLIFY_TOKEN = os.getenv("NETLIFY_TOKEN")
API_BASE = "https://api.netlify.com/api/v1"

def read_webpage(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, "html.parser")
    return str(html)

def auth_headers(content_type=None):
    headers = {
        "Authorization": f"Bearer {NETLIFY_TOKEN}",
    }
    if content_type:
        headers["Content-Type"] = content_type
    return headers


def deploy_site(html):
    # 1. Create site
    site_resp = requests.post(
        f"{API_BASE}/sites",
        headers=auth_headers("application/json"),
        json={},
    )
    site_resp.raise_for_status()
    site = site_resp.json()
    site_id = site["id"]

    # 2. Create ZIP in memory (index.html at ZIP root)
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("index.html", html.encode("utf-8"))
        # with open("index.html", "rb") as f:
        #     z.writestr("index.html", f.read())

        # 🔑 FORCE HTML MIME TYPE
        z.writestr("_headers", "/*\n  Content-Type: text/html; charset=utf-8\n")

    zip_buffer.seek(0)

    # 3. Deploy ZIP
    deploy_resp = requests.post(
        f"{API_BASE}/sites/{site_id}/deploys",
        headers=auth_headers("application/zip"),
        data=zip_buffer.read(),
    )
    deploy_resp.raise_for_status()
    # deploy = deploy_resp.json()
    # print("🚀 Deploy complete")
    # print("Production URL:", site["url"])
    # print("Deploy URL:", deploy.get("deploy_url"))
    return site["url"]
