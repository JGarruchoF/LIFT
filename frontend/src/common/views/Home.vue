<script setup>
import {
  IonPage,
  IonContent,
  IonGrid,
  IonRow,
  IonCol,
  IonAvatar,
  IonCard,
  IonCardContent,
} from "@ionic/vue";
</script>
<template>
  <ion-page>
    <ion-content class="ion-padding">
      <ion-grid>
        <ion-row>
          <ion-col
            ><ion-avatar>
              <img
                alt="Silhouette of a person's head"
                src="https://ionicframework.com/docs/img/demos/avatar.svg"
              />
            </ion-avatar>
          </ion-col>
          <ion-col></ion-col>
        </ion-row>
      </ion-grid>
      <h1 class="ion-text-start">Last Sessions</h1>
      <ion-card>
        <ion-card-content><WeeklySessionsChart /></ion-card-content>
      </ion-card>
      <h1 class="ion-text-start">Achivements</h1>
      <h1 class="ion-text-start">Goals</h1>
    </ion-content>
  </ion-page>
</template>
<script>
import WeeklySessionsChart from "../components/WeeklySessionsChart.vue";

export default {
  name: "Home",
  components: { WeeklySessionsChart },
};
</script>
