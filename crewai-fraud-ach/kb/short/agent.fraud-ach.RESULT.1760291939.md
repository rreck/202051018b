```json
{
  "id": "949ad7ccd57002f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291939,
  "host_pid": "9e6742732c60:1",
  "hash": "bbf70e69c9402521b2e83cc46cbfe84fb67edeb1973dcfce9000012abfb860c3",
  "cid": "QmV1bbf70e69c9402521b2e83cc46cbfe84fb67edeb1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291939,
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
      "evaluated_at": 1760291939
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
  "sig": "3a3c69dea7bc322fe6ff9008880746d7464cfff740765b2d718734efe07bd325"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024542500
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 80604588, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': 'f616428a070fc3ba'}}}