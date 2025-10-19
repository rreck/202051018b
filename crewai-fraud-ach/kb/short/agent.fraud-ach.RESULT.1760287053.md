```json
{
  "id": "9c4fe7adba850929",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287053,
  "host_pid": "9e6742732c60:1",
  "hash": "261ac932c788ff81019e4b37dcdbe353bb3a0c7a3aec7ff63a82dca99d059058",
  "cid": "QmV1261ac932c788ff81019e4b37dcdbe353bb3a0c7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287053,
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
      "evaluated_at": 1760287053
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
  "sig": "08a0d1e5f58f89801533cfffdf4a3223bd6ecf9c6eabb3f639428d20989af2a4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462224628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10717540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': '4ca3be34af08dccb'}}}