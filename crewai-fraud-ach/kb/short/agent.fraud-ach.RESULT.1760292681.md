```json
{
  "id": "403fb4bedf4f52d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292681,
  "host_pid": "9e6742732c60:1",
  "hash": "f7b58fa667a971335b6b559c2d978885c54f4effbe30f2e8a9abda819574f2f0",
  "cid": "QmV1f7b58fa667a971335b6b559c2d978885c54f4eff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292681,
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
      "evaluated_at": 1760292681
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
  "sig": "cba888fc67bf5b7c6387b155001143adc9d14842f740e025cd3439fc08c92994"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 580123061332551
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 42742665, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': 'b65f94a39c8828ce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}