"""Functions to interact with the PetFinder API."""

def get_auth_token():
    """Request a token from PetFinder using SECRET KEY"""


def get_random_animal();
    """Get a random animal from PetFinder API at /animals"""


"""For reference - What we need from /animals:
the pet name - animals[idx]['name']
the pet age (baby, young, adult, senior) - animals[idx]['age']
the URL of a photo of the pet - animals[idx]['photos'][0]['large']

{
    "id": 53014786,
    "organization_id": "TX123",
    "url": "https:\/\/www.petfinder.com\/dog\/bailey-53014786\/tx\/el-paso\/animal-rescue-league-of-el-paso-tx123\/?referrer_id=88bf2a00-80b2-478d-8197-a20c76df2368",
    "type": "Dog",
    "species": "Dog",
    "breeds": {
      "primary": "Husky",
      "secondary": "Shepherd",
      "mixed": true,
      "unknown": false
    },
    "colors": {
      "primary": null,
      "secondary": null,
      "tertiary": null
    },
    "age": "Adult",
    "gender": "Female",
    "size": "Large",
    "coat": null,
    "attributes": {
      "spayed_neutered": true,
      "house_trained": false,
      "declawed": null,
      "special_needs": false,
      "shots_current": true
    },
    "environment": {
      "children": null,
      "dogs": null,
      "cats": null
    },
    "tags": [],
    "name": "Bailey",
    "description": "Bailey was found as a stray.  She is a sweet girl about 5 years old.  ARL hasn&#039;t had Bailey out...",
    "organization_animal_id": "20-0536",
    "photos": [
      {
        "small": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/1\/?bust=1631922415&width=100",
        "medium": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/1\/?bust=1631922415&width=300",
        "large": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/1\/?bust=1631922415&width=600",
        "full": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/1\/?bust=1631922415"
      },
      {
        "small": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/2\/?bust=1631922415&width=100",
        "medium": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/2\/?bust=1631922415&width=300",
        "large": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/2\/?bust=1631922415&width=600",
        "full": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/2\/?bust=1631922415"
      },
      {
        "small": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/3\/?bust=1631922416&width=100",
        "medium": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/3\/?bust=1631922416&width=300",
        "large": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/3\/?bust=1631922416&width=600",
        "full": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/3\/?bust=1631922416"
      },
      {
        "small": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/4\/?bust=1631922417&width=100",
        "medium": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/4\/?bust=1631922417&width=300",
        "large": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/4\/?bust=1631922417&width=600",
        "full": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/4\/?bust=1631922417"
      },
      {
        "small": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/5\/?bust=1631922417&width=100",
        "medium": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/5\/?bust=1631922417&width=300",
        "large": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/5\/?bust=1631922417&width=600",
        "full": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/5\/?bust=1631922417"
      }
    ],
    "primary_photo_cropped": {
      "small": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/1\/?bust=1631922415&width=300",
      "medium": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/1\/?bust=1631922415&width=450",
      "large": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/1\/?bust=1631922415&width=600",
      "full": "https:\/\/dl5zpyw5k3jeb.cloudfront.net\/photos\/pets\/53014786\/1\/?bust=1631922415"
    },
    "videos": [],
    "status": "adoptable",
    "status_changed_at": "2021-09-17T23:46:58+0000",
    "published_at": "2021-09-17T23:46:58+0000",
    "distance": null,
    "contact": {
      "email": "info@arlep.org",
      "phone": "(915)877-5002",
      "address": {
        "address1": "7256 La Junta",
        "address2": "Canutillo, Texas 79835",
        "city": "El Paso",
        "state": "TX",
        "postcode": "79821",
        "country": "US"
      }
    },
    "_links": {
      "self": {
        "href": "\/v2\/animals\/53014786"
      },
      "type": {
        "href": "\/v2\/types\/dog"
      },
      "organization": {
        "href": "\/v2\/organizations\/tx123"
      }
    }
  },"""