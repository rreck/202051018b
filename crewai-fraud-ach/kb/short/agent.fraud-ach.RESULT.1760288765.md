```json
{
  "id": "e3cb350f456d8b47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288765,
  "host_pid": "9e6742732c60:1",
  "hash": "6b55ead2416d0ef76f331a167c9a096de2d75c3ff5aa1c8d581a01a8c6958d5d",
  "cid": "QmV16b55ead2416d0ef76f331a167c9a096de2d75c3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288765,
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
      "evaluated_at": 1760288765
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
  "sig": "5826658877c9bc3d2943abb79c5db13e13159bf15a451d14431b2bf82e9488c2"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 763245925890246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 46770755, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285764, 'matching_hash': '634500dd7ac761f0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '763245921', 'validation_error': 'Invalid routing number checksum'}}}