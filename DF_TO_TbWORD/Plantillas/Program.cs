using System;
using System.Collections.Generic;
using System.IO;
using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;
using System.Linq;

namespace Plantillas
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] wordTemplatePaths = {
    "C:\\Users\\Bernal\\source\\repos\\Plantillas\\plantilla1.docx",
    "C:\\Users\\Bernal\\source\\repos\\Plantillas\\plantilla2.docx"
};
            string outputFolderPath = "C:\\Users\\Bernal\\source\\repos\\Plantillas\\salida";
            Dictionary<string, List<string[]>> csvData = new Dictionary<string, List<string[]>>();

       
            csvData["Marcador1"] = ReadCSVFile("C:\\Users\\Bernal\\source\\repos\\Plantillas\\datos1.csv");
            csvData["Marcador2"] = ReadCSVFile("C:\\Users\\Bernal\\source\\repos\\Plantillas\\datos2.csv");


           
            ProcessFiles(csvData, wordTemplatePaths[0], outputFolderPath);
            ProcessFiles(csvData, wordTemplatePaths[1], outputFolderPath, "output2.docx");
        }

        private static List<string[]> ReadCSVFile(string csvFilePath)
        {
            List<string[]> csvData = new List<string[]>();

            using (var reader = new StreamReader(csvFilePath))
            {
                while (!reader.EndOfStream)
                {
                    var line = reader.ReadLine();
                    var values = line.Split(',');
                    csvData.Add(values);
                }
            }

            return csvData;
        }

        private static void ProcessFiles(Dictionary<string, List<string[]>> csvData, string wordTemplatePath, string outputFolderPath, string outputFileName = "output.docx")
        {
            
            string tempFilePath = Path.Combine(outputFolderPath, "temp.docx");
            File.Copy(wordTemplatePath, tempFilePath, true);

            bool success = false;
            int retries = 0;
            while (!success && retries < 10)
            {
                try
                {
                   
                    using (var wordDoc = WordprocessingDocument.Open(tempFilePath, true))
                    {
                       
                        ReplacePlaceholderWithCSVTable(wordDoc, "Marcador1", csvData["Marcador1"]);
                        ReplacePlaceholderWithCSVTable(wordDoc, "Marcador2", csvData["Marcador2"]);

                       
                        string outputFilePath = Path.Combine(outputFolderPath, outputFileName);
                        wordDoc.SaveAs(outputFilePath);
                        wordDoc.Close();
                    }

                    success = true;
                }
                catch (IOException)
                {
                    retries++;
                    System.Threading.Thread.Sleep(1000);
                }
            }

            
            File.Delete(tempFilePath);
        }





        private static void ReplacePlaceholderWithCSVTable(WordprocessingDocument doc, string markerName, List<string[]> csvData)
        {
           
            var placeholder = doc.MainDocumentPart.RootElement.Descendants<BookmarkStart>()
                .Where(b => b.Name == markerName)
                .FirstOrDefault();

            if (placeholder != null)
            {
                
                var table = placeholder.Ancestors<Table>().FirstOrDefault();

                if (table != null)
                {
                 
                    var firstRow = table.Elements<TableRow>().FirstOrDefault();

                    if (firstRow != null)
                    {
                       
                        firstRow.Remove();
                    }

                    
                    foreach (var row in csvData)
                    {
                        var tableRow = new TableRow();

                      
                        foreach (var item in row)
                        {
                            var tableCell = new TableCell();
                            tableCell.AppendChild(new Paragraph(new Run(new Text(item))));
                            tableRow.AppendChild(tableCell);
                        }

                       
                        table.AppendChild(tableRow);
                    }

               
                    var bookmarkEnd = placeholder.Parent.Elements<BookmarkEnd>().FirstOrDefault(e => e.Id.Value == placeholder.Id.Value);
                    var bookmarkStart = placeholder;
                    bookmarkStart.Remove();
                    bookmarkEnd.Remove();
                }
            }
        }










    }
}
