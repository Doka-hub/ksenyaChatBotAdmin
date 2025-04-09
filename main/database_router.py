class DBRouter:
    bot_app_labels = ['channels', 'payments', 'tgusers', 'notifications']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.bot_app_labels:
            return 'bot'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.bot_app_labels:
            return 'bot'

    def allow_migrate(self, db, app_label=None, model_name=None, **hints):
        if db == 'bot':
            return False

        if app_label in self.bot_app_labels:
            return False
