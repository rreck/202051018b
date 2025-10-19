```json
{
  "id": "10d9222f56f1325b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287470,
  "host_pid": "9e6742732c60:1",
  "hash": "12f7582608c5f9a9cfa57c2f4f07a72e1fea946f70db5b318b6d0184e927ecbc",
  "cid": "QmV112f7582608c5f9a9cfa57c2f4f07a72e1fea946f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287470,
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
      "evaluated_at": 1760287470
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "5350f93eeb12400a0ab72ee9ff1742097ea8935a2dc267a6c2fd7b1a15420754"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 031201462505262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 23883574, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285764, 'matching_hash': 'e15f6eb56271d036'}}}