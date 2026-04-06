"""Stores details of TEDx talks and displays them on a website."""
import tedxcurated
import media

def main():
    """Creates six TEDx talks initialising these objects with title, summary,
    poster image link, talk video link and publish date."""

    talk1 = media.Talk(
        "Capt. Hansja Sharma",
        "An inspiring TEDx talk on the journey of Capt. Hansja Sharma, a helicopter pilot who overcame challenges to achieve success.",
        "https://www.defenceguru.co.in/assets/uploads/blog/Captain%20Hansja%20Sharma%20Rudra%20Helicopter%20Pilot.webp",
        "https://youtu.be/1hWMIEl3dh0?si=mb5Fo0olPI6GFFtp",
        "2 Feb 2026"
    )

    talk2 = media.Talk(
        'Surabhi Gautam | How "SHE" became an IAS officer | TEDxRGPV',
        "A motivational TEDx talk about the journey of Surabhi Gautam becoming an IAS officer.",
        "https://laex.in/wp-content/uploads/2025/08/IMG_3504.jpg",
        "https://youtu.be/sKvMxZ284AA?si=etPCOXgQiQKjYxgt",
        "10 Nov 2017"
    )

    talk3 = media.Talk(
        "Small Steps, Big Changes | The Power of Habits | Saurabh Bothra",
        "A powerful TEDx talk explaining how small habits can create big life changes.",
        "POSTER_IMAGE_URL_HERE",
        "https://youtu.be/TIwBwyMgS50?si=vJLprD-RlQ-8Pga6",
        "5 July 2019"
    )

    talk4 = media.Talk(
        "Challenging Yourself is the Key to Achieving Your Endeavours | Spoorthi Vishwas",
        "An inspiring TEDx session about pushing personal limits to achieve goals.",
        "POSTER_IMAGE_URL_HERE",
        "https://youtu.be/VU7VIcd_i68?si=KkzhbDSRc_uVmICD",
        "7 June 2019"
    )

    talk5 = media.Talk(
        "How to Get Your Brain to Focus | Chris Bailey | TEDxManchester",
        "A TEDx talk on improving focus, productivity, and managing attention effectively.",
        "POSTER_IMAGE_URL_HERE",
        "VIDEO_URL_HERE",
        "PUBLISH_DATE_HERE"
    )

    talk6 = media.Talk(
        "Your Talk Title",
        "Brief description of the idea shared in this TEDx talk.",
        "POSTER_IMAGE_URL_HERE",
        "VIDEO_URL_HERE",
        "PUBLISH_DATE_HERE"
    )

    talks = [talk1, talk2, talk3, talk4, talk5, talk6]

    tedxcurated.open_talks_page(talks)


if __name__ == "__main__":
    main()