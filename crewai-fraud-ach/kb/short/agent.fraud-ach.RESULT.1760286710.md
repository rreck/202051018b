```json
{
  "id": "67d94a61cd57178d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286710,
  "host_pid": "9e6742732c60:1",
  "hash": "d0dcd02f032931ff45d9512df5cbb61796af7af75dceb098ca34212a3916b1e4",
  "cid": "QmV1d0dcd02f032931ff45d9512df5cbb61796af7af7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286710,
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
      "evaluated_at": 1760286710
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
  "sig": "ee367d92faa4492684c68aa98bab3aa86f185eecd57878c72218a5aecf395b7e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000027607406
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}