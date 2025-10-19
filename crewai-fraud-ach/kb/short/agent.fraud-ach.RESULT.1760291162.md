```json
{
  "id": "22110f850a85f994",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291162,
  "host_pid": "9e6742732c60:1",
  "hash": "fecbcb177a6cfa45fbda1032c9fa7014a24d369aa71858125433ab2e3e195197",
  "cid": "QmV1fecbcb177a6cfa45fbda1032c9fa7014a24d369a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291162,
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
      "evaluated_at": 1760291162
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
  "sig": "17982125c359b7cd391baa9d257ccb3781f8e1e68f6d43d0cc318ea1d4b1de9d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249867755
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 10065888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285765, 'matching_hash': '3e6b26eb59ce898a'}}}