```json
{
  "id": "77bdfe946601d1fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291976,
  "host_pid": "9e6742732c60:1",
  "hash": "e27f7996eeb7255bbd390057068f4da8aa0ff3aad55771a285c4fa206e636208",
  "cid": "QmV1e27f7996eeb7255bbd390057068f4da8aa0ff3aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291976,
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
      "evaluated_at": 1760291976
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
  "sig": "5923f84f91169fd4855105a1e96135c8fd9eeab16b2302f2fbfac6f24bd70a02"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 478694940117269
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 36206940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285764, 'matching_hash': 'c8ebc968ccc74844'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '478694940', 'validation_error': 'Invalid routing number checksum'}}}