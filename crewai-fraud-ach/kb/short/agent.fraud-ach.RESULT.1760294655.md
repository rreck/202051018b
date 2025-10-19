```json
{
  "id": "735483599989828f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294655,
  "host_pid": "9e6742732c60:1",
  "hash": "f02a5cc5a7b25db7742f4e99f001b97b73c241dc9ea7c36dd4a865e3cd5b163d",
  "cid": "QmV1f02a5cc5a7b25db7742f4e99f001b97b73c241dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294655,
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
      "evaluated_at": 1760294655
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
  "sig": "2e6f5f9050b4f289e6748763007513e0f8ab14e599883c7973e28ad3de1d113d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467071616
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 108838048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': 'cbd6f8586f75cfb9'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}