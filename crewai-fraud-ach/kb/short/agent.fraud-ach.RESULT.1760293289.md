```json
{
  "id": "3560c7bbe0b38667",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293289,
  "host_pid": "9e6742732c60:1",
  "hash": "cc1670ed6c1fcb112891ff8b3cb633c6c3c9bda427af3fbc117900db9fb5ba4d",
  "cid": "QmV1cc1670ed6c1fcb112891ff8b3cb633c6c3c9bda4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293289,
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
      "evaluated_at": 1760293289
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
  "sig": "48d4c1a072b0da784e18ec2d9a4b3301c03869dc920d8469199e4dc512e728ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279614717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 85160855, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': '2481e4baa9b260b7'}}}