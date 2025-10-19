```json
{
  "id": "71789bab4b3dc3fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286126,
  "host_pid": "9e6742732c60:1",
  "hash": "252bedee70de001ee952d6a17f0a07b768e680982b2b885ddbc9a0ec204a10c3",
  "cid": "QmV1252bedee70de001ee952d6a17f0a07b768e68098",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286126,
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
      "evaluated_at": 1760286126
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
  "sig": "3554a257c96bcd0c043b74ea5d301f4170b2d01288b631cf9de9df0d2beb8a31"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 121000247715779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': 'e635467487b35661'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}