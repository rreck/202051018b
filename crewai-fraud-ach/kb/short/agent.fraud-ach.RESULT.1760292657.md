```json
{
  "id": "fb654dffb6be9842",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292657,
  "host_pid": "9e6742732c60:1",
  "hash": "72e70b9b5b2fab8b15df2698be7ce3d816c842baaf048daa9c1b212adc0e15c3",
  "cid": "QmV172e70b9b5b2fab8b15df2698be7ce3d816c842ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292657,
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
      "evaluated_at": 1760292657
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
  "sig": "a9e48f5776efae525ffd9437b2174a0e24b2829be950d110419a81e4ba8aa934"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271240415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 23770148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': '8c20097da64de4ba'}}}