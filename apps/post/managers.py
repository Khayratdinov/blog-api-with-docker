from django.db.models import Manager
# ============================================================================ #

# =============================== BLOG MANAGER =============================== #

class BlogManager(Manager):
    
    def publish(self):
        return self.filter(is_active=True)

    def select_related_object(self, object):
        return self.select_related(object).filter(is_active=True)

# ============================= CATEGORY MANAGER ============================= #

class CategoryManager(Manager):
    def active(self):
        return self.filter(is_active=True)


# ============================================================================ #