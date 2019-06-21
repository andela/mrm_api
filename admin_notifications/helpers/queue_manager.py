from datetime import timedelta
beat_schedule = {
    'run-check-device-last-seen-hourly': {
        'task': 'check-device-last-seen',
        'schedule': timedelta(seconds=5)
    }
}
