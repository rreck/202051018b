```json
{
  "id": "ff1c4cc7ce6a51de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290749,
  "host_pid": "9e6742732c60:1",
  "hash": "2cd66db8d12de893164e1a7ad38754f5771be05f90819385d6ae20e04c6d63dc",
  "cid": "QmV12cd66db8d12de893164e1a7ad38754f5771be05f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290749,
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
      "evaluated_at": 1760290749
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
  "sig": "87dc67d5aad346b65c126c5f0881a5882d4f7a9e9362db4d06ad1d54fed96d8c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598076965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 24776296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': '05e01649c2d43b8b'}}}