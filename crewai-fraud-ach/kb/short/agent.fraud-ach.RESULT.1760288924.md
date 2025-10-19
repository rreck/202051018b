```json
{
  "id": "2b07413ba4208162",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288924,
  "host_pid": "9e6742732c60:1",
  "hash": "950b922bdf414189614e5cadc4d733c7dca23622d6a2aa6df4a26d9174a71dc6",
  "cid": "QmV1950b922bdf414189614e5cadc4d733c7dca23622",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288924,
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
      "evaluated_at": 1760288924
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
  "sig": "8e23ecd567ffa5d4b3f3c67a830316dd43abe81521995a6be1cb18fca9ac5ed6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597475256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 25617384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': 'c99ab431a9f6998c'}}}