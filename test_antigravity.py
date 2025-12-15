from playwright.sync_api import Page, expect

def test_google_antigravity_title(page: Page):
    page.goto("https://antigravity.google/")
    expect(page).to_have_title("Google Antigravity")
