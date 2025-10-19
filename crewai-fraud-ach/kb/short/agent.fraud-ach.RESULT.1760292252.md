```json
{
  "id": "e4d68cc470713c5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292252,
  "host_pid": "9e6742732c60:1",
  "hash": "daee8a2b6fb59b3ce1cddd82de5cf920959213e7d83ac14c0fbaa889d9e07e20",
  "cid": "QmV1daee8a2b6fb59b3ce1cddd82de5cf920959213e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292252,
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
      "evaluated_at": 1760292252
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "fdaeb478fd284111caf7c0715cc79e50edbb3bf820139f90199283ec50b08477"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000022377083
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 96500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285765, 'matching_hash': 'fc2d68d27512b7d3'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}