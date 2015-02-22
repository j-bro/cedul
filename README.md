# Cedul

Idea by @al-duss for a Doodle like scheduling app to find the idea time for an event by polling participants for their availabilities. Worked on at McHacks 2015.

## Current implementation
- Scheduler backend: incomplete
- Scheduler display: incomplete
- DB: complete
- Create event: complete
- Key lookup: complete

## Setup

- On first run: ```python manage.py migrate```
- Put your secret key in ```secrets.py``` as ```SECRET_KEY```
- Start development server with ```python manage.py runserver```