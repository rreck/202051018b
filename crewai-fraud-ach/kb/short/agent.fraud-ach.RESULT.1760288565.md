```json
{
  "id": "2d99a37cb8961dab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288565,
  "host_pid": "9e6742732c60:1",
  "hash": "559ef87359ad4d6e901d38a9aae9e67bdebf81f44e68fa6d777bc8eed8f66fa7",
  "cid": "QmV1559ef87359ad4d6e901d38a9aae9e67bdebf81f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288565,
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
      "evaluated_at": 1760288565
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
  "sig": "7aea2aa829ee71eeaf88d7b70d65e137f0471ff400428e793add109126c2bb5f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467837924
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285765, 'matching_hash': '256da828ea708baa'}}}een': 1760285763, 'matching_hash': '9ac81502eabc8fa5'}}}