```json
{
  "id": "07bc07c87d0ad1df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287646,
  "host_pid": "9e6742732c60:1",
  "hash": "6517f98e3d769d52c88a41a2dc7828d9575212d0cfd3cee5f69bdc3528f45e6b",
  "cid": "QmV16517f98e3d769d52c88a41a2dc7828d9575212d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287646,
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
      "evaluated_at": 1760287646
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
  "sig": "f92246e81a55597c9fff1afeda597a633bf9b5a3e599c73635a925cbca97bc04"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 021000025329406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 32449909, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285765, 'matching_hash': '4bb9b304f38123bb'}}}