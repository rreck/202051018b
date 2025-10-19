```json
{
  "id": "4615804bb3a81a32",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293735,
  "host_pid": "9e6742732c60:1",
  "hash": "c6ac7c01cd939a99fbacd962a83485499a63a12af30ccc74efc591e6b275b778",
  "cid": "QmV1c6ac7c01cd939a99fbacd962a83485499a63a12a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293735,
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
      "evaluated_at": 1760293735
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
  "sig": "64dcc4c42ae8087badc85792c364bb6efab978d564a8d10da7894fd6d16a1e1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 39343360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}