```json
{
  "id": "1ac1ff2d1d2c5468",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294902,
  "host_pid": "9e6742732c60:1",
  "hash": "95c7fb815d0f170c4323e975f0b5441cb2d25dd8cac102bba4539c562359b5e3",
  "cid": "QmV195c7fb815d0f170c4323e975f0b5441cb2d25dd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294902,
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
      "evaluated_at": 1760294902
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
  "sig": "c96e61435b44ea6b7db1024fbc913a8e2223d8827a1681dd02b818c8b0259105"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021480535
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 121338762, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}