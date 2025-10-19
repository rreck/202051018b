```json
{
  "id": "18920896c048bf36",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286091,
  "host_pid": "9e6742732c60:1",
  "hash": "0a866af8a4d0849bb23543a0f13fe1eb99c9b0bcf0574d65698ecda01da627f8",
  "cid": "QmV10a866af8a4d0849bb23543a0f13fe1eb99c9b0bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286091,
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
      "evaluated_at": 1760286091
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
  "sig": "c8d586aaf4760a84e28886168616c987394c9e774a54e6c7c78e4d9ed83b579d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000026701294
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285764, 'matching_hash': 'c6488d75609f0f90'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}