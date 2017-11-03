# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2017
"""
from geomdl import BSpline
from geomdl import utilities

# Create a B-Spline curve instance
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up curve
curve.read_ctrlpts_from_txt("CP_Curve1.txt")
curve.degree = 4

# Auto-generate  knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Calculate curve
curve.evaluate()

# Save control points and evaluated curve points
curve.save_surfpts_to_csv("curve1.csv")
curve.save_ctrlpts_to_csv("ctrlpts1.csv")

print("End of NURBS-Python Example")
