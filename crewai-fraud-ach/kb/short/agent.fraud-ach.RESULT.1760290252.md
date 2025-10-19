```json
{
  "id": "05352772c4643514",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290252,
  "host_pid": "9e6742732c60:1",
  "hash": "55d59c6993ac9f7968659f59a74525cdac700299bb8e8c53f16ca7fee8a064b9",
  "cid": "QmV155d59c6993ac9f7968659f59a74525cdac700299",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290252,
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
      "evaluated_at": 1760290252
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
  "sig": "9c7961ba726043b531956ec6c79e6324ab1ce3acab2267b99f13a974532b9ded"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592654855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 43781735, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': '0ed93ea6dd0046b6'}}}