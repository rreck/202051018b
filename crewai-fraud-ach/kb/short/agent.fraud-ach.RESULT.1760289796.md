```json
{
  "id": "8bea65ed2634d4e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289796,
  "host_pid": "9e6742732c60:1",
  "hash": "b6be60c9fc08a00dae9d15536ed43286c522e2472f96d798028ad22ef3d91139",
  "cid": "QmV1b6be60c9fc08a00dae9d15536ed43286c522e247",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289796,
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
      "evaluated_at": 1760289796
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
  "sig": "6a155193925fa0492e6d470707df05bf78cd4e187bef33be30e2a1aa03ded1cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271648434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 31481499, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}