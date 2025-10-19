```json
{
  "id": "97e9a655714359ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286244,
  "host_pid": "9e6742732c60:1",
  "hash": "9d7fd0fbe53727f99e92ce0121952b005d3c782c5a2821d7e227c573b275a710",
  "cid": "QmV19d7fd0fbe53727f99e92ce0121952b005d3c782c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286244,
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
      "evaluated_at": 1760286244
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
  "sig": "7c364f527b5415f5be3d31cf306f060d9963a4a6ab913a208aa2f0248e3c6275"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 22625675, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6131353}}}