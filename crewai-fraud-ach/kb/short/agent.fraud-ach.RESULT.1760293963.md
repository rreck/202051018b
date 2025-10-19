```json
{
  "id": "116849b56ec453c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293963,
  "host_pid": "9e6742732c60:1",
  "hash": "4ab8261b4b8c33359f0e471e7616658ebe7ab9e9ac50a29b36b3d370fe888f8e",
  "cid": "QmV14ab8261b4b8c33359f0e471e7616658ebe7ab9e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293963,
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
      "evaluated_at": 1760293963
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
  "sig": "b9a19cf827bd85ee4ee305ce5e6999857e1cd3a9aff71a6828c0415c2bc1758b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592648645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 86609403, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'd7971b176fb0516b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244890022', 'validation_error': 'Invalid routing number checksum'}}}