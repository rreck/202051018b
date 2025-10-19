```json
{
  "id": "cfca15433a0b3a31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290025,
  "host_pid": "9e6742732c60:1",
  "hash": "632708cd351b3077b7f011edb3210401ded60dcb4e39dada57e8363320e9ff1f",
  "cid": "QmV1632708cd351b3077b7f011edb3210401ded60dcb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290025,
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
      "evaluated_at": 1760290025
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
  "sig": "5877dcb81a0d357f3331f606fb1963c1489b6c6d2be2b4113f26d83f009f5efd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153539871
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 34750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285765, 'matching_hash': '6120bfc166994b37'}}}