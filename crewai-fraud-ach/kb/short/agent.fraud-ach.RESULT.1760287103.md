```json
{
  "id": "ab65a18f46503bc1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287103,
  "host_pid": "9e6742732c60:1",
  "hash": "0ddc0a3f9e5171ca97bd41d2549ddb1a039ca6b3d2826a7168b784740722636b",
  "cid": "QmV10ddc0a3f9e5171ca97bd41d2549ddb1a039ca6b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287103,
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
      "evaluated_at": 1760287103
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
  "sig": "291868d01b7e60caa6c9d7817f2937ff11ba24f72e88a14550ab0e8478bf8639"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009598542542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16053648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285764, 'matching_hash': '3cc1c7bbce52acf6'}}}