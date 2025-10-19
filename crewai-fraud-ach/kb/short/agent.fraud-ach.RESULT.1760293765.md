```json
{
  "id": "5a8dc25a6624bc31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293765,
  "host_pid": "9e6742732c60:1",
  "hash": "1a7b9a14be73f06dc76d57b0f52b2d68161c20c083cec649f84fbe6d689972ab",
  "cid": "QmV11a7b9a14be73f06dc76d57b0f52b2d68161c20c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293765,
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
      "evaluated_at": 1760293765
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
  "sig": "427447bb6981fa05c87d24ca25a6eb6c5e07ccdcd879454654a5c86bbc710489"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039408811
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 16717050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': '99e9efe9af819799'}}}