```json
{
  "id": "5479707eef340c51",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288157,
  "host_pid": "9e6742732c60:1",
  "hash": "ca3b44207d2af21b03246ab1fc0e01afe35e62605a5181084cbe849b3035605c",
  "cid": "QmV1ca3b44207d2af21b03246ab1fc0e01afe35e6260",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288157,
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
      "evaluated_at": 1760288157
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
  "sig": "b8690e47be2de6b8ba57eb7314a25c76edc237b86ff39a4b132433b922ba5e60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 35106288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': 'adb809538e6eb6af'}}}