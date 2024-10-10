
function decodeUplink(input) {
    return { 
        data: Decoder(input.fPort, input.bytes, input.variables)
    };   
}
//This sentence was added in order to fix the code

//Original code from the supplier
var pos = 0;
var bindata = "";

var ConvertBase = function (num) {
    return {
        from : function (baseFrom) {
            return {
                to : function (baseTo) {
                    return parseInt(num, baseFrom).toString(baseTo);
                }
            };
        }
    };
};

function pad(num) {
    var s = "0000000" + num;
    return s.slice(-8);
}

ConvertBase.dec2bin = function (num) {
    return pad(ConvertBase(num).from(10).to(2));
};

ConvertBase.bin2dec = function (num) {
    return ConvertBase(num).from(2).to(10);
};

function data2bits(data) {
    var binary = "";
    for(var i=0; i<data.length; i++) {
        binary += ConvertBase.dec2bin(data[i]);
    }
    return binary;
}

function bitShift(bits) {
    var num = ConvertBase.bin2dec(bindata.substr(pos, bits));
    pos += bits;
    return Number(num);
}

function precisionRound(number, precision) {
  var factor = Math.pow(10, precision);
  return Math.round(number * factor) / factor;
}

function Decoder(bytes, port) {
  bindata = data2bits(bytes);
 
  if(bytes.length != 6) return {"status": "ERROR", "describtion": "6 bytes are required"};
 
    Index = bitShift(8);
    Battery = precisionRound(bitShift(5)*0.05+3, 2);
    Rain = precisionRound(bitShift(12), 1);
    Rain_time = precisionRound(bitShift(8), 1);
    Frost_alert = 1 - precisionRound(bitShift(1)*1, 0);
    Heater_on = precisionRound(bitShift(1)*1, 0);
    RainIntensityCorrection = precisionRound(bitShift(12)*0.01,2);
  
  
  decoded = {
    "1_Index": Index,
    "2_Battery": Battery,
    "3_Rain": Rain,
    "4_Rain_time": Rain_time,
    "5_Frost_alert": Frost_alert,
    "6_Heater_on": Heater_on,
    "7_RainIntensityCorrection": RainIntensityCorrection,
  };
  
  return decoded;
}