```json
{
  "id": "39fb7fab26ca1232",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293049,
  "host_pid": "9e6742732c60:1",
  "hash": "d6a4f6d62836fe3388f25d563f8b0f7ce807a8d4aadd2b5b6558f45e09089926",
  "cid": "QmV1d6a4f6d62836fe3388f25d563f8b0f7ce807a8d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293049,
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
      "evaluated_at": 1760293049
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
  "sig": "f99321b2cc43a695924d3953d10907f31a03243d2ba6c3c3f58fe14c7fd87e8d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029236644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 47836950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285765, 'matching_hash': 'c69cf0de1758a1d7'}}}