import gpxpy
import os
import glob


def parsegpx(f):
    # Parse a GPX file into a list of dictoinaries.
    # Each dict is one row of the final dataset

    points2 = []
    with open(f, 'r') as gpxfile:
        gpx = gpxpy.parse(gpxfile)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    dict = {'Timestamp': point.time,
                            'Latitude': point.latitude,
                            'Longitude': point.longitude,
                            'Elevation': point.elevation
                            }
                    points2.append(dict)
    return points2


def export_txt(f, data):
    with open(f, 'w') as txt_file:
        for i in range(len(data)):
            point2D = data[i]
            s = 'coord({},{}),\n'.format(point2D['Latitude'],
                                         point2D['Longitude'])
            txt_file.write(s)
    return 0


if __name__ == '__main__':
    path_data = os.path.join('Data', '*.gpx')
    filenames = sorted(glob.glob(path_data))
    for f in filenames:
        f_txt = f.replace('.gpx', '.txt')
        all_points = parsegpx(f)
        export_txt(f_txt, all_points)
