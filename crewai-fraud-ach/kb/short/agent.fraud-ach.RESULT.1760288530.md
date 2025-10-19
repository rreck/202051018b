```json
{
  "id": "fb7d44636af9b93f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288530,
  "host_pid": "9e6742732c60:1",
  "hash": "e8a896d0be14282d9ac2542c30ad75b2ace8b01b838dbfeab544de48c4d24e38",
  "cid": "QmV1e8a896d0be14282d9ac2542c30ad75b2ace8b01b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288530,
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
      "evaluated_at": 1760288530
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "84bfcaaf4098aa67d7e8d473832c145d67f84f367c3943147e23e981c6c6c553"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 537469236347495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 20324352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': 'a49bc27baafeabf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '537469236', 'validation_error': 'Invalid routing number checksum'}}}