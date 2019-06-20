from datetime import timedelta
"""Celery beat schedule that checks a device's last seen every 24 hours"""
beat_schedule = {
    'run-check-device-last-seen-hourly': {
        'task': 'check-device-last-seen',
        'schedule': timedelta(hours=24)
    }
}
