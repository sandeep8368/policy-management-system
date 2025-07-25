from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Policy(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="policies")
    policy_type = models.CharField(max_length=100)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    document = models.FileField(upload_to='policy_docs/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Active')
    
    def __str__(self):
        return f"{self.user.username} - {self.policy_type}"
    
    
class Claim(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name="claims")
    claim_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    approved = models.BooleanField(default=False)
        
        
    def __str__(self):
        return f"Claim #{self.id} on {self.policy}"