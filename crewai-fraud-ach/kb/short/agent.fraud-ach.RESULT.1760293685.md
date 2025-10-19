```json
{
  "id": "37e6093334736c6f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293685,
  "host_pid": "9e6742732c60:1",
  "hash": "e9aa1780fae2ad98982a331f8be05ecc43e5ad1ed1d041fa84418ceb527082d5",
  "cid": "QmV1e9aa1780fae2ad98982a331f8be05ecc43e5ad1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293685,
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
      "evaluated_at": 1760293685
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
  "sig": "c5440be6fa442ccd115923eb2d556975df8fd8b5b9fc3248bf5ca4cb3af47f8d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274395247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 73111665, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285765, 'matching_hash': '7ef610f7539e9ec6'}}}