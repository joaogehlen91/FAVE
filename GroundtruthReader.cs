using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace GroundtruthReader
{
    
    class GroundtruthContainer
    {
        public void LoadFromFile(string file)
        {
            if (!File.Exists(file))
            {
                Console.WriteLine("Error: cannot find ground-truth file " + file);
                return;
            }

            // initialize container
            this._pageId_attValList = new Dictionary<string, List<string>>();

            // read ground-truth information from the given file
            using (StreamReader sr = new StreamReader(file, Encoding.UTF8))
            {
                // read names of vertical, website, and attribute
                string[] header = sr.ReadLine().Split('\t');
                if (header.Length == 3)
                {
                    _verticalName = header[0];
                    _websiteName = header[1];
                    _attributeName = header[2];
                    Console.WriteLine(" Vertical = " + header[0]);
                    Console.WriteLine("  Website = " + header[1]);
                    Console.WriteLine("Attribute = " + header[2]);
                }
                else
                {
                    Console.WriteLine("Error: fail to read header");
                }

                // read related statistics
                string[] statistics = sr.ReadLine().Split('\t');
                if (statistics.Length == 4)
                {
                    Console.WriteLine("\n{0} out of {1} pages contain:", statistics[1], statistics[0]);
                    Console.WriteLine("{0} attribute values ({1} unique)", statistics[2], statistics[3]);
                }
                else
                {
                    Console.WriteLine("Error: fail to read statistics");
                }

                // read ground-truth attribute values in each page
                while (!sr.EndOfStream)
                {
                    string[] infoLine = sr.ReadLine().Split('\t');
                    if (infoLine.Length > 2)
                    {
                        string pageId = infoLine[0];
                        int numAttValsInPage = int.Parse(infoLine[1]);
                        List<string> attValListInPage = (numAttValsInPage > 0) ? infoLine.ToList().GetRange(2, numAttValsInPage) : new List<string>();

                        _pageId_attValList.Add(pageId, attValListInPage);
                    }
                }
            }

            // optionally, check result
            int numPagesWithAttVals = 0;
            int numAttVals = 0;
            foreach (List<string> attValList in _pageId_attValList.Values)
            {
                if (attValList.Count > 0)
                {
                    ++numPagesWithAttVals;
                    numAttVals += attValList.Count;
                }
            }
            Console.WriteLine("\nLoaded ground-truth: {0} attribute values contained in {1} out of {2} pages\n", numAttVals, numPagesWithAttVals, _pageId_attValList.Count);
        }

        public List<string> GetGroundtruthByPageId(string pageId)
        {
            if (_pageId_attValList == null)
            {
                Console.WriteLine("Error: invalid ground-truth data");
                return null;
            }

            List<string> attValList = null;
            if (!string.IsNullOrEmpty(pageId) && _pageId_attValList.TryGetValue(pageId, out attValList)) // find attribute value(s)
            {
                Console.WriteLine("Loaded {0} ground-truth attribute value(s) for page {1}", attValList.Count, pageId);
            }
            else
            {
                Console.WriteLine("Error: the given page-ID {0} is invalid", pageId);
            }
            return attValList;
        }

        // container for attribute values of each web page
        private Dictionary<string, List<string>> _pageId_attValList = null; // pageId ~ {attributeValue}

        // names of vertical, website, and attribute
        private string _verticalName;
        private string _websiteName;
        private string _attributeName;
    }

    class Program
    {
        static void Main(string[] args)
        {
            // TODO: please change to your root directory of ground-truth files
            string root_groundtruth = @"e:\data\groundtruth";

            // specify vertical, website, and attribute
            string verticalName = "book";
            string websiteName = "buy";
            string attributeName = "author";

            // locate the corresponding ground-truth file
            string groundtruthFile = string.Format(@"{0}\{1}\{2}-{3}-{4}.txt",root_groundtruth, verticalName, verticalName, websiteName, attributeName);

            // create a ground-truth container and load data from the file
            GroundtruthContainer gc = new GroundtruthContainer();
            gc.LoadFromFile(groundtruthFile);

            // get ground-truth attribute value(s) by specifying a page-ID
            for (;;)
            {
                Console.Write("\nPlease specify a page-ID: ");
                string pageId = Console.ReadLine().Trim();
                if (pageId == "exit")
                {
                    break;
                }

                List<string> attValListInPage = gc.GetGroundtruthByPageId(pageId);

                if (attValListInPage != null && attValListInPage.Count > 0)
                {
                    foreach (string val in attValListInPage)
                    {
                        Console.WriteLine(val);
                    }
                }
            }
        }
    }
}
