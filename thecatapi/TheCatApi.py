import requests, json, magic, os

class CatObj:
    def __init__(self, api_key):
        if not api_key:
            raise Exception("Please supply an API key")

        self.api_key = api_key
        self.url_base = "https://api.thecatapi.com/v1"
        self.images_base = self.url_base + "/images"
        self.voting_base = self.url_base + "/votes"
        self.breeds_base = self.url_base + "/breeds"
        self.categories_base = self.url_base + "/categories"
    def random_cat(self, amount):
        if not amount:
            raise ValueError("Please supply an amount of cat pictures")

        try:
            request_data = requests.get(self.images_base + "/search?limit=" + str(amount), headers={"x-api-key": self.api_key})
        except Exception as e:
            raise Exception("An error occured while attempting to request the image API. " + str(e))

        if not request_data.status_code == 200:
            raise Exception("Did not receive a 200 HTTP response, instead got: " + str(request_data.text))

        try:
            json_data = json.loads(request_data.text)
        except Exception as e:
            raise Exception("Failed to turn request data into json. " + str(e))

        return json_data
    def search_by_breed(self, breed, amount):
        if not amount:
            raise ValueError("Please supply an amount of cat pictures")
        elif not breed:
            raise ValueError("Please supply the four letter breed code")
        elif len(breed) != 4:
            raise ValueError("Please assure the breed code is four letters.")

        try:
            request_data = requests.get(self.images_base + "/search?limit=" + str(amount) + "&breed_ids=" + breed, headers={"x-api-key": self.api_key})
        except Exception as e:
            raise Exception("An error occured while attempting to request the image API. " + str(e))

        if not request_data.status_code == 200:
            raise Exception("Did not receive a 200 HTTP response, instead got: " + str(request_data.text))

        try:
            json_data = json.loads(request_data.text)
        except Exception as e:
            raise Exception("Failed to turn request data into json. " + str(e))

        return json_data
    def search_by_category(self, category, amount):
        if not amount:
            raise ValueError("Please supply an amount of cat pictures")
        elif not category:
            raise ValueError("Please supply the category")

        try:
            request_data = requests.get(self.images_base + "/search?limit=" + str(amount) + "&category_ids=" + str(category), headers={"x-api-key": self.api_key})
        except Exception as e:
            raise Exception("An error occured while attempting to request the image API. " + str(e))

        if not request_data.status_code == 200:
            raise Exception("Did not receive a 200 HTTP response, instead got: " + str(request_data.text))

        try:
            json_data = json.loads(request_data.text)
        except Exception as e:
            raise Exception("Failed to turn request data into json. " + str(e))

        return json_data
    def search_by_file_type(self, file_type, amount):
        if not amount:
            raise ValueError("Please supply an amount of cat pictures")
        elif not file_type:
            raise ValueError("Please supply the file type")
        elif file_type not in ["gif", "jpg", "png"]:
            raise ValueError("Please use either gif, jpg or png")



        try:
            request_data = requests.get(self.images_base + "/search?limit=" + str(amount) + "&mime_types=" + file_type, headers={"x-api-key": self.api_key})
        except Exception as e:
            raise Exception("An error occured while attempting to request the image API. " + str(e))

        if not request_data.status_code == 200:
            raise Exception("Did not receive a 200 HTTP response, instead got: " + str(request_data.text))

        try:
            json_data = json.loads(request_data.text)
        except Exception as e:
            raise Exception("Failed to turn request data into json. " + str(e))

        return json_data
    def vote(self, iid, value):
        new_id = ""
        if not iid:
            raise ValueError("Please supply an ID")
        if not value or value not in [0,1]:
            raise ValueError("Please supply a 1 for upvote, or a 0 for downvote.")
        if type(iid) is str:
            new_id = id
        elif type(iid) is dict:
            try:
                new_id = iid['id']
            except Exception as e:
                raise ValueError("Received incorrect object, for up_vote. " + str(e))
        else:
            raise ValueError("Received incorrect object, for up_vote")


        post_data = {
            'image_id': new_id,
            'value': value
        }
        try:
            request_data = requests.post(self.voting_base, data=json.dumps(post_data), headers={"x-api-key": self.api_key, "Content-Type": "application/json"})
        except Exception as e:
            raise Exception("An error occured while attempting to post to the vote API. " + str(e))

        if not request_data.status_code == 200:
            raise Exception("Did not receive a 200 HTTP response, instead got: " + str(request_data.text))

        try:
            json_data = json.loads(request_data.text)
        except Exception as e:
            raise Exception("Failed to turn request data into json. " + str(e))

        try:
            if json_data['message'] == "SUCCESS":
                return True
            else:
                return False
        except:
            return False
    def upload_cat(self, image):
        if not image:
            raise ValueError("Please supply an image")
        try:
            filemime = magic.from_file(image, mime=True)
        except Exception as e:
            raise Exception("Failed to obtain mimetype from your file. Did you provide the path? " + str(e))
        try:
            files = {
                "file": (os.path.basename(image), open(image, 'rb').read(), filemime)
            }
        except Exception as e:
            raise Exception("Failed to open file, with path: " + str(image) + '. ' + str(e))
        try:
            request_data = requests.post(self.images_base + "/upload", headers={"x-api-key": self.api_key}, files=files)
        except Exception as e:
            raise Exception("An error occured while attempting to upload an image. " + str(e))
        if not request_data.status_code == 201:
            raise Exception("Did not receive a 201 HTTP response, instead got: " + str(request_data.text))

        try:
            json_data = json.loads(request_data.text)
        except Exception as e:
            raise Exception("Failed to turn request data into json. " + str(e))

        return json_data
