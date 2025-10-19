```json
{
  "id": "f45d5ae48c1df05c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287210,
  "host_pid": "9e6742732c60:1",
  "hash": "350a61cb90e0e620d432c8b7039b9a6597e17ff07e7fc1b3b93b2a30a0339ff7",
  "cid": "QmV1350a61cb90e0e620d432c8b7039b9a6597e17ff0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287210,
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
      "evaluated_at": 1760287210
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
  "sig": "b980c00bda6f0fa2731483cd0752e5d2415b81464a80b1d306098b5a7cc4b363"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026472141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 10712624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285764, 'matching_hash': 'c34da1cfbf75ff05'}}}