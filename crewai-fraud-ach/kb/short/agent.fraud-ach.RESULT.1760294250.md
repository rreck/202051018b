```json
{
  "id": "14e0229a98091ebb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294250,
  "host_pid": "9e6742732c60:1",
  "hash": "856c874bc7f64a43735a4688cfddf022b1d1fb8f91219151074b553c14c4e1e9",
  "cid": "QmV1856c874bc7f64a43735a4688cfddf022b1d1fb8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294250,
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
      "evaluated_at": 1760294250
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
  "sig": "cb40fb6460d5225325ee0f3280a1950fdd9a9f33e6d879929e89ed24ba49a2e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151957108
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 112798296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': 'c64e753eaec43197'}}}