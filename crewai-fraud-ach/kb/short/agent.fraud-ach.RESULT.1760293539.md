```json
{
  "id": "117f86e10392b826",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293539,
  "host_pid": "9e6742732c60:1",
  "hash": "2322ef1230e0b37dbff81b62bb5b6f6c8d8e84b3f63dc5093897e8c56d62b864",
  "cid": "QmV12322ef1230e0b37dbff81b62bb5b6f6c8d8e84b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293539,
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
      "evaluated_at": 1760293539
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
  "sig": "419a47858a9cfeb0ea6e4e586540d3d58fd66d7ff102211276db46140f8a3f7b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276764543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 72160440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': '861ebf9054cc2433'}}}