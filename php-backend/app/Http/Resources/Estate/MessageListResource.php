<?php

declare(strict_types=1);

namespace App\Http\Resources\Estate;

use App\Models\Message;
use Illuminate\Http\Request;
use App\Http\Resources\Estate\PhotoResource;
use App\Http\Resources\Estate\AuthorResource;
use Illuminate\Http\Resources\Json\JsonResource;

final class MessageListResource extends JsonResource
{
    /**
     * @param Request $request
     * @return array
     */
    public function toArray($request): array
    {
        /** @var Message $this */

        return [
            'id' => $this->id,
            'telegram_group_id' => $this->telegram_group_id,
            'telegram_author_id' => $this->telegram_author_id,
            'city_id' => $this->city_id,
            'grouped_id' => $this->grouped_id,
            'text' => $this->text,
            'price' => $this->price,
            'created_at' => $this->created_at,
            'updated_at' => $this->updated_at,

            'photos' => PhotoResource::collection($this->whenLoaded('photos')),
            'author' => new AuthorResource($this->whenLoaded('author')),
            'group' => new GroupResource($this->whenLoaded('group')),
        ];
    }
}
