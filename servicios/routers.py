from rest_framework import routers
from modulos.facturas.views import FacturaViewSet
from modulos.facturas.views import DetalleFacturaViewSet
from modulos.pedidos.views import PedidoViewSet
from modulos.perfiles.views import PerfilViewSet
from modulos.productos.views import ProductoViewSet

__author__ = 'franc'
router = routers.DefaultRouter()


router.register(r'perfiles', PerfilViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'detalle-facturas', DetalleFacturaViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'productos', ProductoViewSet)

