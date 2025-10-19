```json
{
  "id": "54d0900d781fe2ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286874,
  "host_pid": "9e6742732c60:1",
  "hash": "4f4415644dde0ed5fd1245fdb986b1af9bbf29c06e8568d75962e3558165ef7c",
  "cid": "QmV14f4415644dde0ed5fd1245fdb986b1af9bbf29c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286874,
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
      "evaluated_at": 1760286874
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
  "sig": "07a1039b562a69b89d22dade51633e82255d1767cd2e33c4edfea878047fa2de"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105159090424
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285764, 'matching_hash': 'fe78f8ea626833d8'}}}