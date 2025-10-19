```json
{
  "id": "5082742f8c289f99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287959,
  "host_pid": "9e6742732c60:1",
  "hash": "3b20fdc56345f851cc700a98ec545531ad0c84ba1a8ac82010e2057cb9e78cb0",
  "cid": "QmV13b20fdc56345f851cc700a98ec545531ad0c84ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287959,
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
      "evaluated_at": 1760287959
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
  "sig": "04744f24f160ea566f5b6d2491587928dfa9dc42aafda1dba5b0685c88fd8a58"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276380856
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 37334544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285764, 'matching_hash': '152950ce26814ef6'}}}