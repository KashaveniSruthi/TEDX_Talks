import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>TEDx Talks Library</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #333;
            color: #CCC;
        }
        #talk .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #talk-video {
            width: 100%;
            height: 100%;
        }
        .talk-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .talk-tile:hover {
            background-color: #444;
            cursor: pointer;
        }
        .talk-tile img {
            box-shadow: 7px 7px 12px #222;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>

    <script type="text/javascript" charset="utf-8">

        // Stop video when modal closes
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            $("#talk-video-container").empty();
        });

        // Play talk video when talk tile is clicked
        $(document).on('click', '.talk-tile', function (event) {
            var talkYouTubeId = $(this).attr('data-talk-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + talkYouTubeId + '?autoplay=1&html5=1';

            $("#talk-video-container").empty().append($("<iframe></iframe>", {
              'id': 'talk-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // Animate talks when page loads
        $(document).ready(function () {
          $('.talk-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });

    </script>

</head>
'''

# Main page layout
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>

    <!-- Talk Video Modal -->
    <div class="modal" id="talk">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>

          <div class="scale-media" id="talk-video-container">
          </div>

        </div>
      </div>
    </div>


    <!-- Page Content -->
    <div class="container">

      <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">

          <div class="navbar-header">
            <a class="navbar-brand" href="#">TEDx Inspirational Talks</a>
          </div>

        </div>
      </div>

    </div>


    <div class="container">
      {talk_tiles}
    </div>

  </body>
</html>
'''

# Single talk tile template
talk_tile_content = '''
<div class="col-md-6 col-lg-4 talk-tile text-center"
data-talk-youtube-id="{talk_youtube_id}"
data-toggle="modal"
data-target="#talk">

    <img src="{poster_image_url}" width="220" height="342">

    <h2>{talk_title}</h2>

    <p>{talk_summary}</p>

    <p>Published on: {talk_publish_date}</p>

</div>
'''


def create_talk_tiles_content(talks):

    content = ''

    for talk in talks:

        # extract youtube id
        youtube_id_match = re.search(r'(?<=v=)[^&#?]+', talk.talk_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#?]+',
                                                         talk.talk_youtube_url)

        talk_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        content += talk_tile_content.format(

            talk_title=talk.title,
            talk_summary=talk.summary,
            poster_image_url=talk.poster_image_url,
            talk_youtube_id=talk_youtube_id,
            talk_publish_date=talk.publish_date

        )

    return content



def open_talks_page(talks):

    if os.path.exists('tedxcurated.html'):

        url = os.path.abspath('tedxcurated.html')
        webbrowser.open('file://' + url, new=2)

    else:

        output_file = open('tedxcurated.html', 'w')

        rendered_content = main_page_content.format(
            talk_tiles=create_talk_tiles_content(talks)
        )

        output_file.write(main_page_head + rendered_content)

        output_file.close()

        url = os.path.abspath(output_file.name)

        webbrowser.open('file://' + url, new=2)