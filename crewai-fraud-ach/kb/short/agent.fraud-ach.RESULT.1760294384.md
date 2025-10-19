```json
{
  "id": "7d1a10724956c6fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294384,
  "host_pid": "9e6742732c60:1",
  "hash": "f8d028b38d56ba6254cd11747b80324c912b2e7b370a9f0795761ae32fc45611",
  "cid": "QmV1f8d028b38d56ba6254cd11747b80324c912b2e7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294384,
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
      "evaluated_at": 1760294384
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
  "sig": "782fba4c20951322f11c12c8317a196d56d09649a5ed03157cf262f43c3e07cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030505524
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 106524627, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': '58071665864a5dbb'}}}