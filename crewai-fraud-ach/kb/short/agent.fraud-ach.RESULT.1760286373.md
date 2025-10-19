```json
{
  "id": "32c994322806fd3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286373,
  "host_pid": "9e6742732c60:1",
  "hash": "d23e9ee023773a6eb99b7b429e5dc8b64877bf0e4da90616ea33d151e74fabbd",
  "cid": "QmV1d23e9ee023773a6eb99b7b429e5dc8b64877bf0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286373,
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
      "evaluated_at": 1760286373
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
  "sig": "2df8ad19460016e510cab68554ab8780c3879d2c8170564e6ae26eb08ea76923"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100274472610
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285764, 'matching_hash': '7db40904e20d1f88'}}}