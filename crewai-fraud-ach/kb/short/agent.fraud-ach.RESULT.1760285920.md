```json
{
  "id": "f621241c0a95d1b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285920,
  "host_pid": "9e6742732c60:1",
  "hash": "862698c6ce4bc457a9deced7857f34f6590202ff3509eb484e7df39b002507ad",
  "cid": "QmV1862698c6ce4bc457a9deced7857f34f6590202ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285920,
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
      "evaluated_at": 1760285920
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
  "sig": "306ee7139d85641d812589c8c34a91e666a8f2eb9dffe3a94b9aba76635bd8e4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034053694
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285765, 'matching_hash': 'f3f5d61420936f73'}}}