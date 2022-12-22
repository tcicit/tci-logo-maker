import cairosvg
import base64

out_filename = "new_logo-02"
overlay_image = "tci-flower.png" # Das Bild muss im PNG Format vorliegen und der Hintergrund sollte transparent sein.
img_height = 256
img_width = 256
background_color = "gray"
boarder = 20
boarder_radius = 150
stroke_fill = "black"
stroke_width = 0

with open(overlay_image, "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())

data = (f'''
        <svg 
            width="{img_width}"     
            height="{img_height}" 
            xmlns="http://www.w3.org/2000/svg" 
            xmlns:xlink="http://www.w3.org/1999/xlink">

        <g>
            <rect 
                width="{img_width - stroke_width}"  
                height="{img_height - stroke_width}" 
                x="{stroke_width/2}"
                y="{stroke_width/2}"
                rx="{boarder_radius}" 
                style="fill:{background_color}; stroke: {stroke_fill}; stroke-width: {stroke_width};" />'
            <image 
                width="{img_width - stroke_width -(boarder*2)}" 
                height="{img_height - stroke_width -(boarder*2)}" 
                x="{boarder + (stroke_width/2)}" 
                y="{boarder + (stroke_width/2)}"  
                preserveAspectRatio="none" 
                xlink:href="data:image/png;base64,{b64_string.decode('utf-8')}" />
        </g>
        
    </svg>
    ''')

print (data)

f = open(f'{out_filename}.svg', "w")
f.write(data) 
f.close()

cairosvg.svg2png(url=f'{out_filename}.svg', write_to=f'{out_filename}.png')
