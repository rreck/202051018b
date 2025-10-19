```json
{
  "id": "2861986012e224c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286191,
  "host_pid": "9e6742732c60:1",
  "hash": "b7db94046e596e447b0d4b0641c3b314652d0ab30fac1fe15f0e632bbe61b72e",
  "cid": "QmV1b7db94046e596e447b0d4b0641c3b314652d0ab3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286191,
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
      "evaluated_at": 1760286191
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
  "sig": "edd4de52a278901ffb74034769a81605d0c6b9b29e4fbe31902a58d9d20a230d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025503816
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}