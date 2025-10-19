```json
{
  "id": "1b644e450b197ebf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286992,
  "host_pid": "9e6742732c60:1",
  "hash": "4a2c55088a071ffeb8460c03baac954d67533713f814cb939bcf40e636c4cbba",
  "cid": "QmV14a2c55088a071ffeb8460c03baac954d67533713",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286992,
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
      "evaluated_at": 1760286992
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
  "sig": "28a49c0fd6c02c42f76dc9eac785eaf0e0dab01f7c65e185769d7b4fbada1b73"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000247499118
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285765, 'matching_hash': 'f65a723d753f6ade'}}}