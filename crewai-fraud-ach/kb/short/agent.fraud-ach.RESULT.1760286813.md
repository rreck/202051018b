```json
{
  "id": "abd8e7d8218ecfde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286813,
  "host_pid": "9e6742732c60:1",
  "hash": "ba4e70999c6fee38022fcffb52e826efc00bd0d5a9aa7c809188d87da3f53b78",
  "cid": "QmV1ba4e70999c6fee38022fcffb52e826efc00bd0d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286813,
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
      "evaluated_at": 1760286813
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
  "sig": "271f36a46b05cbebbc76f9f237c601025c945ecc0cb6b0da56e9b81b63bb401c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009596849873
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10845922, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285763, 'matching_hash': 'd03c8a9dd75ef277'}}}