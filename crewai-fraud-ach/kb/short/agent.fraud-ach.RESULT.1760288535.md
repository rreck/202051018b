```json
{
  "id": "1aa4360cfe5e9b65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288535,
  "host_pid": "9e6742732c60:1",
  "hash": "95a2c6552d22ed544e754e1df74c31a9fe2a7b983059e0a29cedf570e509de80",
  "cid": "QmV195a2c6552d22ed544e754e1df74c31a9fe2a7b98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288535,
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
      "evaluated_at": 1760288535
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
  "sig": "a86c11559a123fa7f2e3e12691bfa672369cd6f7d2596b9e29536f02d2fa4b6b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469526930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 10922688, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}