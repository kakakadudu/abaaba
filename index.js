const axios = require('axios').default;
const cheerio = require('cheerio')
const xlsx = require('node-xlsx').default;
const fs = require('fs');
const path = require('path');

async function getBookHTML() {
  let result = await axios.get('https://www.sohu.com/a/485193126_121124286')
  return result.data;
}

async function getBookWords() {
  const html = await getBookHTML();
  const $ = cheerio.load(html)
  const aEles = $("tr>td:first-child");// tbody 下 tr 第一个 td
  var result = aEles.map((i, el) => {
    return $(el).text();
  }).get()
  result = result.map(item => [item])

  const fileName = path.resolve(__dirname, 'words.xlsx');
  var buffer = xlsx.build([{ name: 'words', data: result }]); // Returns a buffer
  fs.writeFile(fileName, buffer, (err) => {
    if (err) throw err;
    console.log('保存成功');
  });
}
getBookWords();