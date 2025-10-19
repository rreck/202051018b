```json
{
  "id": "23e2364107e1e1e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292048,
  "host_pid": "9e6742732c60:1",
  "hash": "5edde8fe3dea1ee1bef6f845f7b91ebf089a9f8d69f07ab10ad3ffaae6a54af1",
  "cid": "QmV15edde8fe3dea1ee1bef6f845f7b91ebf089a9f8d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292048,
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
      "evaluated_at": 1760292048
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
  "sig": "01ad519a771c4aa04af29032cb8dcdddc3e3c19ad922e6bcd88a4d545099f2de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021988031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 47791863, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': '88465ad333807d91'}}}