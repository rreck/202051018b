```json
{
  "id": "d9ebfab446b31af5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293164,
  "host_pid": "9e6742732c60:1",
  "hash": "dc992f2ac24361af79f1f615a35c8f24e826d8d48c7c722aa4d789bbd423462e",
  "cid": "QmV1dc992f2ac24361af79f1f615a35c8f24e826d8d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293164,
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
      "evaluated_at": 1760293164
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
  "sig": "c541ca8cbf65c0badfae3899300f4449ad30517cc34ee6be08eb91d42241a2b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462075291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 67295007, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '75f7f0ceec197518'}}}