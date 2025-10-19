```json
{
  "id": "f9c590312c20276b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290663,
  "host_pid": "9e6742732c60:1",
  "hash": "ebbe1c4b42609dba50c896d30796cfee8d70fab3a9fa32827b0e1b3ea0fe2abe",
  "cid": "QmV1ebbe1c4b42609dba50c896d30796cfee8d70fab3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290663,
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
      "evaluated_at": 1760290663
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
  "sig": "cd3d1e3f067dff3dc21797d8dd5087c995c257007360ab74930107979f85f1b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277214063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 44702580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': 'ff6f9f90137c8ef9'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '442437646', 'validation_error': 'Invalid routing number checksum'}}}