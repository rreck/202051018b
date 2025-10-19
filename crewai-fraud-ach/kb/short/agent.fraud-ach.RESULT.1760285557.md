```json
{
  "id": "852ede5d16db29c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285557,
  "host_pid": "9e6742732c60:1",
  "hash": "59eca17c824ddb07774dd317687ffb844ad227973994817f0732ff595364fdb4",
  "cid": "QmV159eca17c824ddb07774dd317687ffb844ad22797",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285557,
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
      "evaluated_at": 1760285557
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
  "sig": "d64609b76feb333fe199f85bab10a4bb1a365c854edc85889d55e0078839f25e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 24019458, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}