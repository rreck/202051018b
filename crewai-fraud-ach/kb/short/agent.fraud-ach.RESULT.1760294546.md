```json
{
  "id": "2f585354ac717a25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294546,
  "host_pid": "9e6742732c60:1",
  "hash": "fc2e54b72595e54da62025522031fb6be5f72a4b1f8a7e781810639fbd2e52c3",
  "cid": "QmV1fc2e54b72595e54da62025522031fb6be5f72a4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294546,
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
      "evaluated_at": 1760294546
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
  "sig": "154f751a2097d553bfbe82d075746ed15a3662f93995f1d0621dabab608c9d1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 107766240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}