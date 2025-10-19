```json
{
  "id": "fecad3a588a01493",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286692,
  "host_pid": "9e6742732c60:1",
  "hash": "6804449a6d82dd95cde9632db4dc34e08b6967cd0b4bafd26b17c06f6ea76d74",
  "cid": "QmV16804449a6d82dd95cde9632db4dc34e08b6967cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286692,
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
      "evaluated_at": 1760286692
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "4be8711b32b4e403094af1ad30fa341188ebd2b9032804d1e7c7f967c9efab35"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248569332
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '521bb7eb391c7339'}}}k_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '77eebc6eb9f79eeb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}