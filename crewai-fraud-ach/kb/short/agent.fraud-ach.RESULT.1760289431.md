```json
{
  "id": "1bb13caf6ece64b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289431,
  "host_pid": "9e6742732c60:1",
  "hash": "f07c0d051dc089e224e11ca6dabc52cd57cf352fc305a870dca6ec010350db8e",
  "cid": "QmV1f07c0d051dc089e224e11ca6dabc52cd57cf352f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289431,
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
      "evaluated_at": 1760289431
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
  "sig": "21158faa68623c0d643e06db41567e176a17aa196ee2af5d02c8689d9425400b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 113877664521121
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 44436210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': '0cc689f8838aa314'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}s': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6602570}}}