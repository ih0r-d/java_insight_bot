import requests
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bs4 import BeautifulSoup
from aiogram.enums import ParseMode

from ..common.constants import java_versions_url

router = Router()


@router.message(Command('java_releases'))
async def java_release_cmd(message: Message):
    releases = get_java_release_info()
    response = "<b>Java Releases:\n\n</b>"
    for release in releases:
        response += f"<b>Version:</b> {release[0]}\n<b>Release Date:</b> {release[1]}\n<b>Pockets:</b> {release[2]}\n\n"
    await message.answer(response, parse_mode=ParseMode.HTML)


def get_java_release_info():
    response = requests.get(java_versions_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    release_table = soup.find('table', {'class': 'wikitable'})
    releases = []
    data = release_table.find_all('tr')[1:]
    for row in data:
        columns = row.findAll('td')
        if columns and len(columns) >= 3:
            release_date = columns[2]
            # release_date = columns[0].get_text().strip()
            version = columns[1]
            # version = columns[1].get_text().strip()
            pockets = columns[0]
            # pockets = columns[2].get_text().strip()
            releases.append((version.get_text().strip() if version is not None else '',
                             release_date.get_text().strip() if release_date is not None else '',
                             pockets.get_text().strip() if pockets is not None else '')
                            )
    return releases
