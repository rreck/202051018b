```json
{
  "id": "1374c317580cab64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293940,
  "host_pid": "9e6742732c60:1",
  "hash": "71dc8334c22602875af07c8aef18b01b1572ed1f903e85a9ad06e32f2f795ef2",
  "cid": "QmV171dc8334c22602875af07c8aef18b01b1572ed1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293940,
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
      "evaluated_at": 1760293940
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
  "sig": "7b136cc1d55d1bcd8a1bdd774f64d8e6fb62313ac918a7299699534915295bea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 20192592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}