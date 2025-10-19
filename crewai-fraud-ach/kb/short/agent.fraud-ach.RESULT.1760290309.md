```json
{
  "id": "45bdbeb98d1f6118",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290309,
  "host_pid": "9e6742732c60:1",
  "hash": "39491b9c4509fafa4eedb4a66f5942a7715ad0b7592883ae11ee11f50c89bfd3",
  "cid": "QmV139491b9c4509fafa4eedb4a66f5942a7715ad0b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290309,
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
      "evaluated_at": 1760290309
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
  "sig": "d541565668648020aee379a6ebfbd83a1263abfcbb81bdd3e8d3c96ae379ae20"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596354415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 40915245, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': 'f20df65cb297838c'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '586667919', 'validation_error': 'Invalid routing number checksum'}}}