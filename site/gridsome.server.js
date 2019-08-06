// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`
const syllabus = require("../data/syllabus.json");
const { createHash } = require("crypto")

const hash = (text) => {
  return createHash('md5').update(text).digest('hex').slice(0, 8)
}
const hashStore = []

const uniqueHash = (text) => {

  let hashString = '';
  while (true) {

    hashString = hash(text)

    if (hashStore.includes(hashString)) {
      hashString = hash(hashString)
    } else {
      hashStore.push(hashString)
      break;
    }
  }
  return hashString;
}
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
        console.log({ hash })
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
      subjectType.addNode({
        ...subject,
        id: subject.code,
        detail: createReference(detailNode),
        teacher: createReference("Teacher", teachers[subject.teacher].id),
        categories: createReference("Categoy", categories[subject.category].id),
        year: createReference("Year", years[subject.year].id)
      });
    });
  });

  //api.createPages(({ createPage }) => {
  //   Use the Pages API here: https://gridsome.org/docs/pages-api
  //});
};
