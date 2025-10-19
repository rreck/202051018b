```json
{
  "id": "5b510bbf0f24425f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291646,
  "host_pid": "9e6742732c60:1",
  "hash": "3a516073443145dcb1f1b42859861ed2f932d0f42f079c4cf17b225e8765aa2a",
  "cid": "QmV13a516073443145dcb1f1b42859861ed2f932d0f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291646,
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
      "evaluated_at": 1760291647
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "a7a3c687b123bef08b8fed9899f4bc6f962193d81c185a6ffb971ccf6f34d4e1"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 261425243879882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 59462460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': 'bea146cfc71ce9bb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}