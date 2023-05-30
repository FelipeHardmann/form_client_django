from django.contrib.auth.mixins import UserPassesTestMixin


class GerentePermissionMixin(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        '''Só deixará cadastrar usuários que tiverem cargo de gerente'''
        return self.request.user.cargo == 1
    

class AdminPermissionMixin(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user.is_superuser