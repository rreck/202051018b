```json
{
  "id": "3113209275f35def",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294094,
  "host_pid": "9e6742732c60:1",
  "hash": "884ea9d90bd5b8c6409925b5841d74d90d6302612e43f92f2bf077ede1732f31",
  "cid": "QmV1884ea9d90bd5b8c6409925b5841d74d90d630261",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294094,
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
      "evaluated_at": 1760294094
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
  "sig": "63c6eaed9f02bd08e001debbe8e971a85e51d2db6e911083ee31511963354076"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031078531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 17764593, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}