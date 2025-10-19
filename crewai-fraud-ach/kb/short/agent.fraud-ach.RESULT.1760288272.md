```json
{
  "id": "5b12eee824aeabb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288272,
  "host_pid": "9e6742732c60:1",
  "hash": "612e74c8f0493f76948d20b2bc4158f29f3752503e94816d749588ccbab690f6",
  "cid": "QmV1612e74c8f0493f76948d20b2bc4158f29f375250",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288272,
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
      "evaluated_at": 1760288272
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
  "sig": "36969e4c45b0b59ee4c67a7f17e0dff83ac187486694dd38b07855deb1a1d0f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036487644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 68994308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760284979, 'matching_hash': '0d42dcc750e3a553'}}}