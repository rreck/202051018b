```json
{
  "id": "acb94971e74827e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288881,
  "host_pid": "9e6742732c60:1",
  "hash": "59c514d214da732d7521b192efba9731023947527fd099f1c9b787e940704327",
  "cid": "QmV159c514d214da732d7521b192efba973102394752",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288881,
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
      "evaluated_at": 1760288881
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
  "sig": "c3273c0e0a26205f06bfd7f11ce54ca0fddeb56904c607055670f518458c4493"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460168239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'c8b812a49265f53e'}}}een': 1760285763, 'matching_hash': 'c1a39c32a70f5fe9'}}}