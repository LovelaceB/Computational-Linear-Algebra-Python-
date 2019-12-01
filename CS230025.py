"""Ben Lovelace 
CS 2300 section 1 
Homework 2.5"""
import os 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


Pyramid  = np.loadtxt(fname  = "C:/Users/blove/Desktop/fig1.txt")
Pyramid = Pyramid.astype(int)
print(Pyramid)
#input1.tolist()
#input1 = input1.astype(int)
Cube  = np.loadtxt(fname  = "C:/Users/blove/Desktop/fig2.txt")
Cube = Cube.astype(int)

Rectangular  = np.loadtxt(fname  = "C:/Users/blove/Desktop/fig3.txt")
print(Rectangular)
Complex  = np.loadtxt(fname  = "C:/Users/blove/desktop/fig4.txt")
print(Complex)



figChoice = input("Which figure would you like to see? You can choose from : Pyramid, Cube, Rectangular and Complex.")


if figChoice == "Pyramid":

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')

    #plot the vertices of the pyramid 
    v = np.array(Pyramid)
    ax1.scatter3D(v[:, 0], v[:, 1], v[:, 2])

    # generate list of sides' polygons of our pyramid
    verts = [ [v[0],v[1],v[4]], [v[0],v[3],v[4]],
      [v[2],v[1],v[4]], [v[2],v[3],v[4]], [v[0],v[1],v[2],v[3]]]

    # plot sides
    ax1.add_collection3d(Poly3DCollection(verts, 
        facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    
    TransformationChoice = input("What type of transformation would you like to see? A Translation, Rotation, or Scale?")

    if TransformationChoice == "Rotation":
        Radx = input("Enter the Radians you wish to rotate in the x1 axis, A: pi/2, B: pi , C: 5pi/4")
        if Radx == "A":
            Radx = np.pi/2
        if Radx == "B":
            Radx = np.pi
        if Radx == "C":
            Radx = np.pi/4
        Pyramid1 = np.array([])
        for a in Pyramid:
            a = np.append(a,1)
            Pyramid1 = np.append(Pyramid1, a)
            print(a)
        Pyramid1 = np.reshape(Pyramid1,(5,4))
        print(Pyramid1)
        
        theta = Radx
        c, s = np.cos(theta), np.sin(theta)
        Rx = np.array(((1,0,0,0),(0,c,s,0),(0,-s,c,0),(0,0,0,1)))
        result = np.array([])
        for i in Pyramid1:
            print(i)
            n = np.matmul(Rx,i)
            result = np.append(result, n)
        result = np.reshape(result,(5,4))
        print(result)

        Rady = input("Enter the Radians you wish to rotate in the x2 axis, A: pi/2, B: pi , C: 5pi/4")
        if Rady == "A":
            Rady = np.pi/2
        if Rady == "B":
            Rady = np.pi
        if Rady == "C":
            Rady = np.pi/4

        theta = Rady
        c, s = np.cos(theta), np.sin(theta)
        Ry = np.array(((c,0,-s,0),(0,1,0,0),(s,0,c,0),(0,0,0,1)))
        result2 = np.array([])
        for i in result:
            n = np.matmul(Ry,i)
            print(n)
            result2 = np.append(result2, n)

        result2 = np.reshape(result2,(5,4))
        print(result2)

        Radz = input("Enter the Radians you wish to rotate in the x3 axis, A: pi/2, B: pi , C: 5pi/4")
        if Radz == "A":
            Radz = np.pi/2
        if Radz == "B":
            Radz = np.pi
        if Radz == "C":
            Radz = np.pi/4

        theta = Radz
        c, s = np.cos(theta), np.sin(theta)
        Rz = np.array(((c,s,0,0),(-s,c,0,0),(0,0,1,0),(0,0,0,1)))
        result3 = np.array([])
        for i in result2:
            n = np.matmul(Rz,i)
            print(n)
            result3 = np.append(result3, n)

        result3 = np.reshape(result3,(5,4))
        print(result3)
        finalRotatedMatrix = np.array([])
        for i in result3:
            n = np.delete(i, -1)
            finalRotatedMatrix = np.append(finalRotatedMatrix, n)
        finalRotatedMatrix = np.reshape(finalRotatedMatrix,(5,3))
        print(finalRotatedMatrix, file=open("File1_Rotation.txt", "a"))
        
        j = np.array(finalRotatedMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our pyramid
        verts = [ [j[0],j[1],j[4]], [j[0],j[3],j[4]],
            [j[2],j[1],j[4]], [j[2],j[3],j[4]], [j[0],j[1],j[2],j[3]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

    if TransformationChoice == "Translation":
        Vx = int(input("Enter V1 of translation vector"))    
        
        Vy = int(input("Enter V2 of translation vector"))
        
        Vz = int(input("Enter V3 of translation vector"))
       
        TranslationMatrix = np.array(((1,0,0,Vx),(0,1,0,Vy),(0,0,1,Vz),(0,0,0,1)))
        TranslationResult = np.array([])

        Pyramid1 = np.array([])
        for a in Pyramid:
            a = np.append(a,1)
            Pyramid1 = np.append(Pyramid1, a)
            print(a)
        Pyramid1 = np.reshape(Pyramid1,(5,4))

        print(Pyramid1)

        for i in Pyramid1:
            n = np.matmul(TranslationMatrix,i)
            TranslationResult = np.append(TranslationResult, n)
        TranslationResult = np.reshape(TranslationResult,(5,4))
        print(TranslationResult)
        
        finalTranslatedMatrix = np.array([])
        
        for i in TranslationResult:
            n = np.delete(i, -1)
            finalTranslatedMatrix = np.append(finalTranslatedMatrix, n)
        finalTranslatedMatrix = np.reshape(finalTranslatedMatrix,(5,3))
        print(finalTranslatedMatrix, file=open("File1_Translation.txt", "a"))
        
        j = np.array(finalTranslatedMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our pyramid
        verts = [ [j[0],j[1],j[4]], [j[0],j[3],j[4]],
            [j[2],j[1],j[4]], [j[2],j[3],j[4]], [j[0],j[1],j[2],j[3]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

    if TransformationChoice == "Scale":
        Vx = int(input("Enter V1 of Scale vector"))    
        
        Vy = int(input("Enter V2 of Scale vector"))
        
        Vz = int(input("Enter V3 of Scale vector"))

        ScalingMatrix = np.array(((Vx,0,0,0),(0,Vy,0,0),(0,0,Vz,0),(0,0,0,1)))

        ScalingResult = np.array([])

        Pyramid1 = np.array([])
        for a in Pyramid:
            a = np.append(a,1)
            Pyramid1 = np.append(Pyramid1, a)
            print(a)
        Pyramid1 = np.reshape(Pyramid1,(5,4))

        print(Pyramid1)

        for i in Pyramid1:
            n = np.matmul(ScalingMatrix,i)
            ScalingResult = np.append(ScalingResult, n)
        ScalingResult = np.reshape(ScalingResult,(5,4))
        print(ScalingResult)
        
        finalScaledMatrix = np.array([])
        
        for i in ScalingResult:
            n = np.delete(i, -1)
            finalScaledMatrix = np.append(finalScaledMatrix, n)
        finalScaledMatrix = np.reshape(finalScaledMatrix,(5,3))
        print(finalScaledMatrix, file=open("File1_Scale.txt", "a"))
        
        j = np.array(finalScaledMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our pyramid
        verts = [ [j[0],j[1],j[4]], [j[0],j[3],j[4]],
            [j[2],j[1],j[4]], [j[2],j[3],j[4]], [j[0],j[1],j[2],j[3]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()
       

"""
Start of Cube 

"""


if figChoice == "Cube":

    fig2 = plt.figure()     
    ax1 = fig2.add_subplot(111, projection='3d')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')

    #plot the vertices of the pyramid 
    l = np.array(Cube)
    ax1.scatter3D(l[:, 0], l[:, 1], l[:, 2])

    # generate list of sides' polygons of our Cube
    verts = [[l[7],l[6],l[5],l[4]], [l[1],l[0],l[5],l[6]],[l[7],l[6],l[1],l[2]], [l[7],l[4],l[3],l[2]], [l[0],l[5],l[4],l[3]], [l[0],l[3],l[2],l[1]]]
  

    # plot sides
    ax1.add_collection3d(Poly3DCollection(verts, 
    facecolors='r', linewidths=1, edgecolors='b', alpha=.25))

    

    TransformationChoice = input("What type of transformation would you like to see? A Translation, Rotation, or Scale?")

    if TransformationChoice == "Rotation":
        Radx = input("Enter the Radians you wish to rotate in the x1 axis, A: pi/2, B: pi , C: 5pi/4")
        if Radx == "A":
            Radx = np.pi/2
        if Radx == "B":
            Radx = np.pi
        if Radx == "C":
            Radx = np.pi/4
        Cube1 = np.array([])
        for a in Cube:
            a = np.append(a,1)
            Cube1 = np.append(Cube1, a)
        Cube1 = np.reshape(Cube1,(8,4))
        print(Cube1)
        
        theta = Radx
        c, s = np.cos(theta), np.sin(theta)
        Rx = np.array(((1,0,0,0),(0,c,s,0),(0,-s,c,0),(0,0,0,1)))
        result = np.array([])
        for i in Cube1:
            print(i)
            n = np.matmul(Rx,i)
            result = np.append(result, n)
        result = np.reshape(result,(8,4))
        print(result)

        Rady = input("Enter the Radians you wish to rotate in the x2 axis, A: pi/2, B: pi , C: 5pi/4")
        if Rady == "A":
            Rady = np.pi/2
        if Rady == "B":
            Rady = np.pi
        if Rady == "C":
            Rady = np.pi/4

        theta = Rady
        c, s = np.cos(theta), np.sin(theta)
        Ry = np.array(((c,0,-s,0),(0,1,0,0),(s,0,c,0),(0,0,0,1)))
        result2 = np.array([])
        for i in result:
            n = np.matmul(Ry,i)
            print(n)
            result2 = np.append(result2, n)

        result2 = np.reshape(result2,(8,4))
        print(result2)

        Radz = input("Enter the Radians you wish to rotate in the x3 axis, A: pi/2, B: pi , C: 5pi/4")
        if Radz == "A":
            Radz = np.pi/2
        if Radz == "B":
            Radz = np.pi
        if Radz == "C":
            Radz = np.pi/4

        theta = Radz
        c, s = np.cos(theta), np.sin(theta)
        Rz = np.array(((c,s,0,0),(-s,c,0,0),(0,0,1,0),(0,0,0,1)))
        result3 = np.array([])
        for i in result2:
            n = np.matmul(Rz,i)
            print(n)
            result3 = np.append(result3, n)

        result3 = np.reshape(result3,(8,4))
        print(result3)
        finalRotatedMatrix = np.array([])
        for i in result3:
            n = np.delete(i, -1)
            finalRotatedMatrix = np.append(finalRotatedMatrix, n)
        finalRotatedMatrix = np.reshape(finalRotatedMatrix,(8,3))
        print(finalRotatedMatrix, file=open("File2_Rotation.txt", "a"))
        
        j = np.array(finalRotatedMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our cube
        verts = [[l[7],l[6],l[5],l[4]], [l[1],l[0],l[5],l[6]],[l[7],l[6],l[1],l[2]], [l[7],l[4],l[3],l[2]], [l[0],l[5],l[4],l[3]], [l[0],l[3],l[2],l[1]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

    if TransformationChoice == "Translation":
        Vx = int(input("Enter V1 of translation vector"))    
        
        Vy = int(input("Enter V2 of translation vector"))
        
        Vz = int(input("Enter V3 of translation vector"))
       
        TranslationMatrix = np.array(((1,0,0,Vx),(0,1,0,Vy),(0,0,1,Vz),(0,0,0,1)))
        TranslationResult = np.array([])

        Cube1 = np.array([])
        for a in Cube:
            a = np.append(a,1)
            Cube1 = np.append(Cube1, a)
            print(a)
        Cube1 = np.reshape(Cube1,(8,4))

        print(Cube1)

        for i in Cube1:
            n = np.matmul(TranslationMatrix,i)
            TranslationResult = np.append(TranslationResult, n)
        TranslationResult = np.reshape(TranslationResult,(8,4))
        print(TranslationResult)
        
        finalTranslatedMatrix = np.array([])
        
        for i in TranslationResult:
            n = np.delete(i, -1)
            finalTranslatedMatrix = np.append(finalTranslatedMatrix, n)
        finalTranslatedMatrix = np.reshape(finalTranslatedMatrix,(8,3))
        print(finalTranslatedMatrix, file=open("File2_Translation.txt", "a"))
        
        j = np.array(finalTranslatedMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our Cube
        verts = [[l[7],l[6],l[5],l[4]], [l[1],l[0],l[5],l[6]],[l[7],l[6],l[1],l[2]], [l[7],l[4],l[3],l[2]], [l[0],l[5],l[4],l[3]], [l[0],l[3],l[2],l[1]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='r', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

    if TransformationChoice == "Scale":
        Vx = int(input("Enter V1 of Scale vector"))    
        
        Vy = int(input("Enter V2 of Scale vector"))
        
        Vz = int(input("Enter V3 of Scale vector"))

        ScalingMatrix = np.array(((Vx,0,0,0),(0,Vy,0,0),(0,0,Vz,0),(0,0,0,1)))

        ScalingResult = np.array([])

        Cube1 = np.array([])
        for a in Cube:
            a = np.append(a,1)
            Cube1 = np.append(Cube1, a)
            print(a)
        Cube1 = np.reshape(Cube1,(8,4))

        print(Cube1)

        for i in Cube1:
            n = np.matmul(ScalingMatrix,i)
            ScalingResult = np.append(ScalingResult, n)
        ScalingResult = np.reshape(ScalingResult,(8,4))
        print(ScalingResult)
        
        finalScaledMatrix = np.array([])
        
        for i in ScalingResult:
            n = np.delete(i, -1)
            finalScaledMatrix = np.append(finalScaledMatrix, n)
        finalScaledMatrix = np.reshape(finalScaledMatrix,(8,3))
        print(finalScaledMatrix, file=open("File2_Scale.txt", "a"))
        
        j = np.array(finalScaledMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our Cube
        verts = [[l[7],l[6],l[5],l[4]], [l[1],l[0],l[5],l[6]],[l[7],l[6],l[1],l[2]], [l[7],l[4],l[3],l[2]], [l[0],l[5],l[4],l[3]], [l[0],l[3],l[2],l[1]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

"""
Start of Rectangular

"""


if figChoice == "Rectangular":

    fig2 = plt.figure()     
    ax1 = fig2.add_subplot(111, projection='3d')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')

    #plot the vertices of the pyramid 
    l = np.array(Rectangular)
    ax1.scatter3D(l[:, 0], l[:, 1], l[:, 2])

    # generate list of sides' polygons of our Rectangle
    verts = [[l[7],l[6],l[5],l[4]], [l[1],l[0],l[5],l[6]],[l[7],l[6],l[1],l[2]], [l[7],l[4],l[3],l[2]], [l[0],l[5],l[4],l[3]], [l[0],l[3],l[2],l[1]]]
  

    # plot sides
    ax1.add_collection3d(Poly3DCollection(verts, 
    facecolors='r', linewidths=1, edgecolors='b', alpha=.25))

    

    TransformationChoice = input("What type of transformation would you like to see? A Translation, Rotation, or Scale?")

    if TransformationChoice == "Rotation":
        Radx = input("Enter the Radians you wish to rotate in the x1 axis, A: pi/2, B: pi , C: 5pi/4")
        if Radx == "A":
            Radx = np.pi/2
        if Radx == "B":
            Radx = np.pi
        if Radx == "C":
            Radx = np.pi/4
        Rectangle1 = np.array([])
        for a in Rectangular:
            a = np.append(a,1)
            Rectangle1 = np.append(Rectangle1, a)
        Rectangle1 = np.reshape(Rectangle1,(8,4))
        print(Rectangle1)
        
        theta = Radx
        c, s = np.cos(theta), np.sin(theta)
        Rx = np.array(((1,0,0,0),(0,c,s,0),(0,-s,c,0),(0,0,0,1)))
        result = np.array([])
        for i in Rectangle1:
            print(i)
            n = np.matmul(Rx,i)
            result = np.append(result, n)
        result = np.reshape(result,(8,4))
        print(result)

        Rady = input("Enter the Radians you wish to rotate in the x2 axis, A: pi/2, B: pi , C: 5pi/4")
        if Rady == "A":
            Rady = np.pi/2
        if Rady == "B":
            Rady = np.pi
        if Rady == "C":
            Rady = np.pi/4

        theta = Rady
        c, s = np.cos(theta), np.sin(theta)
        Ry = np.array(((c,0,-s,0),(0,1,0,0),(s,0,c,0),(0,0,0,1)))
        result2 = np.array([])
        for i in result:
            n = np.matmul(Ry,i)
            print(n)
            result2 = np.append(result2, n)

        result2 = np.reshape(result2,(8,4))
        print(result2)

        Radz = input("Enter the Radians you wish to rotate in the x3 axis, A: pi/2, B: pi , C: 5pi/4")
        if Radz == "A":
            Radz = np.pi/2
        if Radz == "B":
            Radz = np.pi
        if Radz == "C":
            Radz = np.pi/4

        theta = Radz
        c, s = np.cos(theta), np.sin(theta)
        Rz = np.array(((c,s,0,0),(-s,c,0,0),(0,0,1,0),(0,0,0,1)))
        result3 = np.array([])
        for i in result2:
            n = np.matmul(Rz,i)
            print(n)
            result3 = np.append(result3, n)

        result3 = np.reshape(result3,(8,4))
        print(result3)
        finalRotatedMatrix = np.array([])
        for i in result3:
            n = np.delete(i, -1)
            finalRotatedMatrix = np.append(finalRotatedMatrix, n)
        finalRotatedMatrix = np.reshape(finalRotatedMatrix,(8,3))
        print(finalRotatedMatrix, file=open("File3_Rotation.txt", "a"))
        
        j = np.array(finalRotatedMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our Rectangle
        verts = [[l[7],l[6],l[5],l[4]], [l[1],l[0],l[5],l[6]],[l[7],l[6],l[1],l[2]], [l[7],l[4],l[3],l[2]], [l[0],l[5],l[4],l[3]], [l[0],l[3],l[2],l[1]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

    if TransformationChoice == "Translation":
        Vx = int(input("Enter V1 of translation vector"))    
        
        Vy = int(input("Enter V2 of translation vector"))
        
        Vz = int(input("Enter V3 of translation vector"))
       
        TranslationMatrix = np.array(((1,0,0,Vx),(0,1,0,Vy),(0,0,1,Vz),(0,0,0,1)))
        TranslationResult = np.array([])

        Rectangle1 = np.array([])
        for a in Rectangular:
            a = np.append(a,1)
            Rectangle1 = np.append(Rectangle1, a)
            print(a)
        Rectangle1 = np.reshape(Rectangle1,(8,4))

        print(Rectangle1)

        for i in Rectangle1:
            n = np.matmul(TranslationMatrix,i)
            TranslationResult = np.append(TranslationResult, n)
        TranslationResult = np.reshape(TranslationResult,(8,4))
        print(TranslationResult)
        
        finalTranslatedMatrix = np.array([])
        
        for i in TranslationResult:
            n = np.delete(i, -1)
            finalTranslatedMatrix = np.append(finalTranslatedMatrix, n)
        finalTranslatedMatrix = np.reshape(finalTranslatedMatrix,(8,3))
        print(finalTranslatedMatrix, file=open("File3_Translation.txt", "a"))
        
        j = np.array(finalTranslatedMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our Rectangular
        verts = [[l[7],l[6],l[5],l[4]], [l[1],l[0],l[5],l[6]],[l[7],l[6],l[1],l[2]], [l[7],l[4],l[3],l[2]], [l[0],l[5],l[4],l[3]], [l[0],l[3],l[2],l[1]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='r', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

    if TransformationChoice == "Scale":
        Vx = int(input("Enter V1 of Scale vector"))    
        
        Vy = int(input("Enter V2 of Scale vector"))
        
        Vz = int(input("Enter V3 of Scale vector"))

        ScalingMatrix = np.array(((Vx,0,0,0),(0,Vy,0,0),(0,0,Vz,0),(0,0,0,1)))

        ScalingResult = np.array([])

        Rectangle1 = np.array([])
        for a in Cube:
            a = np.append(a,1)
            Rectangle1 = np.append(Rectangle1, a)
            print(a)
        Rectangle1 = np.reshape(Rectangle1,(8,4))

        print(Rectangle1)

        for i in Rectangle1:
            n = np.matmul(ScalingMatrix,i)
            ScalingResult = np.append(ScalingResult, n)
        ScalingResult = np.reshape(ScalingResult,(8,4))
        print(ScalingResult)
        
        finalScaledMatrix = np.array([])
        
        for i in ScalingResult:
            n = np.delete(i, -1)
            finalScaledMatrix = np.append(finalScaledMatrix, n)
        finalScaledMatrix = np.reshape(finalScaledMatrix,(8,3))
        print(finalScaledMatrix, file=open("File3_Scale.txt", "a"))
        
        j = np.array(finalScaledMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our Rectangular
        verts = [[l[7],l[6],l[5],l[4]], [l[1],l[0],l[5],l[6]],[l[7],l[6],l[1],l[2]], [l[7],l[4],l[3],l[2]], [l[0],l[5],l[4],l[3]], [l[0],l[3],l[2],l[1]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()


"""
Complex

"""

if figChoice == "Complex":

    fig2 = plt.figure()     
    ax1 = fig2.add_subplot(111, projection='3d')
    ax1.set_xlabel('X1')
    ax1.set_ylabel('X2')
    ax1.set_zlabel('X3')

    #plot the vertices of the pyramid 
    l = np.array(Complex)
    ax1.scatter3D(l[:, 0], l[:, 1], l[:, 2])

    # generate list of sides' polygons of our Complex Figure
    verts = [[l[0],l[1],l[2],l[3],l[4]], [l[1],l[2],l[8],l[7]],[l[0],l[1],l[6],l[7]], [l[0],l[4],l[5],l[6]], [l[3],l[4],l[5],l[9]], [l[2],l[3],l[8],l[9]], [l[8],l[7],l[6],l[5],l[9]]]
  

    # plot sides
    ax1.add_collection3d(Poly3DCollection(verts, 
    facecolors='r', linewidths=1, edgecolors='b', alpha=.25))

    

    TransformationChoice = input("What type of transformation would you like to see? A Translation, Rotation, or Scale?")

    if TransformationChoice == "Rotation":
        Radx = input("Enter the Radians you wish to rotate in the x1 axis, A: pi/2, B: pi , C: 5pi/4")
        if Radx == "A":
            Radx = np.pi/2
        if Radx == "B":
            Radx = np.pi
        if Radx == "C":
            Radx = np.pi/4
        Complex1 = np.array([])
        for a in Complex:
            a = np.append(a,1)
            Complex1 = np.append(Complex1, a)
        Complex1 = np.reshape(Complex1,(10,4))
        print(Complex1)
        
        theta = Radx
        c, s = np.cos(theta), np.sin(theta)
        Rx = np.array(((1,0,0,0),(0,c,s,0),(0,-s,c,0),(0,0,0,1)))
        result = np.array([])
        for i in Complex1:
            print(i)
            n = np.matmul(Rx,i)
            result = np.append(result, n)
        result = np.reshape(result,(10,4))
        print(result)

        Rady = input("Enter the Radians you wish to rotate in the x2 axis, A: pi/2, B: pi , C: 5pi/4")
        if Rady == "A":
            Rady = np.pi/2
        if Rady == "B":
            Rady = np.pi
        if Rady == "C":
            Rady = np.pi/4

        theta = Rady
        c, s = np.cos(theta), np.sin(theta)
        Ry = np.array(((c,0,-s,0),(0,1,0,0),(s,0,c,0),(0,0,0,1)))
        result2 = np.array([])
        for i in result:
            n = np.matmul(Ry,i)
            print(n)
            result2 = np.append(result2, n)

        result2 = np.reshape(result2,(10,4))
        print(result2)

        Radz = input("Enter the Radians you wish to rotate in the x3 axis, A: pi/2, B: pi , C: 5pi/4")
        if Radz == "A":
            Radz = np.pi/2
        if Radz == "B":
            Radz = np.pi
        if Radz == "C":
            Radz = np.pi/4

        theta = Radz
        c, s = np.cos(theta), np.sin(theta)
        Rz = np.array(((c,s,0,0),(-s,c,0,0),(0,0,1,0),(0,0,0,1)))
        result3 = np.array([])
        for i in result2:
            n = np.matmul(Rz,i)
            print(n)
            result3 = np.append(result3, n)

        result3 = np.reshape(result3,(10,4))
        print(result3)
        finalRotatedMatrix = np.array([])
        for i in result3:
            n = np.delete(i, -1)
            finalRotatedMatrix = np.append(finalRotatedMatrix, n)
        finalRotatedMatrix = np.reshape(finalRotatedMatrix,(10,3))
        print(finalRotatedMatrix, file=open("File4_Rotation.txt", "a"))
        
        j = np.array(finalRotatedMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our Complex Fugure
        verts = [[l[0],l[1],l[2],l[3],l[4]], [l[1],l[2],l[8],l[7]],[l[0],l[1],l[6],l[7]], [l[0],l[4],l[5],l[6]], [l[3],l[4],l[5],l[9]], [l[2],l[3],l[8],l[9]], [l[8],l[7],l[6],l[5],l[9]]]
        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

    if TransformationChoice == "Translation":
        Vx = int(input("Enter V1 of translation vector"))    
        
        Vy = int(input("Enter V2 of translation vector"))
        
        Vz = int(input("Enter V3 of translation vector"))
       
        TranslationMatrix = np.array(((1,0,0,Vx),(0,1,0,Vy),(0,0,1,Vz),(0,0,0,1)))
        TranslationResult = np.array([])

        Complex1 = np.array([])
        for a in Complex:
            a = np.append(a,1)
            Complex1 = np.append(Complex1, a)
            print(a)
        Complex1 = np.reshape(Complex1,(10,4))

        print(Complex1)

        for i in Complex1:
            n = np.matmul(TranslationMatrix,i)
            TranslationResult = np.append(TranslationResult, n)
        TranslationResult = np.reshape(TranslationResult,(10,4))
        print(TranslationResult)
        
        finalTranslatedMatrix = np.array([])
        
        for i in TranslationResult:
            n = np.delete(i, -1)
            finalTranslatedMatrix = np.append(finalTranslatedMatrix, n)
        finalTranslatedMatrix = np.reshape(finalTranslatedMatrix,(10,3))
        print(finalTranslatedMatrix, file=open("File4_Translation.txt", "a"))
        
        j = np.array(finalTranslatedMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our Complex Figure
        verts = [[l[0],l[1],l[2],l[3],l[4]], [l[1],l[2],l[8],l[7]],[l[0],l[1],l[6],l[7]], [l[0],l[4],l[5],l[6]], [l[3],l[4],l[5],l[9]], [l[2],l[3],l[8],l[9]], [l[8],l[7],l[6],l[5],l[9]]]
        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='r', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()

    if TransformationChoice == "Scale":
        Vx = int(input("Enter V1 of Scale vector"))    
        
        Vy = int(input("Enter V2 of Scale vector"))
        
        Vz = int(input("Enter V3 of Scale vector"))

        ScalingMatrix = np.array(((Vx,0,0,0),(0,Vy,0,0),(0,0,Vz,0),(0,0,0,1)))

        ScalingResult = np.array([])

        Complex1 = np.array([])
        for a in Complex:
            a = np.append(a,1)
            Complex1 = np.append(Complex1, a)
            print(a)
        Complex1 = np.reshape(Complex1,(10,4))

        print(Complex1)

        for i in Complex1:
            n = np.matmul(ScalingMatrix,i)
            ScalingResult = np.append(ScalingResult, n)
        ScalingResult = np.reshape(ScalingResult,(10,4))
        print(ScalingResult)
        
        finalScaledMatrix = np.array([])
        
        for i in ScalingResult:
            n = np.delete(i, -1)
            finalScaledMatrix = np.append(finalScaledMatrix, n)
        finalScaledMatrix = np.reshape(finalScaledMatrix,(10,3))
        print(finalScaledMatrix, file=open("File4_Scale.txt", "a"))
        
        j = np.array(finalScaledMatrix)
        print(j)
        ax1.scatter3D(j[:, 0], j[:, 1], j[:, 2])

        # generate list of sides' polygons of our Complex figure
        verts = [[l[0],l[1],l[2],l[3],l[4]], [l[1],l[2],l[8],l[7]],[l[0],l[1],l[6],l[7]], [l[0],l[4],l[5],l[6]], [l[3],l[4],l[5],l[9]], [l[2],l[3],l[8],l[9]], [l[8],l[7],l[6],l[5],l[9]]]

        # plot sides
        ax1.add_collection3d(Poly3DCollection(verts, 
            facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        
        plt.show()
