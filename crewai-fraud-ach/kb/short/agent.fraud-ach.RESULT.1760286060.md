```json
{
  "id": "d813559c28129466",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286060,
  "host_pid": "9e6742732c60:1",
  "hash": "25ca31db7b215baabc883b4aafff617710d859ad218beeaae45952e8cf4a139c",
  "cid": "QmV125ca31db7b215baabc883b4aafff617710d859ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286060,
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
      "evaluated_at": 1760286060
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
  "sig": "f0957da78e0792f5ca48d60b0c2213beefb8af2181f604bafd6a1c43714f2525"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000021988031
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285764, 'matching_hash': '88465ad333807d91'}}}