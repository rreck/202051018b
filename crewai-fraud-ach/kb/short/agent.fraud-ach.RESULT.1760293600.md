```json
{
  "id": "6994970c007a4985",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293600,
  "host_pid": "9e6742732c60:1",
  "hash": "cde5db5f7e1d1b13cd20a7e0bed95a1b2f7bc5e0e6c0c526cc968311bc3b8cd7",
  "cid": "QmV1cde5db5f7e1d1b13cd20a7e0bed95a1b2f7bc5e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293600,
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
      "evaluated_at": 1760293600
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
  "sig": "db6a9878401bad353b9cb79f11d5fe3cd35acdbb0b75408462233ff64f9f419b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029996971
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 23090886, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '92fd98aa1089d1f1'}}}