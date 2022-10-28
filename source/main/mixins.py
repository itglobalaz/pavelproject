class FilterByProjectMixin:
    membership_path = ''

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(**{self.membership_path: self.request.user})
        return queryset
