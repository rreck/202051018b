```json
{
  "id": "d6e639f43ff49cf6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288087,
  "host_pid": "9e6742732c60:1",
  "hash": "c66e63cc0be917e802ee5fdb0851dd48665d5062605a9065b1dc436be452872b",
  "cid": "QmV1c66e63cc0be917e802ee5fdb0851dd48665d5062",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288087,
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
      "evaluated_at": 1760288087
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
  "sig": "26031f778da692a6b2380d0e90e38e5fb58f606b3d0b108886538b6e544d084c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}