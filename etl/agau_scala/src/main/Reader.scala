
import scala.collection.mutable.ArrayBuffer
import scala.io.Source

class Reader {
    def readAg(agpath: String): ArrayBuffer[PriceStamp] = {
        var priceStamps = new ArrayBuffer[PriceStamp]();
        
        priceStamps;
    }
    
    private def readFile(filePath: String, filtRegex: String): Iterator[String]= {
        val filtPattern = filtRegex.r
//        var lines = new ArrayBuffer[String]()
        val source = Source.fromFile(filePath, "UTF-8")
        val lines = source.getLines().filter { line =>  filtPattern.findFirstMatchIn(line).nonEmpty}
//        for(line <- source.getLines if filtPattern.findFirstMatchIn(line).nonEmpty) {
//            lines += line
//        }
        source.close
        lines
    }
}
