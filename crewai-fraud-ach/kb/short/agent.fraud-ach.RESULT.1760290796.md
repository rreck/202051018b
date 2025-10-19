```json
{
  "id": "d6f100bde77c0cde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290796,
  "host_pid": "9e6742732c60:1",
  "hash": "4adebed52dfed23d6a70ad55bccc203620011619d91e001093c6dbc2ffabd440",
  "cid": "QmV14adebed52dfed23d6a70ad55bccc203620011619",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290796,
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
      "evaluated_at": 1760290796
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
  "sig": "91f8ac625e99917ec4539005af26bde8b254e9ca817a2afe0d7c8ba48d31e0f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466004729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 45355863, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285765, 'matching_hash': '1e26fed2c08b1370'}}}