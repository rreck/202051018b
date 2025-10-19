```json
{
  "id": "399ef147e5b06050",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293230,
  "host_pid": "9e6742732c60:1",
  "hash": "d37433f4a273c23cb45171f52a723fdb66cd4204c3ca7f1631d78b9714428aff",
  "cid": "QmV1d37433f4a273c23cb45171f52a723fdb66cd4204",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293230,
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
      "evaluated_at": 1760293230
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
  "sig": "3d35b4dd8c603f794bb71db75be170feb84938601285a06eb27f0d370e5e2c21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024300942
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 17275578, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '95903848ba405d51'}}}