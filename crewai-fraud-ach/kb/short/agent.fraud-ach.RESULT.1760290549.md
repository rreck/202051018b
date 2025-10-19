```json
{
  "id": "8e32308785888640",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290549,
  "host_pid": "9e6742732c60:1",
  "hash": "f8d977975b6c85c602128cabf87cc4a615c7b022d6f8c16356242e35c5d1e82a",
  "cid": "QmV1f8d977975b6c85c602128cabf87cc4a615c7b022",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290549,
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
      "evaluated_at": 1760290549
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
  "sig": "775749e3f21e9f09f9ba6276618ec5aa7704caa3aadae689f602cea650898562"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023745358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 23477391, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285764, 'matching_hash': '29c890c1b3276ef0'}}}