```json
{
  "id": "3cbc66e1d0b0b408",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288090,
  "host_pid": "9e6742732c60:1",
  "hash": "f9b9dc1138f6cb8509d6191212e4f38e238aa3b43c1cfc91aec35c53742a533a",
  "cid": "QmV1f9b9dc1138f6cb8509d6191212e4f38e238aa3b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288090,
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
      "evaluated_at": 1760288090
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
  "sig": "01f792ad4cabbf99a2d228891d65cac2e5cb20996306b56a5283d1fdc89d0123"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156760115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 26303304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285764, 'matching_hash': '84a7174d04c2e814'}}}