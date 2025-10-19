```json
{
  "id": "230d4f54f6b76ecb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286185,
  "host_pid": "9e6742732c60:1",
  "hash": "6c78aeb524e7007961475ceed15ba038bee3573f605b375b99e20df33d072f58",
  "cid": "QmV16c78aeb524e7007961475ceed15ba038bee3573f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286185,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286185
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "ce3bcaa32a005ebf5324b1a3b2de4e745c4edcfc8df678f28aa181675784a2ab"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 906924177607497
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285765, 'matching_hash': 'a0bedab775ea6194'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}