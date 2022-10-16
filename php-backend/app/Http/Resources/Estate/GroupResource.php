<?php

declare(strict_types=1);

namespace App\Http\Resources\Estate;

use App\Models\Group;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

final class GroupResource extends JsonResource
{
    /**
     * @param Request $request
     * @return array
     */
    public function toArray($request): array
    {
        /** @var Group $this */

        return [
            'id' => $this->id,
            'username' => $this->username,
            'title' => $this->title,
            'avatar_path' => $this->avatar_path,
            'description' => $this->description,
        ];
    }
}
