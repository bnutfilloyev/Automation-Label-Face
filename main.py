import face_recognition as fr
import os

path = 'images'
images = os.listdir('images')
images.remove('.DS_Store')

def markAttendence(top, right, bottom, left, i, height, width, depth):
    with open(f"{os.path.splitext(i)[0]}.xml", 'w+') as f:
        f.write(f"""<annotation>
	<folder>snap</folder>
	<filename>{i}</filename>
	<path>/Users/yoshlikmedia/PycharmProjects/Label/snap/{i}</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>{width}</width>
		<height>{height}</height>
		<depth>{depth}</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>face</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>{left}</xmin>
			<ymin>{top}</ymin>
			<xmax>{right}</xmax>
			<ymax>{bottom}</ymax>
		</bndbox>
	</object>
</annotation>""")

if __name__ == '__main__':
    for i in images:
        # print(i)
        img = fr.load_image_file(f'{path}/{i}')
        address = fr.face_locations(img)
        if address != [] :
            print(address)
            top, right, bottom, left = address[0]
            height, width, depth = img.shape
            print(img.shape)
            markAttendence(top, right, bottom, left, i, height, width, depth)
