```json
{
  "id": "cfb681626374c2e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292790,
  "host_pid": "9e6742732c60:1",
  "hash": "f6f635333a379f07c865489c266d43986c448f6a5f3469a9ab91f1ec789658b2",
  "cid": "QmV1f6f635333a379f07c865489c266d43986c448f6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292790,
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
      "evaluated_at": 1760292790
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
  "sig": "d890ccdadb207c19a14a17e257bd764214508b14bb432e7ee94d65759dc2138d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026472141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 42232460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285764, 'matching_hash': 'c34da1cfbf75ff05'}}}