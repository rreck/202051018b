```json
{
  "id": "7443a1b7d299409d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292655,
  "host_pid": "9e6742732c60:1",
  "hash": "924531deee569a782a770e87e0e2642a058808e1c1fdcf644bd154027880e0a5",
  "cid": "QmV1924531deee569a782a770e87e0e2642a058808e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292655,
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
      "evaluated_at": 1760292655
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
  "sig": "f6e47326f9da8f08137aa11a72a98a8b02e721ba855ab3f4824d71cb0dfc36de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592035169
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 278, 'threshold': 50, 'total_amount': 131324698, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 277, 'first_seen': 1760284979, 'matching_hash': 'af51af40be20c608'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}