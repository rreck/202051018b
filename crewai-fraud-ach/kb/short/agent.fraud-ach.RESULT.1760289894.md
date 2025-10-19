```json
{
  "id": "263fe70f9b5d48fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289894,
  "host_pid": "9e6742732c60:1",
  "hash": "c74b861ddb16ffcd4c22090c3038d0b789452705700c8f0d3b1c25400c85b787",
  "cid": "QmV1c74b861ddb16ffcd4c22090c3038d0b789452705",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289894,
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
      "evaluated_at": 1760289894
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
  "sig": "77544f6752fad8dd7da6ed4c61301830e52b05de01e288739748dea29460e86d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028841300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 25423160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': 'f5bed59f6c250fae'}}}