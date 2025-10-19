```json
{
  "id": "dcce01da89992fa0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291848,
  "host_pid": "9e6742732c60:1",
  "hash": "032f386edef5faa4cd6c7da5f6917e58f79258a3f0effc81e747e21b5e6f4174",
  "cid": "QmV1032f386edef5faa4cd6c7da5f6917e58f79258a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291848,
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
      "evaluated_at": 1760291848
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
  "sig": "b223ef487b55e63195e5fbf0af33b7d4ff2951de043703c457921d79e3fedf79"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597421131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 42938424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': 'ee859bd02c19b1f0'}}}