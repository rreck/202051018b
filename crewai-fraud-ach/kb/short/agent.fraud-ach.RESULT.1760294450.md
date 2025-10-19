```json
{
  "id": "d2eae57f68082f07",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294450,
  "host_pid": "9e6742732c60:1",
  "hash": "80f6fd5513852b01bc6dddf39962adf7ba4e7ca4e61ac327e5ee1fd5995ee86a",
  "cid": "QmV180f6fd5513852b01bc6dddf39962adf7ba4e7ca4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294450,
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
      "evaluated_at": 1760294450
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
  "sig": "edd02b7e8a40300196eaceec92348f2baaefaeb363f7ec7be931aa719b776e72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461577963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 103498584, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285764, 'matching_hash': '6bf1d905269d1dd3'}}}