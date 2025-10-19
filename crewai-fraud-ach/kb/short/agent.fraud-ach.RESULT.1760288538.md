```json
{
  "id": "a0378809acc31c0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288538,
  "host_pid": "9e6742732c60:1",
  "hash": "4182abe90b6a35ab1d8a2ce684d216f258a2b1adbd66a56fbd28cb5203319958",
  "cid": "QmV14182abe90b6a35ab1d8a2ce684d216f258a2b1ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288538,
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
      "evaluated_at": 1760288538
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
  "sig": "adba3018c66b5e775a844815c729d144fc1cb8c86d62a782fa910480835fc240"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025341515
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 24119424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285765, 'matching_hash': '76c6a410184ad94b'}}}