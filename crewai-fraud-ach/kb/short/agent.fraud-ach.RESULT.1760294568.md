```json
{
  "id": "f8e0f3d0a6d7eced",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294568,
  "host_pid": "9e6742732c60:1",
  "hash": "1974dbc1ad69fc744b9ec59e7f60d77e0ca0aac1c1dcea18aeb0837c661b119f",
  "cid": "QmV11974dbc1ad69fc744b9ec59e7f60d77e0ca0aac1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294568,
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
      "evaluated_at": 1760294568
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
  "sig": "ba1b869791ad3bb50d081d8c60d74987edcc8200f07c25103feaa84ca97e6b5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029513246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 12156480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285764, 'matching_hash': '556e5d87a3998e0a'}}}