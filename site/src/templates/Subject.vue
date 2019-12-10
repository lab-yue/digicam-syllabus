<template>
  <syllabus-layout>
    <v-card width="1500" class="mx-auto">
      <v-card-title class="s-title">
        {{ $page.subject.title }}
        <g-link :to="`/teacher/${$page.subject.teacher.id}`">
          <v-btn class="ma-2 email-substyle" tile outlined color="primary">
            {{
            $page.subject.teacher.name
            }}
          </v-btn>
        </g-link>
      </v-card-title>

      <v-container class="pa-2" fluid>
        <v-card class="s-card">
          <v-card-title class="s-subtitle">Tags</v-card-title>
          <g-link v-for="(link,id) in tags" :key="id" :to="link.url">
            <v-chip class="ma-2" color="primary" link outlined>{{link.name}}</v-chip>
          </g-link>
        </v-card>
        <syllabus-section title="Purpose" :content="detail.purpose" />
        <syllabus-section title="Target" :content="detail.target" />
        <syllabus-section title="Teaching Style" :content="detail.teachingStyle" />
        <syllabus-section title="Grade Policy" :content="detail.gradePolicy" />
        <syllabus-section title="Final Test" :content="detail.finalTest" />
        <syllabus-section title="Message" :content="detail.message" />
        <syllabus-section title="Keywords" :content="detail.keywords" />
        <syllabus-section title="Contents" :content="detail.contents" />
      </v-container>
    </v-card>
  </syllabus-layout>
  <!--
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

      <syllabus-section title="Purpose" :content="detail.purpose" />
      <syllabus-section title="Target" :content="detail.target" />
      <syllabus-section title="Teaching Style" :content="detail.teachingStyle" />
      <syllabus-section title="Grade Policy" :content="detail.gradePolicy" />
      <syllabus-section title="Final Test" :content="detail.finalTest" />
      <syllabus-section title="Message" :content="detail.message" />
      <syllabus-section title="Keywords" :content="detail.keywords" />
      <syllabus-section title="Contents" :content="detail.contents" />
    </div>
  </syllabus-layout>
  -->
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
    category {
      id
      name
    }
    field {
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
import SyllabusCard from "../components/SyllabusCard";

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
  },
  components: {
    SyllabusCard
  }
};
</script>

<style lang="scss" scoped>
.s {
  &-title {
    margin: 30px 0 10px 30px;
  }
  &-card {
    box-shadow: none;
    margin: 0 20px;
  }
  &-subtitle {
    font-size: 1.3rem;
  }
}
/*
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
@media screen and (max-width: 640px) {
  .subject {
    &-txt {
      padding-left: 0;
      font-size: 1.1rem;
    }
  }
}
*/
</style>
