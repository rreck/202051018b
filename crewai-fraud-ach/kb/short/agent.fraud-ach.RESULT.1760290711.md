```json
{
  "id": "80226342e4ad8919",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290711,
  "host_pid": "9e6742732c60:1",
  "hash": "8f2203f9aef5975c20461bef9b1a9d67779ba06928ec92d59b10a8379cc1a8f1",
  "cid": "QmV18f2203f9aef5975c20461bef9b1a9d67779ba069",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290711,
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
      "evaluated_at": 1760290711
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
  "sig": "4f8f50bb6ace42b2ef888e660499c3de514d1d67f22058805be2e3768b52ac28"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243340063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 66549474, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '5f2724e98c8a67b0'}}}