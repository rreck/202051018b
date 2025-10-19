```json
{
  "id": "5c04eb374fdd6713",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285514,
  "host_pid": "9e6742732c60:1",
  "hash": "c17d1980bcdc4662126c19d99f33dd10c7300aead7eed11d18e5760146736e0b",
  "cid": "QmV1c17d1980bcdc4662126c19d99f33dd10c7300aea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285514,
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
      "evaluated_at": 1760285514
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
  "sig": "dacfc8c75f0fa04a172723f5023db09c8b96a35633836eaa260e2c89c93601b8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105154887163
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 18645347, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760284979, 'matching_hash': '445784114b53d57b'}}}