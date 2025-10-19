```json
{
  "id": "645e31e2b2fbd7b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289873,
  "host_pid": "9e6742732c60:1",
  "hash": "ab9e481411d4ba491e16070dcf38cd6cc45480495ed43c32118b312e93dbf99a",
  "cid": "QmV1ab9e481411d4ba491e16070dcf38cd6cc4548049",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289873,
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
      "evaluated_at": 1760289873
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
  "sig": "f44e646a1bb25ba71ef05f5bf917dce5fe7b2124fc22a5975be391d9f1fcf5cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275697869
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 28489050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285764, 'matching_hash': '6e45970a6bf10306'}}}