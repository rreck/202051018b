```json
{
  "id": "e4340f459ba6c67e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287883,
  "host_pid": "9e6742732c60:1",
  "hash": "a37250224007b1867e2a238e09f86fe9a37c74df6160f7200bf12e7f59a6bb5b",
  "cid": "QmV1a37250224007b1867e2a238e09f86fe9a37c74df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287883,
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
      "evaluated_at": 1760287883
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
  "sig": "7b8e8a139a805500f019def5c602a4b80e13c06d30415eaa0a11071484c4f162"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082317
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 28893000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285765, 'matching_hash': '7a1c6367235ff38a'}}}