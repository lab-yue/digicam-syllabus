<template>
  <syllabus-layout class="subject">
    <h1 class="syllabus-page-title">{{$page.subject.title}}</h1>
    <p class="subject-teacher">
      <g-link :to="`/teacher/${this.$page.subject.teacher.id}`">{{this.$page.subject.teacher.name}}</g-link>
    </p>
    <pre>{{JSON.stringify($page.subject,null,4)}}</pre>
  </syllabus-layout>
</template>

<page-query>
query Subject($id: String!){
  subject: subject(id:$id) {
    title
    subtitle
    generalTitle
    time
    location
    type
    category
    field
    year{
      name
    }
    compulsory
    detail{
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
    teacher{
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
}
</style>
