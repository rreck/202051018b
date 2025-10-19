```json
{
  "id": "05bff0c3d62f78af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290738,
  "host_pid": "9e6742732c60:1",
  "hash": "ebb8a30873dd0b234207dfec124fa482f2696048d044a0f7e456abb4436a1ca7",
  "cid": "QmV1ebb8a30873dd0b234207dfec124fa482f2696048",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290738,
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
      "evaluated_at": 1760290738
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
  "sig": "ab1c411a525a68c18504b92a280a73b5fa628563b57c510c8722b276afe3b49a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244163284273009
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 52329284, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': '5b6cb55161b8e1f8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}