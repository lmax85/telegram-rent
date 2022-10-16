<?php

declare(strict_types=1);

namespace App\Http\Resources\Estate;

use App\Models\Author;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

final class AuthorResource extends JsonResource
{
    /**
     * @param Request $request
     * @return array
     */
    public function toArray($request): array
    {
        /** @var Photo $this */

        return [
            'id' => $this->id,
            'username' => $this->username,
            'type' => $this->type,
            'first_name' => $this->first_name,
            'last_name' => $this->last_name,
            'title' => $this->title,
            'avatar_path' => $this->avatar_path,
            'created_at' => $this->created_at,
        ];
    }
}
