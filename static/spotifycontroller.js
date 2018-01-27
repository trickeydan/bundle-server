const spotify = new SpotifyWebApi();

function get_banner(container, song_id) {
    container = $(container);

    var track = spotify.getTrack(song_id);
    track.resolve = function() {
        console.log(track);

        container.find(".albumart")[0].src(track["album"]["images"][0]["url"]);
        container.find(".songtitle")[0].html(track["name"]);
        container.find(".artist")[0].html(track["artists"][0]["name"]);
    };
}
