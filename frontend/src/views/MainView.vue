<template>
  <IonTabs>
    <IonRouterOutlet></IonRouterOutlet>
    <IonTabBar slot="bottom">
      <IonTabButton tab="home" href="/home">
        <IonIcon :icon="home" />
        <IonLabel>Home</IonLabel>
      </IonTabButton>

      <IonTabButton tab="training" href="/training">
        <IonIcon :icon="barbell" />
        <IonLabel>Training</IonLabel>
      </IonTabButton>
      <IonTabButton tab="charts" href="/charts">
        <IonIcon :icon="barChart" />
        <IonLabel>Charts</IonLabel>
      </IonTabButton>
      <IonTabButton tab="profile" href="/profile">
        <IonIcon :icon="personCircleOutline" />
        <IonLabel>Profile</IonLabel>
      </IonTabButton>
    </IonTabBar>
  </IonTabs>
</template>

<script setup lang="ts">
import { IonTabs, IonRouterOutlet, IonTabBar, IonTabButton, IonLabel, IonIcon } from "@ionic/vue";
import { home, barbell, barChart, personCircleOutline } from "ionicons/icons";
</script>

<script lang="ts">
export default {
  name: "MainView",
  components: {
    IonTabs,
    IonRouterOutlet,
    IonTabBar,
    IonTabButton,
    IonLabel,
    IonIcon,
  },
};
</script>
