```json
{
  "id": "935c8ef1ddb0c16c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294136,
  "host_pid": "9e6742732c60:1",
  "hash": "823c1d252816c8182f6affc69867534a38824920a0204b9766531036a9196694",
  "cid": "QmV1823c1d252816c8182f6affc69867534a38824920",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294136,
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
      "evaluated_at": 1760294136
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
  "sig": "224cc617ac5760731c8a76c0bace3863e446a5e4804d45ee4bfbf7f6e02aca1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241821144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 113799712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '9191e5c904ced497'}}}