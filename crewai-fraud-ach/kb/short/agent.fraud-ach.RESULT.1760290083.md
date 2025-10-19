```json
{
  "id": "411c6254de624e42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290083,
  "host_pid": "9e6742732c60:1",
  "hash": "2c7932b59e92524d818eaf89f253f390630140eef6fa91622dac455ccffff695",
  "cid": "QmV12c7932b59e92524d818eaf89f253f390630140ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290083,
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
      "evaluated_at": 1760290083
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
  "sig": "dd74c3742168578c63368cb3ee6b6f23047f6be4e91cf3a5364fb7df044f17dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150592686
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '43d52159a9989a8b'}}}