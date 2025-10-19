```json
{
  "id": "a1153e7172dc54eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288428,
  "host_pid": "9e6742732c60:1",
  "hash": "734e06594a5346de65cccd26fff5d6183a7c895ae5f3d1fe966217d7002f23b9",
  "cid": "QmV1734e06594a5346de65cccd26fff5d6183a7c895a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288428,
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
      "evaluated_at": 1760288428
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
  "sig": "be9b895d446b19851fe97dbf15d0cc09edcf498b6ecfc2c6a0c543a036a72469"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285764, 'matching_hash': '763c66b493018133'}}}een': 1760285763, 'matching_hash': '43945ca7b36522b2'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}