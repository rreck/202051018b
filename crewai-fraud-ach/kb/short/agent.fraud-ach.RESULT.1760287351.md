```json
{
  "id": "449501adba601397",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287351,
  "host_pid": "9e6742732c60:1",
  "hash": "7a3cdf70668b86317f62f633ec20414eb0fe3a36924d24e44d5a8d6ecdd8858b",
  "cid": "QmV17a3cdf70668b86317f62f633ec20414eb0fe3a36",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287351,
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
      "evaluated_at": 1760287351
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
  "sig": "35cfd1d55a3112fffc0df7cceefe5117067be8a104b778999ea0283a11644e89"
}
```

Fraud detected: duplicate_transaction (score: 74)
Transaction: 021000027363246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 64, 'details': {'transaction_count': 57, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285764, 'matching_hash': 'ed45becb5b65c89d'}}}een': 1760285763, 'matching_hash': '5c0c0fe7ab2d6845'}}}