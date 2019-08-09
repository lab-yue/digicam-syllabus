<template>
  <syllabus-layout class="subject">
    <h1 class="syllabus-page-title">{{ $page.subject.title }}</h1>
    <p class="subject-teacher">
      <g-link :to="`/teacher/${$page.subject.teacher.id}`">
        {{
        $page.subject.teacher.name
        }}
      </g-link>
    </p>

    <div class="syllabus-page-statistics-wrapper">
      <h2 class="syllabus-page-statistics-title subject-margin">Tags</h2>

      <syllabus-button :link="link" v-for="(link,id) in tags" :key="id" />

      <h2 class="syllabus-page-statistics-title subject-margin">Purpose</h2>
      <p class="subject-txt">{{detail.purpose}}</p>

      <h2 class="syllabus-page-statistics-title subject-margin">Target</h2>
      <p class="subject-txt">{{detail.target}}</p>

      <h2 class="syllabus-page-statistics-title subject-margin">teachingStyle</h2>
      <p class="subject-txt">{{detail.teachingStyle}}</p>

      <h2 class="syllabus-page-statistics-title subject-margin">GradePolicy</h2>
      <p class="subject-txt">{{detail.gradePolicy}}</p>

      <h2 class="syllabus-page-statistics-title subject-margin">FinalTest</h2>
      <p class="subject-txt">{{detail.finalTest}}</p>

      <h2 class="syllabus-page-statistics-title subject-margin">Message</h2>
      <p class="subject-txt">{{detail.message}}</p>

      <h2 class="syllabus-page-statistics-title subject-margin">Keywords</h2>
      <ul>
        <li v-for="line in detail.keywords" :key="line">
          <p class="subject-txt">{{line}}</p>
        </li>
      </ul>

      <h2 class="syllabus-page-statistics-title subject-margin">Contents</h2>
      <ul>
        <li v-for="line in detail.contents" :key="line">
          <p class="subject-txt">{{line}}</p>
        </li>
      </ul>
    </div>
  </syllabus-layout>
</template>

<page-query>
query Subject($id: String!) {
  subject: subject(id: $id) {
    title
    subtitle
    generalTitle
    time
    location
    type
    category{
      id
      name
    }
    field{
      name
      id
    }
    year {
      name
    }
    compulsory
    detail {
      purpose
      target
      message
      keywords
      contents
      finalTest
      teachingStyle
      gradePolicy
      department
    }
    teacher {
      id
      name
    }
  }
}
</page-query>

<script>
export default {
  metaInfo() {
    return {
      title: this.$page.subject.title
    };
  },
  computed: {
    tags() {
      const subject = this.$page.subject;
      return [
        {
          name: subject.time,
          url: `#`
        },
        {
          name: subject.location,
          url: `#`
        },
        {
          name: subject.type,
          url: `#`
        },
        {
          name: subject.category.name,
          url: `/category/${subject.category.id}`
        },
        {
          name: subject.field.name,
          url: `/field/${subject.field.id}`
        },
        {
          name:
            subject.year.name === "不明"
              ? "年: 不明"
              : subject.year.name + "年",
          url: `#`
        },
        {
          name: subject.compulsory,
          url: `#`
        }
      ].filter(tag => tag.name && tag.name !== "不明");
    },
    detail() {
      return this.$page.subject.detail;
    }
  }
};
</script>

<style lang="scss" scoped>
.subject {
  &-title {
    &-sub {
      text-align: center;
      color: $theme-green;
      font-size: 1.4rem;
    }
  }

  &-teacher {
    font-size: 1.6rem;
    color: $theme-grey;
    text-align: center;
  }
  &-margin:not(:first-child) {
    margin-top: 4rem;
  }
  &-txt {
    font-size: 1.2rem;
    padding-left: 3rem;
    white-space: pre-line;
    word-break: break-word;
    line-height: 1.5;
  }
}
@media screen and (max-width: 640px) {
  .subject {
    &-txt {
      padding-left: 0;
      font-size: 1.1rem;
    }
  }
}
</style>
