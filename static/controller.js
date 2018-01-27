function create_banner(song) {
    var banner, albumCover, songTitle, artistName;

    banner = $("<div class=banner></div>")
        .append(albumCover = $("<img class=albumart>").attr("src", song["cover_url"]))
        .append($("<div class=details-wrapper></div>")
            .append($("<div class=songtitle></div>").html(song["title"]))
            .append($("<div class=artist></div>").html(song["artist"])));

    return banner;
}

function grab_songs(bundle) {
    bundle = $(bundle);

    $.getJSON("/api/v1/club/", function(data) {
        bundle.empty();

        for(var key in data["songs"]) {
            var song = data["songs"][key];

            bundle.append(create_banner(song));
        }
    })
}
