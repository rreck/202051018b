```json
{
  "id": "e106392ec2d2b5fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290705,
  "host_pid": "9e6742732c60:1",
  "hash": "1cf6db0522ec1b60c5e6090b6cc2c199ec356e0e17bc0d86a6db7d08316673c1",
  "cid": "QmV11cf6db0522ec1b60c5e6090b6cc2c199ec356e0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290705,
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
      "evaluated_at": 1760290705
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
  "sig": "8fe47e797eaa7f3c935d702454b2e7edf19cb695c1f24392f8306547ffbfb751"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245017605
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 73856882, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5513113}}}