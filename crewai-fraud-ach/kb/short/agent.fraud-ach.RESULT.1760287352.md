```json
{
  "id": "5193dbbb34543be1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287352,
  "host_pid": "9e6742732c60:1",
  "hash": "7a77e82bffe3c31ea6aa22c28bd707c99e13798d1ef360ccd827fb60743deef0",
  "cid": "QmV17a77e82bffe3c31ea6aa22c28bd707c99e13798d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287352,
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
      "evaluated_at": 1760287352
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "bb38ef0625c61d4695138d024234072813f5601cf6216b3d448e1e26e74d53e5"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201461577963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 24787476, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285764, 'matching_hash': '6bf1d905269d1dd3'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6131353}}}