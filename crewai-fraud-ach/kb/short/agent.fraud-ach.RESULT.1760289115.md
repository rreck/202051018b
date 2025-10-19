```json
{
  "id": "1ca2a8192be3af9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289115,
  "host_pid": "9e6742732c60:1",
  "hash": "55eaeae53547c43e72b7083a27c57d9159f7c64fe64b011fdb9b38352476b6c7",
  "cid": "QmV155eaeae53547c43e72b7083a27c57d9159f7c64f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289115,
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
      "evaluated_at": 1760289115
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
  "sig": "ea7570c5dc9c4417683578a2108d5a1c7cd064da208847217b6c1b26ff63ad27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469258561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 29610474, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': 'c5dbb685e09199e5'}}}