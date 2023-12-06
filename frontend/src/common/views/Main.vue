<script setup lang="ts">
import { home, barbell, barChart, personCircleOutline } from "ionicons/icons";
</script>
<template>
  <ion-tabs>
    <ion-router-outlet></ion-router-outlet>
    <ion-tab-bar slot="bottom">
      <ion-tab-button tab="home" href="/home">
        <ion-icon :icon="home" />
        <ion-label>Home</ion-label>
      </ion-tab-button>

      <ion-tab-button tab="training" href="/training">
        <ion-icon :icon="barbell" />
        <ion-label>Training</ion-label>
      </ion-tab-button>

      <ion-tab-button tab="charts" href="/charts">
        <ion-icon :icon="barChart" />
        <ion-label>Charts</ion-label>
      </ion-tab-button>
      <ion-tab-button tab="profile" href="/profile">
        <ion-icon :icon="personCircleOutline" />
        <ion-label>Profile</ion-label>
      </ion-tab-button>
    </ion-tab-bar>
  </ion-tabs>
</template>

<script lang="ts">
import {
  IonPage,
  IonTabs,
  IonRouterOutlet,
  IonTabBar,
  IonTabButton,
  IonLabel,
  IonIcon,
} from "@ionic/vue";

export default {
  components: {
    IonPage,
    IonTabs,
    IonRouterOutlet,
    IonTabBar,
    IonTabButton,
    IonLabel,
    IonIcon,
  },
};
</script>
