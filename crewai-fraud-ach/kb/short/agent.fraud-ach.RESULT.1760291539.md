```json
{
  "id": "573d7b242ef572cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291539,
  "host_pid": "9e6742732c60:1",
  "hash": "1aed1f4f65e7cb2d9366080ebf52c8b48cdf14fa02076fa4f653ebc098a5411a",
  "cid": "QmV11aed1f4f65e7cb2d9366080ebf52c8b48cdf14fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291539,
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
      "evaluated_at": 1760291539
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
  "sig": "63cab75401cf1e0ea1ff90ae6bac8d0fe99bf3d5a3d6091200f19e460d734792"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274747147
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 13821222, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '9bf7edfe04e96377'}}}