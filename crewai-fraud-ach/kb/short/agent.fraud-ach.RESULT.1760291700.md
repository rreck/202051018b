```json
{
  "id": "0307a6efa7937f63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291700,
  "host_pid": "9e6742732c60:1",
  "hash": "b269b1a01a6ac789e5267f72e02ed8f53fc2bc1e277e1c75a9f2ef5df6362649",
  "cid": "QmV1b269b1a01a6ac789e5267f72e02ed8f53fc2bc1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291700,
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
      "evaluated_at": 1760291700
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
  "sig": "297fa39cec2961f69597f67863d2b63aebb57b395137b59a0f8f275e7bc29980"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029588067
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 55706370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285764, 'matching_hash': '5ca8480d00f733c5'}}}