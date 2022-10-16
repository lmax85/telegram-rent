<?php

declare(strict_types=1);

namespace App\Http\Resources\Estate;

use App\Models\Photo;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

final class PhotoResource extends JsonResource
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
            'path' => $this->path,
        ];
    }
}
