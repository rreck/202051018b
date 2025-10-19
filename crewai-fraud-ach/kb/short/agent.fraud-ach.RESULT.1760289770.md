```json
{
  "id": "8a72ea3a65f10d40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289770,
  "host_pid": "9e6742732c60:1",
  "hash": "286f8abb857635d0417bba0faf0351018a101e002c8f4b200d843b594c04bd2a",
  "cid": "QmV1286f8abb857635d0417bba0faf0351018a101e00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289770,
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
      "evaluated_at": 1760289770
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
  "sig": "23340653ab5a92131c10d8563470cd3a1e3e580c739c3ed855b331aaddde479f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 42008736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}