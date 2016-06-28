from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active = True)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length = 50, unique = True, help_text = 'Unique value for category page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default = True)
    meta_keywords = models.CharField('Meta Keywords', max_length = 255, help_text = 'Comma delimited set of SEO keywords for meta tag')
    meta_description = models.CharField('Meta Description', max_length = 255, help_text = 'Content for description meta Tag')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()
    active = ActiveCategoryManager()

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category', args=(self.slug,))

class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(is_active = True)

class FeaturedProductManager(models.Manager):
    def all(self):
        return super(FeaturedProductManager, self).all().filter(is_active = True).filter(is_featured = True)


class Product(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=128, unique = True)
    slug = models.SlugField(max_length = 128, unique = True, help_text = 'Unique value for product page url, created from name.')
    sku = models.CharField(max_length = 50, unique = True)
    description = models.TextField()
    size = models.IntegerField(default = 750)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    old_price = models.DecimalField(max_digits=7, decimal_places=2, blank = True, default = 0.00)
    picture = models.ImageField(upload_to='products', blank=True)
    is_active = models.BooleanField(default = True)
    is_featured = models.BooleanField(default = True)
    meta_keywords = models.CharField('Meta Keywords', max_length = 255, help_text = 'Comma delimited set of SEO keywords for meta tag')
    meta_description = models.CharField('Meta Description', max_length = 255, help_text = 'Content for description meta Tag')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    views = models.IntegerField(default=0)
    objects = models.Manager()
    active = ActiveProductManager()
    featured = FeaturedProductManager()

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('product', args=(self.category.slug, self.slug,))

    @property
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None

    def cross_sells_hybrid(self):

        from spiritbuzz.models import Order, OrderItem
        from django.contrib.auth.models import User
        from django.db.models import Q

        orders = Order.objects.filter(orderitem__product = self)
        users = User.objects.filter(order__orderitem__product = self)
        items = OrderItem.objects.filter(Q(order__user__in = users)).exclude(product = self)
        products = Product.active.filter(orderitem__in = items).distinct()

        return products

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #isAdmin = models.BooleanField()
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username


class SearchTerm(models.Model):

    q = models.CharField(max_length = 50)
    search_date = models.DateTimeField(auto_now_add = True)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, null = True)
    tracking_id = models.CharField(max_length = 50, default = '')

    def __str__(self):
        return self.q

class PageView(models.Model):

    class Meta:
        abstract = True

    date = models.DateTimeField(auto_now = True)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, null = True)
    tracking_id = models.CharField(max_length = 50, default = '')

class ProductView(PageView):
    product = models.ForeignKey(Product)

class ActiveProductReviewManager(models.Manager):

    def all(self):
        return super(ActiveProductReviewManager, self).all().filter(is_approved = True)

class ProductReview(models.Model):

    RATINGS = [(5,5),(4,4),(3,3),(2,2),(1,1),]
    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now_add = True)
    rating = models.PositiveSmallIntegerField(default = 5, choices = RATINGS)
    is_approved = models.BooleanField(default = True)
    content = models.TextField()
    objects = models.Manager()
approved = ActiveProductReviewManager()