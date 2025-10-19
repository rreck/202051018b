```json
{
  "id": "49ded97a1c80f4d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288532,
  "host_pid": "9e6742732c60:1",
  "hash": "01bab01fed096166d1cf238caab7cd5ce3227f1e41e0454cb472873840fe2972",
  "cid": "QmV101bab01fed096166d1cf238caab7cd5ce3227f1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288532,
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
      "evaluated_at": 1760288532
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
  "sig": "acefa3cbaf8f3698cabd05c2cf57f6b3693e99fc41d4f634e8a9c90275734853"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464550835
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 17974272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': '50cb0ee46794e046'}}}