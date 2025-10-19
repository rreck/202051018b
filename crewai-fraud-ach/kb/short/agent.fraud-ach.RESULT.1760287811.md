```json
{
  "id": "83c040f438263c22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287811,
  "host_pid": "9e6742732c60:1",
  "hash": "061870457c9e43217cab1cd203b43ca5ef86624e8c72c785e1babeefa1583e90",
  "cid": "QmV1061870457c9e43217cab1cd203b43ca5ef86624e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287811,
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
      "evaluated_at": 1760287811
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
  "sig": "6de6c6bf812cc7a4680093448392aee2df204a94656ceaa692426caed57350e8"
}
```

Fraud detected: invalid_routing (score: 92)
Transaction: 053611743401753
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 14874480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285764, 'matching_hash': 'ed032d3a1e3d03a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}