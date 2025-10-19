```json
{
  "id": "c77bb972803c09eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291774,
  "host_pid": "9e6742732c60:1",
  "hash": "a18acca3c18ef3e530adc9dd920d155822d81a63e3794b4f920ec28b8ccca2ee",
  "cid": "QmV1a18acca3c18ef3e530adc9dd920d155822d81a63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291774,
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
      "evaluated_at": 1760291774
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
  "sig": "ffa8ba93f992625eaf2153b64563684986051769e5d4be7b51c90fe39c84469f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037990803
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 42593250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}