```json
{
  "id": "35000454697afd95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287365,
  "host_pid": "9e6742732c60:1",
  "hash": "590e843002a25cadb1b5dd542f357344a8ddd710747eafc0649cdb3bf1e193bd",
  "cid": "QmV1590e843002a25cadb1b5dd542f357344a8ddd710",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287365,
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
      "evaluated_at": 1760287365
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
  "sig": "fa7c3490a6ac3972a2ab09244f9ae5023c9bc039ab2c2ffb69d85a90c6d2dea4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 18140136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}