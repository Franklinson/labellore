# calculations/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BMRRequestSerializer

class BMRCalculationView(APIView):
    def post(self, request, equation):
        serializer = BMRRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            weight = data.get("weight")
            height = data.get("height")
            age = data.get("age")
            sex = data.get("sex")
            stress_factor = data.get("stress_factor")
            activity_factor = data.get("activity_factor")
            injury_factor = data.get("injury_factor")
            lean_body_mass = data.get("lean_body_mass")
            ffm = data.get("ffm")
            pa = data.get("pa")
            bsa = data.get("bsa")

            bmr = 0
            energy_requirement = None

            if equation == "mifflin_st_jeor":
                if weight is not None and height is not None and age is not None and sex is not None:
                    if sex == "male":
                        bmr = 9.99 * weight + 6.25 * height - 4.92 * age + 5
                    else:
                        bmr = 9.99 * weight + 6.25 * height - 4.92 * age - 161
                    if stress_factor is not None:
                        energy_requirement = bmr * stress_factor
                else:
                    return Response({"error": "Missing required parameters for Mifflin-St Jeor equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "harris_benedict":
                if weight is not None and height is not None and age is not None and sex is not None:
                    if sex == "male":
                        bmr = 66.4730 + 13.7516 * weight + 5.0033 * height - 6.7550 * age
                    else:
                        bmr = 655.0955 + 9.5634 * weight + 1.8496 * height - 4.6756 * age
                    if activity_factor and injury_factor is not None:
                        energy_requirement = bmr * activity_factor * injury_factor
                else:
                    return Response({"error": "Missing required parameters for Harris-Benedict equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "revised_harris_benedict":
                if weight is not None and height is not None and age is not None and sex is not None:
                    if sex == "male":
                        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
                    else:
                        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.33 * age
                    if activity_factor and injury_factor is not None:
                        energy_requirement = bmr * activity_factor * injury_factor
                else:
                    return Response({"error": "Missing required parameters for Revised Harris-Benedict equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "katch_mcardle":
                if lean_body_mass is not None:
                    bmr = 370 + 21.6 * lean_body_mass
                else:
                    return Response({"error": "Missing required parameter lean_body_mass for Katch-McArdle equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "owen":
                if weight is not None and sex is not None:
                    if sex == "male":
                        bmr = 879 + 10.2 * weight
                    else:
                        bmr = 795 + 7.18 * weight
                else:
                    return Response({"error": "Missing required parameters for Owen equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "cunningham_1991":
                if ffm is not None:
                    bmr = 370 + 21.6 * ffm
                else:
                    return Response({"error": "Missing required parameter ffm for Cunningham 1991 equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "cunningham_1980":
                if ffm is not None:
                    bmr = 500 + 22 * ffm
                else:
                    return Response({"error": "Missing required parameter ffm for Cunningham 1980 equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "imna_2002":
                if weight is not None and height is not None and age is not None and sex is not None and pa is not None:
                    if sex == "male":
                        bmr = 662 - 9.53 * age + pa * (15.91 * weight + 539.6 * height)
                    else:
                        bmr = 354 - 6.91 * age + pa * (9.36 * weight + 726 * height)
                else:
                    return Response({"error": "Missing required parameters for IMNA 2002 equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "livingstone":
                if weight is not None and age is not None and sex is not None:
                    if sex == "male":
                        bmr = 293 * weight ** 0.4330 - 5.92 * age
                    else:
                        bmr = 248 * weight ** 0.4356 - 5.09 * age
                else:
                    return Response({"error": "Missing required parameters for Livingstone equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "fleisch":
                if bsa is not None and age is not None and sex is not None:
                    if sex == "male":
                        bmr = 24 * bsa * (38 - 0.073 * (age - 20))
                    else:
                        bmr = 24 * bsa * (35.5 - 0.064 * (age - 20))
                else:
                    return Response({"error": "Missing required parameters for Fleisch equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "henry_oxford":
                if weight is not None and height is not None and age is not None:
                    bmr = 864 - 9.72 * age + 6.8 * weight + 10.2 * height
                else:
                    return Response({"error": "Missing required parameters for Henry Oxford equation"}, status=status.HTTP_400_BAD_REQUEST)

            elif equation == "schofield":
                if weight is not None and height is not None and age is not None and sex is not None:
                    if sex == "male":
                        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
                    else:
                        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.33 * age
                else:
                    return Response({"error": "Missing required parameters for Schofield equation"}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"error": "Invalid equation"}, status=status.HTTP_400_BAD_REQUEST)

            response_data = {"BMR": f"{bmr:.2f}"}
            if energy_requirement:
                response_data["energy_requirement"] = f"{energy_requirement:.2f}kcal"

            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
