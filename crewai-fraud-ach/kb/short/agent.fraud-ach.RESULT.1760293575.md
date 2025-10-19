```json
{
  "id": "7ed1c0df0db26572",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293575,
  "host_pid": "9e6742732c60:1",
  "hash": "fe450d22032c52ca1d0efd2d1cb86bdf83b3a7fa05b54085c4051e7827fba24c",
  "cid": "QmV1fe450d22032c52ca1d0efd2d1cb86bdf83b3a7fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293575,
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
      "evaluated_at": 1760293576
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
  "sig": "b842b939c692c43d454e9a319f1104d5ef0065e56da68037451833ef1137b37a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023553215
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 86543379, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '85da211728f5a38f'}}}