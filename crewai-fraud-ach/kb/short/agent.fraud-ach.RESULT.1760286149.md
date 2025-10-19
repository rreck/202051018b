```json
{
  "id": "262bd7aaaab6ecf6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286149,
  "host_pid": "9e6742732c60:1",
  "hash": "9cd47115284cb8784ac0da2e89acb4adfaac1782542bd9d353dfd68f98dc54da",
  "cid": "QmV19cd47115284cb8784ac0da2e89acb4adfaac1782",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286149,
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
      "evaluated_at": 1760286149
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
  "sig": "680151f6f494520ede8801cf5b1d63e489fa8ca24abc2546d59948fc2bba96a5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201461662622
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285763, 'matching_hash': '96e0bea374e50243'}}}