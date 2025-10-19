```json
{
  "id": "891e97d1f726eab5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288957,
  "host_pid": "9e6742732c60:1",
  "hash": "e765ef83a1590a06e59db1aa9c1fa5f9aeb8e0ee6ae2400a8ba556ae16131a20",
  "cid": "QmV1e765ef83a1590a06e59db1aa9c1fa5f9aeb8e0ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288957,
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
      "evaluated_at": 1760288957
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
  "sig": "8bd5cbdf45d0ef7112b1aba7bbda23e3c8cfd765f722c7fa1a86364d40db792f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026494478
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 20657353, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': 'bca1271a1f86b87c'}}}