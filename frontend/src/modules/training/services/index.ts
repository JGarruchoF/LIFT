import { group } from "radash";

import TrainingSessionService from "./training-session-service.ts";

const services = group([TrainingSessionService], (service) => service.basename);

export default services;
