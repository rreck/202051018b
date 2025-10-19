```json
{
  "id": "534e4504952ce04c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286952,
  "host_pid": "9e6742732c60:1",
  "hash": "746d2a260700b141da6a082f4afdd08b00e82529f2cb70556550b33c0d1d628a",
  "cid": "QmV1746d2a260700b141da6a082f4afdd08b00e82529",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286952,
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
      "evaluated_at": 1760286952
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
  "sig": "b4691f1bd4fd2cffd236d2855b9d100b862e3e6a20b24eb816995919c8413e15"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16400458, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}