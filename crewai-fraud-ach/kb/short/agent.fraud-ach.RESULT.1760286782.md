```json
{
  "id": "e62cc8615165db1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286782,
  "host_pid": "9e6742732c60:1",
  "hash": "fce4f7d35875ab9f28dcff7888e31c9ad5399cae5aca56bb095c6d53aeffa5de",
  "cid": "QmV1fce4f7d35875ab9f28dcff7888e31c9ad5399cae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286782,
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
      "evaluated_at": 1760286782
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
  "sig": "c2160810d4fd57c48f71da5c84c9276c1362b2135a11325a0312d959e9dd04e0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000245124241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12040651, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285764, 'matching_hash': '1e6f1dd53bdf6417'}}}