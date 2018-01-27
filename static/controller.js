const bundle = []
const bannerMap = {}
const voteMap = {}

function updateTimer(remaining, maximum) {
    var timeStr = formatTime(remaining);
    remaining /= maximum
    var i = 0;
    var displayFound = false;

    $("#timer").children("div").each(function() {
        var width = Math.min(remaining, (i+1) * .1);
        remaining -= width;
        $(this).width((width * 100) + "%");

        if(!displayFound && remaining == 0) {
            $(this).html(timeStr);
            displayFound = true;
        } else {
            $(this).html("");
        }
        i++;
    });
}

function formatTime(seconds) {
    var minutes = Math.floor(seconds / 60);
    seconds %= 60;

    return minutes + ":" + pad(seconds, 2);
}

function createBanner(id, song) {
    song = song["track"]

    return bannerMap[id] = $("<div class=banner></div>")
        .append($("<div class=bar></div>"))
        .append($("<img class=albumart>").attr("src", song["album"]["images"][0]["url"]))
        .append($("<div class=details-wrapper></div>")
            .append($("<div class=songtitle></div>").html(song["name"]))
            .append($("<div class=artist></div>").html(song["artists"][0]["name"])))
        
        .click(function() {
            castVote(id);
        });
}

function getVote(id) {
    return id in voteMap ? voteMap[id] : 0;
}

function castVote(id) {
    if(!(id in bundle)) {
        console.log("Song not in current bundle")
    }

    if(!(id in voteMap)) {
        voteMap[id] = 0;
    }
    ++voteMap[id];

    updateBanners();
}

function getVoteCount() {
    var count = 0;

    for(id in voteMap) {
        count += voteMap[id];
    }
    return count;
}

function getMaxVote() {
    var max = 0;

    for(id in voteMap) {
        if(voteMap[id] > max) {
            max = voteMap[id];
        }
    }
    return max;
}

function pad(n, width, z) {
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}

function updateBanners() {
    var totalVotes = getVoteCount();

    for(id in bannerMap) {
        var banner = bannerMap[id];
        var percentage = voteMap[id] / totalVotes * 100;
        var width = voteMap[id] / getMaxVote() * 100

        banner.find(".bar").width(percentage + "%")
            .attr("data-percent", Math.round(percentage));
    }
}

function grabBundle(bundle) {
    bundle = $(bundle);

    $.getJSON("/api/v1/club/", function(data) {
        bundle.empty();

        var items = data["songs"]["items"];
        for(var key in items) {
            var song = items[key];

            bundle.append(createBanner(key, song));
        }
    })
}
