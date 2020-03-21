import os
from io import BytesIO
from PIL import Image

from django.core.files.base import ContentFile
from rest_framework import viewsets, routers
from rest_framework.response import Response
from rest_framework.views import APIView

from greenkoffBack.models import Product, Service
from greenkoffBack.serializers import ProductSerializer, ServiceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UploadImage(APIView):
    def patch(self, request, product_id):
        logo1 = self.request.FILES.get('image1')
        logo2 = self.request.FILES.get('image2')
        logo3 = self.request.FILES.get('image3')
        logo4 = self.request.FILES.get('image4')

        logo_contents1 = logo1.read() if logo1 else None
        logo_contents2 = logo2.read() if logo2 else None
        logo_contents3 = logo3.read() if logo3 else None
        logo_contents4 = logo4.read() if logo4 else None

        f1 = BytesIO(logo_contents1) if logo_contents1 else None
        f2 = BytesIO(logo_contents2) if logo_contents2 else None
        f3 = BytesIO(logo_contents3) if logo_contents3 else None
        f4 = BytesIO(logo_contents4) if logo_contents4 else None

        try:
            if f1:
                Image.open(f1)
            if f2:
                Image.open(f2)
            if f3:
                Image.open(f3)
            if f4:
                Image.open(f4)
        except:
            return Response(status=400, data="Not a valid image")
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(status=400, data="Company #{} does not exist.".format(product))

        old_filename1 = None
        old_filename2 = None
        old_filename3 = None
        old_filename4 = None

        if product.image1:
            old_filename1 = product.image1.path
        if product.image2:
            old_filename2 = product.image2.path
        if product.image3:
            old_filename3 = product.image3.path
        if product.image4:
            old_filename4 = product.image4.path

        if logo_contents1:
            product.image1.save("{}_{}".format(product.pk, 'image1'), ContentFile(logo_contents1))
        if logo_contents2:
            product.image2.save("{}_{}".format(product.pk, 'image1'), ContentFile(logo_contents2))
        if logo_contents3:
            product.image3.save("{}_{}".format(product.pk, 'image1'), ContentFile(logo_contents3))
        if logo_contents4:
            product.image4.save("{}_{}".format(product.pk, 'image1'), ContentFile(logo_contents4))

        if old_filename1 and os.path.isfile(old_filename1):
            os.remove(old_filename1)
        if old_filename2 and os.path.isfile(old_filename2):
            os.remove(old_filename2)
        if old_filename3 and os.path.isfile(old_filename3):
            os.remove(old_filename3)
        if old_filename4 and os.path.isfile(old_filename4):
            os.remove(old_filename4)

        return Response('success naxyu')


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


router = routers.DefaultRouter()

router.register(r'api/products', ProductViewSet)
router.register(r'api/services', ServiceViewSet)
