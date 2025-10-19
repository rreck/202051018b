```json
{
  "id": "c448b1ac0a70d795",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288278,
  "host_pid": "9e6742732c60:1",
  "hash": "5adddd2fce5086a8ccc18eedf6dd8add2ebdc5994d718917590ee5e0f8d80152",
  "cid": "QmV15adddd2fce5086a8ccc18eedf6dd8add2ebdc599",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288278,
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
      "evaluated_at": 1760288278
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
  "sig": "d1a30485c676ad1a30736d0c526afe3b6ab7551f5bb83b52cf2c408030199222"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151422831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285764, 'matching_hash': 'e9fc645b92693d6a'}}}