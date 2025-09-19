export interface Platform {
    platform_id: number;
    name: string;
    category: string;
    metadata: object;
}

export interface User {
    user_id: number;
    username: string;
    age: number;
    country: string;
}

export interface DateDimension {
    date_id: number;
    full_date: Date;
    day: number;
    month: number;
    year: number;
}

export interface Content {
    content_id: number;
    title: string;
    content_type: string;
    tags: string[];
    media_info: object;
}

export interface Engagement {
    engagement_id: number;
    user_id: number;
    content_id: number;
    platform_id: number;
    date_id: number;
    watch_time: number;
    rating: number;
    interaction: object;
}