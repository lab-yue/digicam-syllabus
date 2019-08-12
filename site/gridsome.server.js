// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`
const syllabus = require("../data/syllabus.json");
const search = require("../data/search.json");
const { createHash } = require("crypto")

const hash = (text) => {
  return createHash('md5').update(text).digest('hex').slice(0, 8)
}
const hashStore = {}

const uniqueHash = (text) => {

  let hashString = '';
  while (true) {

    hashString = hash(text)

    if (hashString in hashStore) {
      hashString = hash(hashString)
    } else {
      hashStore[text] = hashString
      hashStore[hashString] = text
      break;
    }
  }
  return hashString;
}

const upper = (text) => text.slice(0, 1).toUpperCase() + text.slice(1);

module.exports = function (api) {
  api.loadSource(({ addContentType, createReference, addReference }) => {
    const subjectType = addContentType({
      typeName: "Subject",
      route: "/subject/:id"
    });
    const detailType = addContentType({
      typeName: "Detail"
    });

    const teacherType = addContentType({
      typeName: "Teacher",
      route: "/teacher/:id"
    });

    const categoryType = addContentType({
      typeName: "Category",
      route: "/category/:id"
    });

    const fieldType = addContentType({
      typeName: "Field",
      route: "/field/:id"
    });

    const yearType = addContentType({
      typeName: "Year",
      route: "/year/:id"
    });

    const teachers = {};
    const categories = {};
    const years = {};
    const fields = {};

    const gather = (collection, key, code) => {
      if (key in collection) {
        collection[key].subjects.push(code);
      } else {
        collection[key] = {
          subjects: [code]
        };
      }
    };

    const create = (contentTypeName, contentType, collection) => {
      Object.entries(collection).map(([key, val]) => {
        const hash = uniqueHash(`${contentTypeName}:${key}`)
        collection[key].id = hash;

        contentType.addNode({
          id: hash,
          name: key || "不明",
          ...val,
          subjects: {
            totalCount: val.subjects.length,
            node: createReference("Subject", val.subjects)
          }
        });
      });
    };

    syllabus.data.map(subject => {
      gather(teachers, subject.teacher, subject.code);
      gather(categories, subject.category, subject.code);
      gather(years, subject.year, subject.code);
      gather(fields, subject.field, subject.code);
    });

    create('teacher', teacherType, teachers);
    create('category', categoryType, categories);
    create('year', yearType, years);
    create('field', fieldType, fields);

    syllabus.data.map(subject => {
      const detail = { ...subject.detail };
      delete subject.detail;

      const detailNode = detailType.addNode({
        ...detail,
        path: `subject/${subject.code}/detail`
      });

      const subjectRef = Object.fromEntries(
        ['teacher', 'category', 'year', 'field'].map(typeName => {

          const hash = hashStore[`${typeName}:${subject[typeName]}`];
          const typeNameUpper = upper(typeName);
          return [typeName, createReference(typeNameUpper, hash)]
        }))

      subjectType.addNode({
        ...subject,
        ...subjectRef,
        id: subject.code,
        detail: createReference(detailNode),
        teacher: createReference("Teacher", teachers[subject.teacher].id),
        categories: createReference("Categoy", categories[subject.category].id),
        year: createReference("Year", years[subject.year].id)
      });
    });

    const emailType = addContentType({
      typeName: "Email"
    });
    const emailMap = {}

    search.data.map(item => {
      /**
        * @see https://stackoverflow.com/a/1373724
        */
      const emailMatched = [...item.text.matchAll(
        /([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi)].map(match => match[1])

      const subject = syllabus.data.filter(subject => item.id === subject.code)[0]

      if (emailMatched.length) {
        for (let email of emailMatched) {
          if (!Array.isArray(emailMap[subject.teacher])) {
            emailMap[subject.teacher] = []
          }
          if (!emailMap[subject.teacher].includes(email)) {
            emailMap[subject.teacher].push({
              link: email,
              subject: createReference('Subject', subject.code)
            })
          }
        }
      }
    })

    Object.entries(emailMap).map(([teacher, item]) => {
      const teacherID = hashStore[`teacher:${teacher}`];

      emailType.addNode({
        id: hash(`email:${teacher}`),
        teacher: createReference('Teacher', teacherID),
        addresses: item
      });
    })

  });

  //api.createPages(({ createPage }) => {
  //   Use the Pages API here: https://gridsome.org/docs/pages-api
  //});
};
