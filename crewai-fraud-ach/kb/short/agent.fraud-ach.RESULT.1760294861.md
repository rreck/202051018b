```json
{
  "id": "457f8ff0e512665e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294861,
  "host_pid": "9e6742732c60:1",
  "hash": "350f8d104c88a4bf4a024645be0d2024830c97e52573ac188864df5aa661f1f3",
  "cid": "QmV1350f8d104c88a4bf4a024645be0d2024830c97e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294861,
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
      "evaluated_at": 1760294861
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
  "sig": "f5f9dcc8f70cda9a34b5dc09367ac22a6822c1d5eccdbcbec7fe14d6e37834aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468983209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 70217502, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'c1a39c32a70f5fe9'}}}