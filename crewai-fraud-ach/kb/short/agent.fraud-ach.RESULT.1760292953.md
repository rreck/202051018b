```json
{
  "id": "ba67bedfe2369fa8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292953,
  "host_pid": "9e6742732c60:1",
  "hash": "6edba94340a56d022b47a835362384ac2898b3116cc5a9eea921d8acbd19cd21",
  "cid": "QmV16edba94340a56d022b47a835362384ac2898b311",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292953,
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
      "evaluated_at": 1760292953
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
  "sig": "e8caa26016b7e8a16897f370892fcdd0ec422e3ce5222fbca0adbf88609e1d6a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 18421312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}