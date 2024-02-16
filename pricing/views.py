from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pricing
from .serializers import PricingSerializer

class CalculatePrice(APIView):
    def get(self, request):
        # Implement the logic to handle GET requests here
        # For example, you can retrieve all pricing data from the database
        pricings = Pricing.objects.all()
        serializer = PricingSerializer(pricings, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Implement the logic to handle POST requests here
        zone = request.data.get('zone')
        organization_id = request.data.get('organization_id')
        total_distance = request.data.get('total_distance')
        item_type = request.data.get('item_type')

        pricing_obj = Pricing.objects.filter(
            organization_id=organization_id,
            zone=zone,
            item__type=item_type
        ).first()

        if pricing_obj:
            base_distance = pricing_obj.base_distance_in_km
            km_price = pricing_obj.km_price_perishable if item_type == 'perishable' else pricing_obj.km_price_non_perishable
            base_price = pricing_obj.base_price

            if total_distance <= base_distance:
                total_price = base_price
            else:
                additional_distance = total_distance - base_distance
                total_price = base_price + (additional_distance * km_price)
            
            return Response({'total_price': total_price})
        else:
            return Response({'error': 'Pricing not found for the given parameters'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # Implement the logic to handle PUT requests here
        return Response({'message': 'PUT method not implemented'}, status=status.HTTP_501_NOT_IMPLEMENTED)

    def delete(self, request):
        # Implement the logic to handle DELETE requests here
        return Response({'message': 'DELETE method not implemented'}, status=status.HTTP_501_NOT_IMPLEMENTED)

    # Implement other HTTP methods as needed
