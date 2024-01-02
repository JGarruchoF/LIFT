import type { TrainingSession } from "@/modules/training/types/training-session.ts";
import type { SearchParams, Response } from "@/types/api-call.ts";

class TrainingSessionService {
  basename = "TrainingSessionService";
  async getUserTrainings({ limit, offset }: SearchParams): Promise<Response<TrainingSession[]>> {
    // TODO: add filters
    const params = new URLSearchParams({
      offset: offset.toString() || "0",
      limit: limit.toString() || "25",
    });
    const response = await fetch(`http://127.0.0.1:8000/api/trainings?${params}`); //TODO: do properly
    return response.json();
  }
}

const service: TrainingSessionService = Object.freeze(new TrainingSessionService());

export default service;
