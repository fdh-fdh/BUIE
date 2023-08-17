from BRep import *

# load stl file
filename = "bunny_small.stl"

# # brep1.show()
brep1 = BRep.from_STL("bunny_small.stl")
# # --- Transformationsvektor ermitteln und Geometrie möglichst nahe an den Ursprung verschieben ---
#
# # min und max x,y,z mit passender Methode in BRep Klasse ermitteln und in der Konsole ausgeben
x_min1, x_max1, y_min1, y_max1, z_min1, z_max1 = brep1.get_min_max()
#
#
# # Geometrie möglichst nahe in den Ursprung verschieben
brep1.move_to_origin(x_min1, y_min1, z_min1)

#
# # nochmal min und max ermitteln. mins sollten nun alle 0 sein
x_min2, x_max2, y_min2, y_max2, z_min2, z_max2 = brep1.get_min_max()
#
# # Kontrolle-Visualisierung
brep1.show()
a = brep1.faces

# --- Backface culling ---
reduced_flist = brep1.apply_backface_culling()

# neue BRep Instanz mit reduzierter Dreiecks-Liste erstellen
reduced_brep = BRep(reduced_flist)

# Kontroll-Visualisierung
reduced_brep.show()

# --- Projektion auf xz Ebene und Rasterisierung ---

# Projektion aller Dreiecke auf die xz-Ebene mit geeigneter Methode der BRep Klasse durchführen
reduced_brep.project_onto_xz_plane()

# Auflösung des Bildes definieren (Anzahl Pixel an der langen Seite)
max_pix = 50
# Auflösung des Bildes definieren (Anzahl Pixel an der kürzen Seite)
if x_max2 < z_max2:
    n_pix_x = int(x_max2 * max_pix / z_max2)
    n_pix_z = max_pix
else:
    n_pix_z = int((z_max2 * max_pix) / x_max2)
    n_pix_x = max_pix

# Je nachdem ob Ausdehnung in x- oder z-Richtung größer ist,
# muss die Anzahl der Pixel für die jeweils andere Seite bestimmt werden,
# damit das Bild im Anschluss im richtigen Verhältnis dargestellt wird

print("x-Pixel: ", n_pix_x)
print("z-Pixel: ", n_pix_z)

# Leinwand erstellen (Matrix aller Pixel jeweils mit 1=weiß belegt)
img = np.ones((n_pix_x, n_pix_z), np.int8)

# Abstand der Mittelpunkte der Pixel in Bezug auf das Koordinatensystem berechnen

# Das ist die Schrittweite mit der das Koordinatensystem abgetastet wird
stepx = int(x_max2 / n_pix_x)
stepz = int(z_max2 / n_pix_z)

# Für jedes Dreieck prüfen welche Pixel innerhalb des Dreiecks liegen
# Dazu für alle Pixel prüfen, ob die Koordinaten des Mittelpunkts des Pixel
# innerhalb des gerade betrachteten Dreiecks liegen


for i in reduced_brep.faces:
    for j in range(0, n_pix_x):
        for k in range(0, n_pix_z):
            if i.point_in_projected_face(Vertex(j*stepx-0.5*stepx, 0, k*stepz-0.5*stepz)):
                img[j, k] = 0

plt.imshow(img, cmap='gray')
plt.show()
