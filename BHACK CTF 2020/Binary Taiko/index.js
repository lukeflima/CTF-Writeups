var parser = require('osu-parser');

function binaryAgent(str) {

    var newBin = str.split(" ");
    var binCode = [];
    
    for (i = 0; i < newBin.length; i++) {
        binCode.push(String.fromCharCode(parseInt(newBin[i], 2)));
    }
    return binCode.join("");
}

parser.parseFile('Matue - 777-666 (FireShell - Bhack) [000-111].osu', function (err, beatmap) {
    const binary = beatmap.hitObjects.map((hit, index) => (hit.soundTypes[0] == 'normal' ? "0" : "1" ) + ((index + 1) % 8 == 0 ? ' ': '')).join('')
    const flag = binaryAgent(binary);
    console.log(flag);
});