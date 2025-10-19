```json
{
  "id": "0144b4de82262a07",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286635,
  "host_pid": "9e6742732c60:1",
  "hash": "1c010429dd14d63c89ce6cbd8eb7704a1aaa77e42a91c9544b618293e541a4d4",
  "cid": "QmV11c010429dd14d63c89ce6cbd8eb7704a1aaa77e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286635,
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
      "evaluated_at": 1760286635
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
  "sig": "f4b579fc4a711bb37f343703b400a45f560a0afc4599b6ecc52732d131e08771"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000028779608
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285763, 'matching_hash': 'f4a7019387fd02e9'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285763, 'matching_hash': '9b2dabf2ca05df4f'}}}