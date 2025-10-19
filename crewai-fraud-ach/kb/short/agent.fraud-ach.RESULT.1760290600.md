```json
{
  "id": "f9312c69dd1ce68a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290600,
  "host_pid": "9e6742732c60:1",
  "hash": "d9dede3cc054947d0117e651c1f6a4670c4476a3ef1a024453c98995ac5f79fa",
  "cid": "QmV1d9dede3cc054947d0117e651c1f6a4670c4476a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290600,
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
      "evaluated_at": 1760290600
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
  "sig": "5b0297256de77751d857cb141033122c6938acf5c006750a4da6506faf7c4b1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275178719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 25566618, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285765, 'matching_hash': '267c9e50b53a1b99'}}}