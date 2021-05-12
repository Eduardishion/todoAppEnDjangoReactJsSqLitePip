

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.response import Response



class listarTodasLasTareasyCrearTarea(APIView):

    # metodo get para listar todas las tareas
    def get(self, request):
        queryset = Tarea.objects.all()
        serializer_class = TareaSerializer(queryset, many=True)
        return Response(serializer_class.data)

    # metodo post para insertar y crear una nueva tarea
    def post(self, request):
        serializer_class = TareaSerializer(data=request.data)
        if (serializer_class.is_valid()):
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)



class ActualizarEliminarTareas(APIView):

    #metodo que obtieene el pk del objeto
    def get_object(self,pk):
        try:
            return Tarea.objects.get(pk=pk)
        except Tarea.DoesNotExist:
            return Response( status=status.HTTP_400_BAD_REQUEST)

    #metodo para mostrar detalle de cada objeto individual
    def get(self,request,pk):
        tmpObj = self.get_object(pk)
        serializer_class = TareaSerializer(tmpObj)
        return Response(serializer_class.data)

    #metodo para actualizar tarea
    def put(self,request,pk):
        tmpObj = self.get_object(pk)
        serializer_class = TareaSerializer(tmpObj,data=request.data)
        if(serializer_class.is_valid()):
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    #metodo para eliminar tarea
    def delete(self,request,pk):
        mpObj = self.get_object(pk)
        mpObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




