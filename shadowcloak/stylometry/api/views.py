
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from rest_framework import mixins
from stylometry.models import Author, Document, Group
from stylometry.api.permissions import IsOwnerOrReadOnly
from stylometry.api.serializers import AuthorSerializer, DocumentSerializer, GroupSerializer

from stylometry.api.services.retrieve_documents import create_dictionary
from stylometry.api.services.analysis import mendenhall_characteristic_curves_of_composition, john_burrows_delta_method



class AuthorViewset(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    
class DocumentViewset(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        author_id = self.request.data.get('author')
        author = Author.objects.filter(pk=author_id).first()

        user = self.request.user
        group = self.request.data.get('group')

        if author == None:
            documents_dictionary = create_dictionary(user, group)
            # mendenhall_characteristic_curves_of_composition(documents_dictionary)
            john_burrows_delta_method(documents_dictionary, self.request.data.get('body'))

        elif author.user != user: 
            raise NotFound('Author ' + str(author) + ' not found!')
        else:
            serializer.save(author=author)


    def get_queryset(self):
        author = self.request.query_params.get('author', None)
        if author is not None:
            return self.queryset.filter(author__pseudonym=author)
        return self.queryset.filter(author__user__username=self.request.user)
        


    
class GroupViewset(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

# class AvatarUpdateView(generics.UpdateAPIView):
#     serializer_class = AuthorAvatarSerializer
#     permission_classes = [IsAuthenticated, IsOwnOrReadOnly]

#     def get_object(self):
#         author_object = self.request.user
#         return author_object