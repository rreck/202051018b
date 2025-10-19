```json
{
  "id": "b07e9b2738621b8f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288409,
  "host_pid": "9e6742732c60:1",
  "hash": "0da64ad59e9902bdf0bc2a945125657cc22f81ac18f2d8cf16b08575becc68f2",
  "cid": "QmV10da64ad59e9902bdf0bc2a945125657cc22f81ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288409,
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
      "evaluated_at": 1760288409
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
  "sig": "a41c2e2ac29202cffc7c38ab1f0d3f31400fe9918491e6f49772fb03356a87bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022683015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 22511480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285765, 'matching_hash': 'a34aa564f21aebc1'}}}