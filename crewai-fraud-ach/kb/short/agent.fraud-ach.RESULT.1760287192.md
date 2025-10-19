```json
{
  "id": "92c3336be835d378",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287192,
  "host_pid": "9e6742732c60:1",
  "hash": "49d0ab0043d1ae0105cbcea6335304c8bb1758f3f2a2a065aa97ad8d8e2148d2",
  "cid": "QmV149d0ab0043d1ae0105cbcea6335304c8bb1758f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287192,
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
      "evaluated_at": 1760287192
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "5455c08cfd7beb93ad5b785481146cb4ad3db6fd2d62b053197a7a815c49f933"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105152922139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 10198572, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285765, 'matching_hash': '36c7f170a3aff02c'}}}