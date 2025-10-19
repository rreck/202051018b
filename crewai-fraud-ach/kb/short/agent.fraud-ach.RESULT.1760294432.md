```json
{
  "id": "a494b0d17d90c094",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294432,
  "host_pid": "9e6742732c60:1",
  "hash": "f7b592253acc81e3e567ad6966a4fd516edda9c028ddbe40ae3147b69ce652bb",
  "cid": "QmV1f7b592253acc81e3e567ad6966a4fd516edda9c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294432,
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
      "evaluated_at": 1760294432
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
  "sig": "7a59f94a1acd4994d5de2ab06ec538e62619d12edcbe963e4cb924a433fa0d3c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028779608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 71632288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'f4a7019387fd02e9'}}}