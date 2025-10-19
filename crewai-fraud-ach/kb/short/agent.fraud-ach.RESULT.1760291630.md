```json
{
  "id": "defd8be6806063ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291630,
  "host_pid": "9e6742732c60:1",
  "hash": "8bda7da6b3b0258444f5269f6f8caa5ca5d80aa59740905bed2e68eb2fd30993",
  "cid": "QmV18bda7da6b3b0258444f5269f6f8caa5ca5d80aa5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291630,
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
      "evaluated_at": 1760291630
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
  "sig": "58044767fc891e25caa4894d7508fac02d52db0b6d07d3ed3d9ed7cc242eac27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248581748
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 34222473, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': '6ba0c7e0a23e9d51'}}}