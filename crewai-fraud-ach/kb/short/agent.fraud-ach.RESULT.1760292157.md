```json
{
  "id": "0c7ea926b192d7e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292157,
  "host_pid": "9e6742732c60:1",
  "hash": "175a384f60ddc87325794688af05ea4277b2100a40b446889543858f699b404d",
  "cid": "QmV1175a384f60ddc87325794688af05ea4277b2100a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292157,
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
      "evaluated_at": 1760292157
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
  "sig": "c0c4f5f68c12423d123e647a6e81a14d03bd300a7622e99415528f0d4f88fb5c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 10910684, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}