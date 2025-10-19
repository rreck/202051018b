```json
{
  "id": "24c1cb4fb25191ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291631,
  "host_pid": "9e6742732c60:1",
  "hash": "66ab7eaf36a70623ba9ab807c339152d1e4b8b73a83ebce0f265fc22e3488383",
  "cid": "QmV166ab7eaf36a70623ba9ab807c339152d1e4b8b73",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291631,
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
      "evaluated_at": 1760291631
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
  "sig": "aec57bf68d829bf8e3284018953476de985a88aa73d3b11d42fa058c1699e02b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021718881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 23424477, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': 'c5f4c03352e0db07'}}}