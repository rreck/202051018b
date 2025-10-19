```json
{
  "id": "724375b032ee4475",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292507,
  "host_pid": "9e6742732c60:1",
  "hash": "f6304885302555e724a855765f39b6b85a42548bb46f237ebeae94632b76309d",
  "cid": "QmV1f6304885302555e724a855765f39b6b85a42548b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292507,
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
      "evaluated_at": 1760292507
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
  "sig": "e465cecef4bcc88826a02f6052dc0ee3faa972dfd235e8f97cfb47164ac2d52b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 10271783, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': '763c66b493018133'}}}