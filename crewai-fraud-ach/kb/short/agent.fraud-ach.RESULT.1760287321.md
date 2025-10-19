```json
{
  "id": "1d851aa28c6986f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287321,
  "host_pid": "9e6742732c60:1",
  "hash": "dc7203e1ba57d7639e39bb21e52fa6dc3ca5117d35628777b55c9587b9902b7c",
  "cid": "QmV1dc7203e1ba57d7639e39bb21e52fa6dc3ca5117d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287321,
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
      "evaluated_at": 1760287321
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "f746bddde5a344cb6bf5dc9c1bb3b6483b8a151947146665412a02ff90ad7a1c"
}
```

Fraud detected: duplicate_transaction (score: 73)
Transaction: 121000243431079
Details: {'velocity': {'fraud_detected': True, 'risk_score': 62, 'details': {'transaction_count': 56, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285764, 'matching_hash': '441814efc7e72dab'}}}een': 1760285763, 'matching_hash': '282a945486899803'}}}