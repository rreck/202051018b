```json
{
  "id": "37fdefcca211c441",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292069,
  "host_pid": "9e6742732c60:1",
  "hash": "8ad910e2dc79e5b9895be07c4d7e5ff329224ff6e854fd66d4d6ade5aebd1112",
  "cid": "QmV18ad910e2dc79e5b9895be07c4d7e5ff329224ff6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292069,
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
      "evaluated_at": 1760292069
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
  "sig": "8d5cfa2883a6e57e18dc016947a11b0668a60f548f675766e148c5cb7bae9711"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599905929
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 73420830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': 'da08c58383816f07'}}}