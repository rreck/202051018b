```json
{
  "id": "032c240144d670aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286815,
  "host_pid": "9e6742732c60:1",
  "hash": "05debbada1fe4638cc230623caf3e60194692e2e4190cb2e07d50d399e26ec8e",
  "cid": "QmV105debbada1fe4638cc230623caf3e60194692e2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286815,
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
      "evaluated_at": 1760286815
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
  "sig": "873c3a0c5db859f0220ec7bb8b1119cd5ffdd013b074b54b9f57a3491e2798dc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240631421
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285763, 'matching_hash': 'a12eb13bd276459e'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': '9c6ceec1730a6176'}}}