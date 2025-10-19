```json
{
  "id": "0c5f5f9da740592f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292709,
  "host_pid": "9e6742732c60:1",
  "hash": "03a671508b86716b9fff3c57bba4d5dfbfc10f1cff36950a889f395bff09ae66",
  "cid": "QmV103a671508b86716b9fff3c57bba4d5dfbfc10f1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292709,
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
      "evaluated_at": 1760292709
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
  "sig": "4695f6875dc6bc0ad3a1c6f0e674a0fa19bf7c434977bead6bb22883f02b6e4a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462125361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 35569863, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285764, 'matching_hash': '410e2c6110d1d339'}}}