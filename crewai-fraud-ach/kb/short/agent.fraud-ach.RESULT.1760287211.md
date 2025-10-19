```json
{
  "id": "dc5ef836bdfc66ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287211,
  "host_pid": "9e6742732c60:1",
  "hash": "f37130721ce62f7c70eec26b4713367d4b0d66c0e01ece8398f8563224da4585",
  "cid": "QmV1f37130721ce62f7c70eec26b4713367d4b0d66c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287211,
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
      "evaluated_at": 1760287211
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
  "sig": "25f81a63e4e13aa073c3880045d0c1c0778309004edc36a014d73680be7a757d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105153734827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 25659140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285764, 'matching_hash': 'f575a9f929aab221'}}}