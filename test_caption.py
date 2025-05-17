from imageinsightai.captioner import ImageCaptioner

model = ImageCaptioner()
caption = model.describe("D:\Images\low_res_addnoise.jpg")  # Replace with your image
print("Caption:", caption)
